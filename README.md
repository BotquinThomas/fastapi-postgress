# fast-api
Fast-api &amp; postgresql with docker

### How to run this project:

1) clone project and cd into it
```
git clone https://github.com/BotquinThomas/fast-api-postgress.git
```

2) run docker container in background from /path-to/docker-compose.yml
```
docker-compose up -d 
```

3) navigate to [http://localhost:80](http://localhost:80) (on your browser)


4) if you want to have to look inside the container (postgres or fast-api)
```
# postgres container
docker container exec -it postgres bin/bash
psql -U username -d database -c 'SELECT * FROM items'
```
```
# fast-api container
docker container exec -it fast-api bash
```

5) once done, stop the containers and remove the volumes (-v) if necessary
```
docker-compose down -v
```
