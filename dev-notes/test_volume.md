
## From cloud Shell

```
# get pod name
kubectl get pods

# log into container using pod name
# - in ex
kubectl exec -it {pod name} --container=ta3-main bash
# example:
# pod name: ravens-main-1301003386-k6crm
# command: kubectl exec -it ravens-main-1301003386-k6crm --container=ta3-main bash
```

## Copy actual data to /ravens_volume

```
cd /ravens_volume
cp -R /var/webapps/TwoRavens/ravens_volume/* .
```

### Go back and refresh browser
