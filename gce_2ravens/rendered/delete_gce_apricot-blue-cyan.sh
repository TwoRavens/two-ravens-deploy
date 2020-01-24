# apply all Two Ravens pods
kubectl delete -f gce_apricot_2020_0124.yaml --grace-period=0 --force
kubectl delete -f gce_blue_2020_0124.yaml --grace-period=0 --force
kubectl delete -f gce_cyan_2020_0124.yaml --grace-period=0 --force
