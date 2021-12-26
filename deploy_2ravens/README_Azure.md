# Azure deployment notes

## Azure Setup/Deploy

These commands assume you have logged onto the Azure shell and connected to your cluster.

1. **Add a kubectl alias**
```
vim .bashrc
# add this line to the end of the .bashrc file:
alias kc="kubectl"
source .bashrc
```

2. **Upload the secrets file**
```
# From the Azure shell 

# (a) Go to the home directory
cd ~ 

# (b) make a directory to hold the k8s secret config files 
mkdir k8s-secrets 

# (c) Use the Azure Terminal's "file transfer" menu button to upload the secrets file
# file name: azure-tworavens-web-secrets.yaml
# This will upload the file to the home directory

# (d) Move and apply the secrets file
#    The 2nd command should result in: "secret/tworavens-web-secrets configured"
mv azure-tworavens-web-secrets.yaml k8s-secrets/
kc apply -f k8s-secrets/azure-tworavens-web-secrets.yaml

# (e) Verify that the secrets exist
kc get secret tworavens-web-secrets -o yaml
```

3. **Clone the TwoRavens/two-ravens-deploy repository**
```
# one time: download the deploy repo:
#
git clone https://github.com/TwoRavens/two-ravens-deploy.git

# Go to the correct directory and update it
#
cd two-ravens-deploy/
git pull

```

4. **Run one of the configs**

```
# Assumes you are in the Azure shell
cd ~/two-ravens-deploy/deploy_2ravens/rendered/

# list files. At time of writing, includes "azure_testing_2021_0603.yaml"
#
ls  

# Start up a pod containing the TwoRavens system
#
kc apply -f azure_testing_2021_0603.yaml
```
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
      - `template_name` - Name of K8s template file in the directory `deploy_2ravens/templates`
      - `rendered_filename` - Name of rendered template, written to directory `deploy_2ravens/rendered`

3. Run the script to make a template
    ```
    cd two-ravens-deploy/deploy_2ravens
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
kubectl logs -f ravenpod-demo ravens-nginx

# The TA3!
#
kubectl logs -f ravenpod-demo ta3-main
kubectl logs -f ravenpod-demo ravens-nginx
kubectl logs -f ravenpod-demo celery-worker
kubectl logs -f ravenpod-demo rook-service

# The TA2!
#
kubectl logs -f ravenpod-demo ta2-container


# Redis + Mongo
#
kubectl logs -f ravenpod-demo redis
kubectl logs -f ravenpod-demo mongo-2ravens

```

## Log into a running container

```
# Front-facing nginx webserver
#
kubectl exec -ti  ravenpod-demo -c ravens-nginx /bin/bash

# The TA3!
#
kubectl exec -ti  ravenpod-demo -c ta3-main /bin/bash
kubectl exec -ti  ravenpod-demo -c celery-worker  /bin/bash
kubectl exec -ti  ravenpod-demo -c rook-service /bin/bash

# The TA2!
#
kubectl exec -ti  ravenpod-demo -c ta2-container /bin/bash

# Redis + Mongo
#
kubectl exec -ti  ravenpod-demo -c redis /bin/bash
kubectl exec -ti  ravenpod-demo -c mongo-2ravens /bin/bash

```

## Delete user files on persistent volume

```
# Example deleting apricot data

# Login into redis which has access to volumes for all instances
#
kubectl exec -ti  tworavensweb-testing -c redis /bin/
bash

# Example of deleting apricot data
#
rm -rf /ravens_volume/2ravens_org-testing/TwoRavens_user_datasets/*
rm -rf /ravens_volume/2ravens_org-testing/evtdata_user_datasets/*
rm -rf /ravens_volume/2ravens_org-testing/test_output/*

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
