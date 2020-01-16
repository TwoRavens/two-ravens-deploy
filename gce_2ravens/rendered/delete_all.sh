# Delete all Two Ravens pods
kubectl delete -f dm_2ravens1_2020_0116.yaml --grace-period=0 --force
kubectl delete -f dm_blue-2ravens_2020_0116.yaml --grace-period=0 --force
kubectl delete -f dm_2ravens3_2020_0116.yaml --grace-period=0 --force
kubectl delete -f dm_2ravens4_2020_0116.yaml --grace-period=0 --force
kubectl delete -f dm_2ravens5_2020_0116.yaml --grace-period=0 --force
kubectl delete -f dm_2ravens6_2020_0116.yaml --grace-period=0 --force
