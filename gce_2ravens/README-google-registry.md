# GCE and Docker registries

Currently, the k8s deploy specs pull from two registries:
  - Docker hub for the TwoRavens images
  - Google's registry for the TA2.
    - This registry is used b/c of the size of the TA2 (~8 gb)


## Push the TA2 to google's registry


## Tag/Push CMU TA2

```
# tag it
docker tag registry.datadrivendiscovery.org/sheath/cmu-ta2:latest gcr.io/raven2-186120/cmu-ta2:2020-0923

# push image
docker push gcr.io/raven2-186120/cmu-ta2:2020-0923


```

---

# -- OLD --

## more general tag/push

```
# tag it

#docker tag registry.datadrivendiscovery.org/j18_ta2eval/isi_ta2:stable gcr.io/raven2-186120/test-service-t2:latest

# push image
gcloud docker -- push gcr.io/raven2-186120/test-service-t2:latest

#
docker tag [image name] gcr.io/raven2-186120/test-ta2-r3:latest
gcloud docker -- push gcr.io/raven2-186120/test-ta2-r3:latest

# another image
docker tag 60406d9ee0a3 gcr.io/raven2-186120/test-ta2-br:latest
gcloud docker -- push gcr.io/raven2-186120/test-ta2-br:latest

```


## Push the TA2 to docker hub

_not currently used_

```
# tag it
docker tag registry.datadrivendiscovery.org/j18_ta2eval/isi_ta2:stable tworavens/test-service-t2:latest

# log in
docker login [username]

# push image
docker push tworavens/test-service-t2:latest
```
