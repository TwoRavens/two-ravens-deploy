# Google Compute Engine deployment notes

## Deploy

These commands assume you have logged onto the GCE shell.

```
# one time: download the deploy repo:
#
git clone https://github.com/TwoRavens/two-ravens-deploy.git  

# Go to the correct directory and update it
#
cd two-ravens-deploy/gce_2ravens/rendered
git pull

# For any file in the directory 'two-ravens-deploy/gce_2ravens/rendered'
#   (example: using file "ta3.yaml")

# start the system
#
kubectl apply -f ta3.yaml


# Check progress
#
kubectl get pods
kubectl describe pod/tworavensweb


# Stop/delete the system
#
kubectl delete -f ta3.yaml --grace-period=0 --force

# to shutdown gracefully, takes a minute or so
#
kubectl delete -f ta3.yaml

```


## Create a k8s file (Locally)

These instructions describe how to create an updated k8s file.
This should be run locally, then update the repository on GCE via `git pull`

1. First time, clone the repository and create a virtualenv
    ```
    git clone https://github.com/TwoRavens/two-ravens-deploy.git  
    cd two-ravens-deploy

    # virtualenv
    #
    mkvirtualenv raven-deploy
    pip install -r requirements/base.txt
    ```
2. Update the template and/or config information.  Relevant files:

    - `config_specs.py` - Add a new python dictionary entry with any relevant variable changes.  Note, the variables include:
      - `template_name` - Name of K8s template file in the directory `gce_2ravens/templates`
      - `rendered_filename` - Name of rendered template, written to directory `gce_2ravens/rendered`

3. Run the script to make a template
    ```
    cd two-ravens-deploy/gce_2ravens
    python create_config.py  # this will give the user a list of choices

    # Output messages should indicate that files have been created.
    ```

4. Check-in the repository changes, e.g. the new templates and/or new data in `config_specs.py`

5. On the GCE console, pull in the relevant changes and use the new templates


## View container-specific logs

```
# View logs
# Use "-f" to tail the log
#

# Front-facing nginx webserver
#
kubectl logs -f tworavensweb ravens-nginx

# The TA3!
#
kubectl logs -f tworavensweb ta3-main
kubectl logs -f tworavensweb celery-worker
kubectl logs -f tworavensweb rook-service

# The TA2!
#
kubectl logs -f tworavensweb ta2-main


# Redis + Mongo
#
kubectl logs -f tworavensweb redis
kubectl logs -f tworavensweb mongo-2ravens

```

## Log into a running container

```
# Front-facing nginx webserver
#
kubectl exec -ti  tworavensweb -c ravens-nginx /bin/bash

# The TA3!
#
kubectl exec -it tworavensweb -c ta3-main /bin/bash
kubectl exec -ti  tworavensweb -c celery-worker  /bin/bash
kubectl exec -ti  tworavensweb -c rook-service /bin/bash

# The TA2!
#
kubectl exec -ti  tworavensweb -c ta2-main /bin/bash

# Redis + Mongo
#
kubectl exec -ti  tworavensweb -c redis /bin/bash
kubectl exec -ti  tworavensweb -c mongo-2ravens /bin/bash

```

## downsize cluster

- Set size to zero

```
gcloud container clusters resize cluster-1 --size=0 --zone=us-central1-a
```

## get cluster going again

- Set size back (to 12 in this example)

```
gcloud container clusters resize cluster-1 --size=12 --zone=us-central1-a
```
