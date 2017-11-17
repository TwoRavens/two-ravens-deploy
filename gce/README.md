## Deployment and service files for Google Compute Engine.

```
kubectl apply -f ravens-main-deployment.yml
kubectl apply -f ravens-main-service.yml
#
# wait for service to have IP assigned
kubectl get svc
```

- Note: The service uses a LoadBalancer with static IP 104.197.235.238
