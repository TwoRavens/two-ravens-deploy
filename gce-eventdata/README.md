# Deployment and service files for Google Compute Engine.

## Deploy

```
cd two-ravens-deploy/gce-eventdata
git pull

# Create deployment
#
kubectl apply -f eventdata-deploy.yml

# Run service:
#
kubectl apply -f eventdata-service.yml


# Wait for service to have IP assigned
#
kubectl get svc

# Check progress
#
kubectl get pods
kubectl describe pod/[pod name from previous command]
```

# -------------------
# local run
# -------------------
sudo kubectl port-forward ravens-eventdata-web-833262626-v1mgs 80:80


## Delete

```
kubectl delete -f eventdata-deploy.yml
kubectl delete -f eventdata-service.yml
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
