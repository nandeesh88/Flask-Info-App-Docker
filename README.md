# Flask-Info-App-Docker 🚀

A Dockerized Flask web app with HTML pages and a JSON API. Demonstrates Python web development and containerization with Docker.

## Features
- **Homepage (`/`)** – Welcome page  
- **About (`/about`)** – Project info  
- **API (`/api/info`)** – JSON endpoint  
- Fully **Dockerized** for easy deployment

## Tech
Python 3.11 | Flask | Docker

## How to Run
1. Build: `docker build -t flask-info-app:1.0 .`  
2. Run: `docker run -d --name flask-info -p 5000:5000 flask-info-app:1.0`  
3. Open: `http://localhost:5000` (homepage)  
   `/about` → About page  
   `/api/info` → JSON API
