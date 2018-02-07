# Deployment and service files for Google Compute Engine.

## Deploy

```
cd two-ravens-deploy/gce
git pull
kubectl apply -f ravens-main-deployment.yml
kubectl apply -f ravens-main-service.yml
#
# wait for service to have IP assigned
kubectl get svc
```

- Note: The service uses a LoadBalancer with static IP as specified in `ravens-main-service.yml`

## Delete

```
kubectl delete -f ravens-main-deployment.yml
kubectl delete -f ravens-main-service.yml
```

## log example

```
kubectl logs tworavensweb-xxxxxxx ta3-main
kubectl logs tworavensweb-xxxxxxx rook-service

```

## login, etc

```
# Log into running pod
#kubectl exec -it tworavensweb-xxxxxxx -c ta3-main /bin/bash

kubectl exec -ti  tworavensweb-1872123671-2rq5p -c ta3-main /bin/bash

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
