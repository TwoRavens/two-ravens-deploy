## Deploying on Google Compute engine

This is currently a naive setup--e.g. no external db, env variables, etc.


### Create a cluster

1. Go to: https://console.cloud.google.com/kubernetes/list
2. Click "Create Cluster"
   - Initially used zone `us-central1-a`
3. Active the "Google Shell Shell", click icon in the top right ">_"
4. From the UI above, click "connect to cluster" and copy first line into the shell.
  - Sample line: `gcloud container clusters get-credentials raven1 --zone us-east1-b --project raven2-186120`

### Setup instructions

- References:
    - https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app
    - https://cloud.google.com/kubernetes-engine/docs/tutorials/guestbook

1. Clone app:
    ```
    git clone https://github.com/TwoRavens/two-ravens-deploy.git
    cd two-ravens-deploy
    export PROJECT_ID="$(gcloud config get-value project -q)"
    ```
2. Deploy & Run
    ```
    kubectl create -f ravens-main-deployment.yml
    kubectl expose deployment ravens-main --type=LoadBalancer --port 80 --target-port 8080
    ```
3. Show services
    ```
    kubectl get svc -o wide
    ```
  - Initially, the EXTERNAL-IP for *ravens-main* will say `<pending>`
  - Repeat the show services command until an IP appears--and try that IP in the browser

### Various commands

```
# ----------
# view
# ----------
# pods
kubectl get pods --all-namespaces -o wide
# services
kubectl get svc -o wide
# deployments
kubectl get deploy

# ----------
# Logs
# ----------

# container specific logs
kubectl logs raven1 ta3-main

# ----------
# delete
# ----------
# service
kubectl delete svc ravens-main
# deploy as defined in file
kubectl delete -f ravens-main-deployment.yml

```
