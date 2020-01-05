
# Push pull images

### Build R if needed

```
# docker build -t tworavens/ravens-r-service:develop -f Dockerfile-r-service .
docker build -t tworavens/ravens-r-service:develop -f Dockerfile-flask-r .

docker push tworavens/ravens-r-service:develop

docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:jan-2020-01
docker push tworavens/ravens-r-service:jan-2020-01
```

### Build nginx if needed

```
#
# Build nginx
cd setup/nginx
docker build -t tworavens/ravens-nginx:develop -f Dockerfile .

docker push tworavens/ravens-nginx:develop

docker tag tworavens/ravens-nginx:develop tworavens/ravens-nginx:jan-2020-01
docker push tworavens/ravens-nginx:jan-2020-01


# docker build -t tworavens/ravens-r-service:develop -f Dockerfile-r-service .
cd setup/nginx
docker build -t tworavens/ravens-r-service:develop -f Dockerfile-flask-r .

docker push tworavens/ravens-r-service:develop

docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:jan-2020-01
docker push tworavens/ravens-r-service:jan-2020-01
```

### Pull/Retag images from dockerhub

- reference: https://hub.docker.com/u/tworavens/

```
docker pull tworavens/ravens-main:develop
docker tag tworavens/ravens-main:develop tworavens/ravens-main:jan-2020-01
docker push tworavens/ravens-main:jan-2020-01

docker pull tworavens/ravens-r-service:develop
docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:jan-2020-01
docker push tworavens/ravens-r-service:jan-2020-01

docker pull tworavens/ravens-nginx:develop
docker tag tworavens/ravens-nginx:develop tworavens/ravens-nginx:jan-2020-01
docker push tworavens/ravens-nginx:jan-2020-01
```

Note: It's not advisable to build your docker images locally and push them. You may inadvertently include development/test files.

### Tag the dockerhub images for gitlab

- remove any old gitlab images from your machine

```
docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:jan-2020-01

docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:jan-2020-01

docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:jan-2020-01

docker system prune
```

- Retag images...

```
docker tag tworavens/ravens-main:jan-2020-01 registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:jan-2020-01

docker tag tworavens/ravens-r-service:jan-2020-01 registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:jan-2020-01

docker tag tworavens/ravens-nginx:jan-2020-01 registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:jan-2020-01
```

### Upload those images

- login
```
docker login registry.datadrivendiscovery.org
```

- push

```
docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:jan-2020-01

docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:jan-2020-01

docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:jan-2020-01
```
