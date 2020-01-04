
## test flask container

```
# build
docker build -t rprasad7/hello-python:test -f Dockerfile-python .

# run locally
docker run --rm --name hello-py -p 8080:8080 rprasad7/hello-python:test

# push
docker push rprasad7/hello-python:test
```

## k8s experiments

```
# -------------
# Pod 1
# -------------
kubectl exec -ti twopod -c twopod-python /bin/bash
echo "hey hey pod1 python" >> /output/touch1.txt

kubectl exec -ti twopod -c twopod-nginx /bin/bash

# -------------
# Pod 2
# -------------
kubectl exec -ti twopod2 -c twopod2-python /bin/bash
echo "hey hey pod2 python" >> /output/touch1.txt
cat /output/touch1.txt

wget  http://twopod-service
wget  http://twopod-service:8080

```
