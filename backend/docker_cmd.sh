docker stop api_app
docker rm api_app
docker build -t fastapi .
docker run -d --name api_app -p 8000:80 fastapi