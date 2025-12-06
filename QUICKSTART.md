# CineFinds - Quick Reference

## 🚀 Quick Commands

### Development

```bash
# Start development server
python manage.py runserver

# Run on different port
python manage.py runserver 8080

# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic
```

### Docker

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

### Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test recommender

# Check code coverage
coverage run --source='.' manage.py test
coverage report
```

## 🔧 Configuration

### Environment Variables

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_URL=redis://localhost:6379/0
LOG_LEVEL=INFO
```

### Cache Settings

```python
# Clear cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
```

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Module Not Found

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Static Files Not Loading

```bash
python manage.py collectstatic --noinput
```

## 📊 Performance Tips

1. **Enable Redis caching** for production
2. **Use PostgreSQL** instead of SQLite for large datasets
3. **Enable GZIP compression** in production
4. **Use CDN** for static files
5. **Monitor logs** for performance issues

## 🔐 Security Checklist

- [ ] Change SECRET_KEY in production
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Enable HTTPS
- [ ] Set secure cookie flags
- [ ] Configure CORS properly
- [ ] Regular security updates

## 📱 API Endpoints

| Endpoint | Method | Description           |
| -------- | ------ | --------------------- |
| `/`      | GET    | Home page with search |
| `/`      | POST   | Get recommendations   |

## 🎨 Color Palette

- **Primary**: #82D4BB (Mint)
- **Background**: #000000 - #111111 (Dark gradient)
- **Text**: #FFFFFF (White)
- **Secondary Text**: #CFCFCF (Light gray)
- **Error**: #FF6B6B (Red)

## ⌨️ Keyboard Shortcuts

- `Ctrl+K` / `Cmd+K` - Focus search
- `Esc` - Clear search
- `Enter` - Submit search

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Redis Documentation](https://redis.io/documentation)
