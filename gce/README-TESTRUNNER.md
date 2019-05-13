
```
cd two-ravens-deploy
git pull
cd gce

kubectl apply -f ravens-job-test-01.yml

kubectl get jobs

kubectl describe job tworavens-test-runner

kubectl logs -f tworavens-test-runner-ksctt

kubectl exec -ti  tworavens-test-runner-ksctt /bin/bash

```
