# apply all Two Ravens pods
kubectl delete -f gce_mint_2020_0129.yaml --grace-period=0 --force
kubectl delete -f gce_navy_2020_0129.yaml --grace-period=0 --force
kubectl delete -f gce_red_2020_0129.yaml --grace-period=0 --force
