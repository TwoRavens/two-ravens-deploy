# apply all Two Ravens pods
kubectl delete -f gce_lime_2020_0124.yaml --grace-period=0 --force
kubectl delete -f gce_magenta_2020_0124.yaml --grace-period=0 --force
kubectl delete -f gce_olive_2020_0124.yaml --grace-period=0 --force
