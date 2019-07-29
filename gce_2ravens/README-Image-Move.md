
# Push pull images

### Build R if needed

```
docker build -t tworavens/ravens-r-service:develop -f Dockerfile-r-service .
docker push tworavens/ravens-r-service:develop

docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:july-2019
docker push tworavens/ravens-r-service:july-2019


```

### Pull/Retag images from dockerhub

- reference: https://hub.docker.com/u/tworavens/

```
docker pull tworavens/ravens-main:develop
docker tag tworavens/ravens-main:develop tworavens/ravens-main:july-2019
docker push tworavens/ravens-main:july-2019

docker pull tworavens/ravens-r-service:develop
docker tag tworavens/ravens-r-service:develop tworavens/ravens-r-service:july-2019
docker push tworavens/ravens-r-service:july-2019

docker pull tworavens/ravens-nginx:develop
docker tag tworavens/ravens-nginx:develop tworavens/ravens-nginx:july-2019
docker push tworavens/ravens-nginx:july-2019
```

Note: It's not advisable to build your docker images locally and push them. You may inadvertently include development/test files.

### Tag the dockerhub images for gitlab

- remove any old gitlab images from your machine

```
docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:july-2019

docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:july-2019

docker rmi registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:july-2019

docker system prune
```

- Retag images...

```
docker tag tworavens/ravens-main:july-2019 registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:july-2019

docker tag tworavens/ravens-r-service:july-2019 registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:july-2019

docker tag tworavens/ravens-nginx:july-2019 registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:july-2019
```

### Upload those images

- login
```
docker login registry.datadrivendiscovery.org
```

- push

```
docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-main:july-2019

docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-r-service:july-2019

docker push registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019/ravens-nginx:july-2019
```
