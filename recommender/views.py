from django.shortcuts import render
from django.core.cache import cache
import pandas as pd
import pyarrow as pa
import logging
import os

# Configure logging
logger = logging.getLogger(__name__)

# Load data once at module initialization
try:
    MOVIES_DATA_PATH = os.path.join("static", "top_2k_movie_data.parquet")
    MODEL_PATH = os.path.join("static", "demo_model.parquet")
    
    movies_data = pd.read_parquet(MOVIES_DATA_PATH)
    titles = movies_data['title']
    titles_list = titles.to_list()
    
    # Load model once at startup (CRITICAL FIX: was loading on every request!)
    similarity_model = pa.parquet.read_table(MODEL_PATH).to_pandas()
    logger.info(f"Successfully loaded {len(titles_list)} movies and similarity model")
except Exception as e:
    logger.error(f"Failed to load movie data or model: {e}")
    movies_data = pd.DataFrame()
    titles_list = []
    similarity_model = None


def get_recommendations(movie_id_from_db, movie_db):
    """
    Get movie recommendations based on cosine similarity.
    
    Args:
        movie_id_from_db: Index of the movie in the database
        movie_db: Similarity matrix
        
    Returns:
        List of recommended movies with details
    """
    try:
        # Check cache first
        cache_key = f"recommendations_{movie_id_from_db}"
        cached_result = cache.get(cache_key)
        if cached_result:
            logger.info(f"Returning cached recommendations for movie ID {movie_id_from_db}")
            return cached_result
        
        # Calculate similarity scores
        sim_scores = list(enumerate(movie_db[movie_id_from_db]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:15]  # Get top 14 recommendations (excluding the movie itself)
        
        movie_indices = [i[0] for i in sim_scores]
        output = movies_data.iloc[movie_indices].copy()
        output.reset_index(inplace=True, drop=True)

        response = []
        for i in range(len(output)):
            movie_title = output['title'].iloc[i]
            release_date = output['release_date'].iloc[i]
            director = output['main_director'].iloc[i]
            
            # Build Google search link
            search_query = '+'.join(movie_title.strip().split())
            year = release_date.split("-")[0] if "-" in release_date else release_date
            google_link = f"https://www.google.com/search?q={search_query}+({year})"
            
            response.append({
                'movie_title': movie_title,
                'movie_release_date': release_date,
                'movie_director': director,
                'google_link': google_link,
                'similarity_score': round(sim_scores[i][1] * 100, 1)  # Add similarity percentage
            })
        
        # Cache the result for 1 hour
        cache.set(cache_key, response, 3600)
        logger.info(f"Generated {len(response)} recommendations for movie ID {movie_id_from_db}")
        return response
        
    except Exception as e:
        logger.error(f"Error generating recommendations: {e}", exc_info=True)
        return []


def main(request):
    """
    Main view for movie recommendation system.
    Handles both GET (initial page load) and POST (search) requests.
    """
    # Check if data loaded successfully
    if similarity_model is None or not titles_list:
        logger.error("Movie data not loaded properly")
        return render(request, 'recommender/error.html', {
            'error_message': 'System error: Movie database not available. Please contact administrator.'
        })

    if request.method == 'GET':
        return render(
            request,
            'recommender/index.html',
            {
                'all_movie_names': titles_list,
                'input_provided': False,
                'movie_found': False,
                'recommendation_found': False,
                'recommended_movies': [],
                'input_movie_name': ''
            }
        )

    if request.method == 'POST':
        data = request.POST
        movie_name = data.get('movie_name', '').strip()
        
        # Input validation
        if not movie_name:
            logger.warning("Empty movie name submitted")
            return render(
                request,
                'recommender/index.html',
                {
                    'all_movie_names': titles_list,
                    'input_provided': True,
                    'movie_found': False,
                    'recommendation_found': False,
                    'recommended_movies': [],
                    'input_movie_name': movie_name,
                    'error_message': 'Please enter a movie name'
                }
            )

        # Find movie in database
        if movie_name in titles_list:
            idx = titles_list.index(movie_name)
            logger.info(f"Found movie: {movie_name} at index {idx}")
        else:
            logger.info(f"Movie not found: {movie_name}")
            return render(
                request,
                'recommender/index.html',
                {
                    'all_movie_names': titles_list,
                    'input_provided': True,
                    'movie_found': False,
                    'recommendation_found': False,
                    'recommended_movies': [],
                    'input_movie_name': movie_name
                }
            )

        # Get recommendations
        final_recommendations = get_recommendations(idx, similarity_model)
        
        if final_recommendations:
            return render(
                request,
                'recommender/result.html',
                {
                    'all_movie_names': titles_list,
                    'input_provided': True,
                    'movie_found': True,
                    'recommendation_found': True,
                    'recommended_movies': final_recommendations,
                    'input_movie_name': movie_name
                }
            )
        else:
            logger.error(f"Failed to generate recommendations for: {movie_name}")
            return render(
                request,
                'recommender/index.html',
                {
                    'all_movie_names': titles_list,
                    'input_provided': True,
                    'movie_found': True,
                    'recommendation_found': False,
                    'recommended_movies': [],
                    'input_movie_name': movie_name,
                    'error_message': 'Unable to generate recommendations. Please try again.'
                }
            )
