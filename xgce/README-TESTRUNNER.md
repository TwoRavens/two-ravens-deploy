
```
cd two-ravens-deploy
git pull
cd gce

kubectl apply -f ravens-job-test-01.yml

kubectl delete -f ravens-job-test-01.yml

kubectl get jobs

kubectl describe job tworavens-test-runner

kubectl get pods

kubectl logs -f tworavens-test-runner-ksctt

kubectl exec -ti  tworavens-test-runner-ksctt /bin/bash


pname=$(kubectl get pods --selector=tworavens-test-runner --output=jsonpath='{.items[*].metadata.name}')
echo $pname
```
