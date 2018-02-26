# Build Images

```invoke minikube docker env
eval $(minikube docker-env)
```

```
# Build main app + R service
#
docker build -t tworavens/ravens-main:latest .
docker build -t tworavens/ravens-r-service:latest -f Dockerfile-r-service .

#
# Build nginx
cd setup/nginx
docker build -t tworavens/ravens-nginx:latest -f Dockerfile .
```

```minikube
kubectl apply -f mktest-main-service.yml --validate=false
kubectl get pods
kubectl exec
kubectl port-forward [pod_name] 8080:8080

# bin/bash
kubectl exec -it [pod_name] -c ta3-main -- /bin/bash

```


## remove docker images

```
docker rmi docker rmi $(docker images -f "dangling=true" -q)
```
