# Flask + Docker App 🚀

An upgraded **Flask application** containerized with **Docker**.  
Includes multiple routes (HTML + JSON API).

## Features
- Homepage (`/`)
- About Page (`/about`)
- API Endpoint (`/api/info`)

## Run with Docker
```bash
docker build -t flask-info-app:1.0 .
docker run -d --name flask-info -p 5000:5000 flask-info-app:1.0
```
