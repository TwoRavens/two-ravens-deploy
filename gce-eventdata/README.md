# Deploying EventData on Google Compute Engine (gce)

These steps deploy the TwoRavens EventData application using Docker images from https://hub.docker.com/r/tworavens/

- **Prerequisite**: admin permissions on the gce kubernetes cluster running event data

## (1) Steps to Build Docker Images

1. In your dev environment, run `fab webpack_prod` + `fab run` to build the latest code into a webpack distribution.
     - Check in any new js/css dist files, if needed
1. Checking in new code to the `EventData_generalization` branch, creates 2 new Docker Images:
    1. Main Two Ravens: https://hub.docker.com/r/tworavens/eventdata-ravens-main/tags/
        - The image is created after a successful Travis build: https://travis-ci.org/TwoRavens/TwoRavens/builds
    1. nginx: [tworavens/eventdata-ravens-nginx/tags](https://hub.docker.com/r/tworavens/eventdata-ravens-nginx/tags/)
        - main nginx dockerhub page: tworavens/eventdata-ravens-nginx](https://hub.docker.com/r/tworavens/eventdata-ravens-nginx/)
1. Check that the 2 required images have been recently built:
    - [tworavens/eventdata-ravens-main/tags](https://hub.docker.com/r/tworavens/eventdata-ravens-main/tags/)
    - [tworavens/eventdata-ravens-nginx/tags](https://hub.docker.com/r/tworavens/eventdata-ravens-nginx/tags/)


## (2) GCE Deploy - Shortcuts (if you've done it before)

1. Go to the cluster list and "connect" to a Terminal
    - https://console.cloud.google.com/kubernetes/list

```
# One-time secret
#
kubectl apply -f k8s-secret-configs/gce-eventdata-secrets.yaml

# (a) pull the latest config code
#
cd two-ravens-deploy/gce-eventdata
git pull # only changes when these instructions/config files change

# (b) apply configmap - This only needs be done if the configmap has changed.
#
kubectl apply -f eventdata-django-configmap.yaml

# (c) Restart the pod + svc
#
kubectl apply -f eventdata-pod-with-svc.yaml

# Send the stop command
#  - This takes about a minute.
#
kubectl delete -f eventdata-pod-with-svc.yaml  # stop the current pod/svc

# Check to make sure the pod is stopped
#  - If the STATUS is "Terminating", keep waiting
#
kubectl get pods   # when the pod stops, you will no longer see "eventdata-web" in the list

# Start the pod + svc
#  - This also takes about a minute
#
kubectl apply -f eventdata-pod-with-svc.yaml  # start the current pod/svc

# Check the status
#   - This can give you an idea of the state, whether containers are being pulled, etc
#
kubectl describe pod eventdata-web

#   Note: It's ok to see the message below--I have to adjust some of the startup timings for the 1st check:
#
#    "Warning  Unhealthy              1m    kubelet, gke-cluster-1-default-pool-e584caed-v4rq  Liveness probe failed: (etc)"


# Alternative Stop: stops the pod + svc immediately
#
kubectl delete -f eventdata-pod-with-svc.yaml --grace-period=0 --force

# ---------------
# other
# ---------------

# list pods, the name of the eventdata pod is "eventdata-web"
#
kubectl get pods

# describe pod using name from "kubectl get pods"
#   - will tell if there are errors starting containers
#
kubectl describe pod eventdata-web

# See a log for a container, e.g. what you see in the rook Terminal when running locally
#   - `kubectl logs -f .....` will stream the log
#
kubectl logs -f eventdata-web ta3-main  # python server log
kubectl logs -f eventdata-web ravens-nginx  # nginx log
kubectl logs -f eventdata-web raven-postgres  # mysql log

# Log into a running container with full admin rights
#   - e.g. look around, see if files are being created, stop/start things, etc
#
kubectl exec -it eventdata-web -c ta3-main -- /bin/bash
kubectl exec -it eventdata-web -c ravens-nginx -- /bin/bash
kubectl exec -it eventdata-web -c raven-postgres  -- /bin/bash

```

## (2) GCE Deploy - Longer explanation

### This part is a bit outdated

## Open a Terminal within a browser (Chrome)

1. Go to the cluster list:
    - https://console.cloud.google.com/kubernetes/list
    - `cluster-1` should appear as a row in the main part of the page
1. Click "connect" which opens a shell in the browser
1. Click "Run in Cloud Shell"
    - A Terminal window opens in the browser
1. Press the "return" key to execute the auto-added line.  Usually something like this:
    - `gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project raven2-186120`

## Create the eventdata Pod and Service

- Run these steps from the Terminal (previous step).  These steps pull the appropriate Docker images (nginx, python server, rook server) from Docker hub

```
cd two-ravens-deploy/gce-eventdata
git pull  # get the latest k8s config info

# Stop any running deployments
#   - if nothing was running, you'll see "Error from server (NotFound):..."
#     - that's fine
#
kubectl delete -f eventdata-pod-with-svc.yaml

# Note: check `kubectl get pods` to make sure the pod
# is deleted before restarting.  This can take a minute

# Create a new pod + svc
#   - should see a message like: deployment "eventdata-web" created
#   - The website can take a couple of minutes to start
#
kubectl apply -f eventdata-pod-with-svc.yaml


# Wait for service to have IP assigned
#
kubectl get svc

# Check progress
#
kubectl get pods
kubectl describe pod eventdata-web
```

## Stop the Pod + Svc (again)

- Open the gce Terminal from a browser (see steps above)

```
cd two-ravens-deploy/gce-eventdata

kubectl delete -f eventdata-pod-with-svc.yaml

```

---

## Misc notes

### local run

```
sudo kubectl port-forward eventdata-web-833262626-v1mgs 80:80
```

### downsize cluster

- Set size to zero

```
gcloud container clusters resize cluster-1 --size=0 --zone=us-central1-a
```

### get cluster going again

- Set size back to 3 (or 2)

```
gcloud container clusters resize cluster-1 --size=2 --zone=us-central1-a
```
