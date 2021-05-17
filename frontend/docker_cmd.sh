docker stop nginx_app
docker rm nginx_app
docker build -t nginx_server .
docker run -d --name nginx_app -p 80:80 nginx_server