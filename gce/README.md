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
