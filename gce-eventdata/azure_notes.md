
# PVC

## 1. Create a static volume
  - https://docs.microsoft.com/en-us/azure/aks/azure-disk-volume

```
az aks show --resource-group twoRavensResourceGroup --name ravensCluster02-EventData --query nodeResourceGroup -o tsv
```

- output: `MC_twoRavensResourceGroup_ravensCluster02-EventData_eastus`


## 2. Create the disk

- make disk w/ name: `eventDataDisk`

```
az disk create \
  --resource-group MC_twoRavensResourceGroup_ravensCluster02-EventData_eastus \
  --name eventDataDisk \
  --size-gb 8 \
  --query id --output tsv
```

- output: `/subscriptions/14d2f886-16d9-4a5b-87f0-7aa1c4608026/resourceGroups/MC_twoRavensResourceGroup_ravensCluster02-EventData_eastus/providers/Microsoft.Compute/disks/eventDataDisk`


## 3. Example mount

```
volumeMounts:
  - name: azure
    mountPath: /mnt/azure
volumes:
  - name: azure
    azureDisk:
      kind: Managed
      diskName: eventDataDisk
      diskURI: /subscriptions/14d2f886-16d9-4a5b-87f0-7aa1c4608026/resourceGroups/MC_twoRavensResourceGroup_ravensCluster02-EventData_eastus/providers/Microsoft.Compute/disks/eventDataDisk


```
