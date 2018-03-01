
## push ta2 to docker hub

```
# tag it
docker tag registry.datadrivendiscovery.org/j18_ta2eval/isi_ta2:stable tworavens/test-service-t2:latest

# log in
docker login rprasad7

# push image
docker push tworavens/test-service-t2:latest
```


## push ta2 to gce repository

```
# tag it
docker tag registry.datadrivendiscovery.org/j18_ta2eval/isi_ta2:stable gcr.io/raven2-186120/test-service-t2:latest

# push image
gcloud docker -- push gcr.io/raven2-186120/test-service-t2:latest
```
