# apply all Two Ravens pods
kubectl delete -f gce_blue_2020_0129.yaml --grace-period=0 --force
kubectl delete -f gce_lime_2020_0129.yaml --grace-period=0 --force
kubectl delete -f gce_olive_2020_0129.yaml --grace-period=0 --force
