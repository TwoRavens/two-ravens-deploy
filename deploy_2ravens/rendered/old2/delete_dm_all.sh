# Delete all Two Ravens pods
kubectl delete -f dm_red-2ravens_2020_0126.yaml --grace-period=0 --force
kubectl delete -f dm_blue-2ravens_2020_0126.yaml --grace-period=0 --force
kubectl delete -f dm_lime-2ravens_2020_0126.yaml --grace-period=0 --force
kubectl delete -f dm_maroon-2ravens_2020_0126.yaml --grace-period=0 --force
kubectl delete -f dm_white-2ravens_2020_0126.yaml --grace-period=0 --force
kubectl delete -f dm_orange-2ravens_2020_0126.yaml --grace-period=0 --force
