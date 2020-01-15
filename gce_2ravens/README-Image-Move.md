
# Push pull images

### Build R if needed

```
docker build -t tworavens/ravens-r-service:develop -f Dockerfile-flask-r .

docker push tworavens/ravens-r-service:develop

docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:comfrey
docker push tworavens/ravens-r-service:comfrey
```

### Build nginx if needed

```
#
# Build nginx
cd setup/nginx
docker build -t tworavens/ravens-nginx:develop -f Dockerfile .

docker push tworavens/ravens-nginx:develop

docker tag tworavens/ravens-nginx:develop tworavens/ravens-nginx:comfrey
docker push tworavens/ravens-nginx:comfrey
```

### Pull/Retag images from dockerhub

- reference: https://hub.docker.com/u/tworavens/

```
docker pull tworavens/ravens-main:develop
docker tag tworavens/ravens-main:develop tworavens/ravens-main:comfrey
docker push tworavens/ravens-main:comfrey

docker pull tworavens/ravens-r-service:develop
docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:comfrey
docker push tworavens/ravens-r-service:comfrey

docker pull tworavens/ravens-nginx:develop
docker tag tworavens/ravens-nginx:develop tworavens/ravens-nginx:comfrey
docker push tworavens/ravens-nginx:comfrey
```

Note: It's not advisable to build your docker images locally and push them. You may inadvertently include development/test files.

### Tag the dockerhub images for gitlab

- remove any old gitlab images from your machine

```
docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:comfrey

docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:comfrey

docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:comfrey

docker system prune
```

- Retag images...

```
docker tag tworavens/ravens-main:comfrey registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:comfrey

docker tag tworavens/ravens-r-service:comfrey registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:comfrey

docker tag tworavens/ravens-nginx:comfrey registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:comfrey
```

### Upload those images

- login
```
docker login registry.datadrivendiscovery.org
```

- push

```
docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:comfrey

docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:comfrey

docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:comfrey
```
