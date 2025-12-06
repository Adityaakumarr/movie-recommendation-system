# 🎬 CineFinds — AI-Powered Movie Recommendation System

> A stunning, Netflix-inspired movie recommender powered by cosine similarity with a premium cinematic UI experience.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)
![Machine Learning](https://img.shields.io/badge/ML-Cosine%20Similarity-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## ✨ Features

- 🎯 **Smart Recommendations** - Get 14 personalized movie suggestions based on cosine similarity
- 🎨 **Premium UI** - Netflix-inspired dark theme with cinematic fog animations
- ⚡ **Lightning Fast** - Optimized model loading with intelligent caching
- 🔍 **Smart Search** - Autocomplete with 2.5K+ IMDb movies
- ⌨️ **Keyboard Shortcuts** - `Ctrl+K` to search, `Esc` to clear
- 📊 **Similarity Scores** - See how closely each recommendation matches
- 🎭 **Custom Cursor** - Immersive mint-glow cursor effects
- 📱 **Responsive Design** - Works beautifully on all devices

---

## 🧠 Tech Stack

| Category            | Technologies                   |
| ------------------- | ------------------------------ |
| **Backend**         | Django 4.x, Python 3.10+       |
| **Data Processing** | Pandas, PyArrow, Parquet       |
| **Frontend**        | HTML5, CSS3, jQuery            |
| **ML Algorithm**    | Cosine Similarity              |
| **Caching**         | Django Cache Framework         |
| **UI Theme**        | Netflix Dark with Mint Accents |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

2. **Create and activate virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables** (optional)

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Start the development server**

```bash
python manage.py runserver
```

7. **Open your browser**

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

```
Movie-Recommendation-System/
├── recommender/                    # Main Django app
│   ├── templates/
│   │   └── recommender/
│   │       ├── index.html         # Search page
│   │       └── result.html        # Recommendations page
│   ├── static/recommender/
│   │   ├── cursor.css             # Custom cursor styles
│   │   ├── cursor.js              # Cursor animations
│   │   ├── navbar.css             # Navigation styles
│   │   └── page.css               # Global styles
│   ├── views.py                   # Core recommendation logic
│   └── urls.py                    # URL routing
├── movie_recommendation/           # Django project settings
├── static/
│   ├── top_2k_movie_data.parquet  # Movie metadata
│   └── demo_model.parquet         # Similarity matrix
├── requirements.txt               # Python dependencies
├── manage.py                      # Django management script
└── README.md                      # This file
```

---

## 🎯 How It Works

### The Algorithm

CineFinds uses **cosine similarity** to find movies similar to your selection:

1. **Feature Extraction** - Movies are vectorized based on genres, directors, cast, and keywords
2. **Similarity Calculation** - Cosine similarity measures the angle between movie vectors
3. **Ranking** - Top 14 most similar movies are returned with match percentages
4. **Caching** - Results are cached for 1 hour for instant retrieval

### Performance Optimizations

- ✅ **Model loaded once at startup** (not per request)
- ✅ **Intelligent caching** reduces computation
- ✅ **Efficient Parquet format** for fast data loading
- ✅ **Optimized similarity calculations**

---

## ⌨️ Keyboard Shortcuts

| Shortcut               | Action                   |
| ---------------------- | ------------------------ |
| `Ctrl + K` / `Cmd + K` | Focus search bar         |
| `Esc`                  | Clear search and unfocus |
| `Enter`                | Submit search            |

---

## 🎨 UI Features

- **Cinematic Fog Animation** - Slow-moving gradient fog creates depth
- **Mint Glow Accents** - Signature #82D4BB color throughout
- **Custom Cursor** - Glowing mint cursor with smooth tracking
- **Loading States** - Beautiful spinner while fetching recommendations
- **Hover Effects** - Smooth card animations on interaction
- **Autocomplete** - Smart suggestions as you type

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file from `.env.example`:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=INFO
```

### Caching (Optional)

For production, configure Redis caching in `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

---

## 📊 Dataset

The system currently includes:

- **2,500+ movies** from IMDb's top-rated collection
- **Metadata**: Title, director, release date, genres, cast
- **Pre-computed similarity matrix** for instant recommendations

### Training Your Own Model

Use the included Jupyter notebook to train on custom data:

```bash
jupyter notebook Movie_Recommendation_System_Complete_Guide.ipynb
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'django'`

```bash
# Solution: Activate virtual environment and install dependencies
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

**Issue**: `FileNotFoundError: static/demo_model.parquet`

```bash
# Solution: Ensure you're running from the project root directory
cd Movie-Recommendation-System
python manage.py runserver
```

**Issue**: Port 8000 already in use

```bash
# Solution: Use a different port
python manage.py runserver 8080
```

---

## 🚢 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in settings
- [ ] Configure proper `SECRET_KEY`
- [ ] Set up Redis for caching
- [ ] Configure static file serving
- [ ] Set up proper logging
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS
- [ ] Set security headers

### Deploy with Docker (Coming Soon)

```bash
docker-compose up -d
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add docstrings to functions
- Update tests for new features
- Keep UI consistent with existing design

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- Movie data from [IMDb](https://www.imdb.com/)
- UI inspiration from [Netflix](https://www.netflix.com/)
- Font: [BebasNeue](https://fonts.google.com/specimen/Bebas+Neue) & [Inter](https://fonts.google.com/specimen/Inter)
- Icons: [Tabler Icons](https://tabler-icons.io/)

---

## ⭐ Support

If you found this project helpful, please consider:

- ⭐ **Starring** the repository
- 🐛 **Reporting** bugs and issues
- 💡 **Suggesting** new features
- 🔀 **Contributing** code improvements

---

<div align="center">
  <strong>Made with ❤️ and lots of ☕</strong>
  <br>
  <sub>Happy movie watching! 🍿</sub>
</div>
