docker stop pgdb_container
docker rm pgdb_container
docker build -t pgdb .
docker run -d --name pgdb_container -p 5432:5432 pgdb
docker run -d --name pgdb_container -p 5432:5432 -v postgres-volume:/var/lib/postgresql/data pgdb