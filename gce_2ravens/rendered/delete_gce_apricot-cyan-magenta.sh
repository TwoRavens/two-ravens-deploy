# apply all Two Ravens pods
kubectl delete -f gce_apricot_2020_0221.yaml --grace-period=0 --force
kubectl delete -f gce_cyan_2020_0221.yaml --grace-period=0 --force
kubectl delete -f gce_magenta_2020_0221.yaml --grace-period=0 --force
