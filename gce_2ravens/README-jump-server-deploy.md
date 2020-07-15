Reference:

https://datadrivendiscovery.org/wiki/pages/viewpage.action?spaceKey=gov&title=Submission+Procedure+for+TA3

## Jump server

- Pull repository (if not already there)
```
git clone git@gitlab.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019.git

git clone https://gitlab-ci-token:[gitlab-token]@gitlab.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2019.git

```

- Update repository

```
cd summer2019/dm_test_files_2019/rendered
git pull
```

## Run/Stop

```
# Stop
kubectl delete -f ta3.yaml --grace-period=0 --force

# Run
kubectl apply -f ta3.yaml

kubectl  describe pod tworavensweb
```

### Test runner

```
/performer-toolbox/d3m_runner/d3m_runner.py --yaml-file ./ta3.yaml --mode ta2ta3 --debug
```

### Additional k8s commands

- **NOTE**: If the pod isn't starting b/c the specified IP is reserved, then:
  1. Edit `raven_deploy.yml`
  1. Comment out line 15 where the IP is specified
  1. Restart the service (delete/apply lines above)
  1. Run `kubectl get svc` to see the newly assigned IP


- Commands for checking on pods, logs, logging into running containers, etc

```
#
#
kubectl describe pod tworavensweb # check on the pod
kubectl get svc # check the svc and IP

# view logs for a specific container
kubectl logs -f tworavensweb-cyan-apricot -c ravens-nginx
kubectl logs -f tworavensweb-cyan -c mongo-2ravens
kubectl logs -f tworavensweb-cyan -c redis
kubectl logs -f tworavensweb-cyan -c ravens-postgres

kubectl logs -f tworavensweb-cyan -c ta3-main
kubectl logs -f tworavensweb-cyan -c ta2-main
kubectl logs -f tworavensweb-cyan -c celery-worker
kubectl logs -f tworavensweb-cyan -c rook-service

# log into a running container
kubectl exec -ti tworavensweb-apricot -c ravens-nginx /bin/bash
kubectl exec -ti tworavensweb-cyan -c ta3-main /bin/bash
kubectl exec -ti tworavensweb -c celery-worker /bin/bash
kubectl exec -ti tworavensweb-cyan -c ta2-container /bin/bash
kubectl exec -ti tworavensweb -c rook-service /bin/bash
```
