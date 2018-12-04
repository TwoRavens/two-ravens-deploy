# Deployment and service files for Google Compute Engine.

## Deploy

```
cd two-ravens-deploy/gce
git pull

# add config variables
kubectl apply -f ravens-d3m-configmap.yml
kubectl apply -f ravens-django-configmap.yml
kubectl apply -f ravens-with-svc3.yml


# Wait for service to have IP assigned
#
kubectl get svc

# Check progress
# Note: It takes a while to pull the "Real TA2" container which is ~8gb
#
kubectl get pods
kubectl describe pod/tworavensweb
```

- Note: The service uses a LoadBalancer with static IP as specified in `ravens-main-service.yml`

## Delete

```
kubectl delete -f ravens-with-svc3.yml

# immediate shutdown
kubectl delete -f ravens-with-svc3.yml --grace-period=0 --force


#kubectl delete -f ravens-deploy.yml # NO TA2
#kubectl delete -f ravens-deploy-with-ta2.yml  # Real TA2
#kubectl delete -f ravens-main-service.yml
```

## log example

```
# View logs
# Use "-f" to tail the log
#
kubectl logs tworavensweb ravens-nginx

kubectl logs tworavensweb ta3-main
kubectl logs tworavensweb rook-service

kubectl logs tworavensweb celery-worker
kubectl logs tworavensweb redis

kubectl logs tworavensweb ta2-main


```

## login, etc

```
# Log into running pod
#
kubectl exec -ti  tworavensweb -c ravens-nginx /bin/bash

kubectl exec -it tworavensweb -c ta3-main /bin/bash
kubectl exec -ti  tworavensweb -c rook-service /bin/bash

kubectl exec -ti  tworavensweb -c celery-worker  /bin/bash
kubectl exec -ti  tworavensweb -c redis /bin/bash

kubectl exec -ti  tworavensweb -c ta2-main /bin/bash



# Make some test configs...
fab make_d3m_config_files

# Copy test data to the shared volume
cp -r ravens_volume/. /ravens_volume

# describe containers in pod
kubectl describe pod/ravens-ta3

# run ta3_search
kubectl exec -ti tworavensweb-2390003843-wrlf9 --container ta3-main -- ta3_search /ravens_volume/config_185_baseball.json

```

## downsize cluster

- Set size to zero

```
gcloud container clusters resize cluster-1 --size=0 --zone=us-central1-a
```

## get cluster going again

- Set size back to 3 (or 2)

```
gcloud container clusters resize cluster-1 --size=2 --zone=us-central1-a
```
