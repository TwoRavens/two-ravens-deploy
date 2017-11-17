

### Mac install gcloud SDK

- Install instructions
  - https://cloud.google.com/sdk/docs/quickstart-mac-os-x

1. Downloaded and moved to user library
  - e.g. ~/Library/google-cloud-sdk/bin
  - update `.bash_profile` with:
    - `export PATH=/Users/{username}/Library/google-cloud-sdk/bin:$PATH`
1. Followed instructions via Terminal commands
  - selected zone: `us-central1-a`
1. From the output:
  ```
  * Commands will reference project `raven2-186120` by default
  * Compute Engine commands will use REGION `us-central1` by default
  * Compute Engine commands will use ZONE `us-central1-a` by default
  ```



## Create a CGE persisent disk

- References:
  - step-by-step: https://cloud.google.com/compute/docs/disks/add-persistent-disk
    - formatting: https://cloud.google.com/compute/docs/disks/add-persistent-disk#formatting
  - general info: https://kubernetes.io/docs/concepts/storage/volumes/#gcepersistentdisk

- Initial command using gcloud SDK

1. Create disk via gcloud
    ```
    gcloud compute disks create --size 200GB raven-disk-dev
    ```
1. List instances running the cluster
    ```
    gcloud compute instances list
    ```
    - Example output:
        ```
        NAME                                      ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP     STATUS
      gke-cluster-1-default-pool-e584caed-34pq  us-central1-a  n1-standard-1               10.128.0.3   35.192.182.137  RUNNING
      gke-cluster-1-default-pool-e584caed-7j5c  us-central1-a  n1-standard-1               10.128.0.2   35.202.102.80   RUNNING
      gke-cluster-1-default-pool-e584caed-c6ls  us-central1-a  n1-standard-1               10.128.0.4   104.197.19.140  RUNNING
      ```
1. Attach the disk to one of the instances
    ```
    # example
    gcloud compute instances attach-disk gke-cluster-1-default-pool-e584caed-34pq --disk raven-disk-dev
    ```
1. Use the console to SSH into the instance
  - https://console.cloud.google.com/compute/instances
1. Run the format commands
    ```
    # list attached disks
    lsblk
    # format disk
    sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_ini
t=0,discard /dev/sdb
1. Now detach the disk--don't really want it on this instance
    ```
    # example
    gcloud compute instances detach-disk gke-cluster-1-default-pool-e584caed-34pq --disk raven-disk-dev
    ```
1. Add the disk mount to the deploy file

### Format disk

(do this an easier way next time)

- Run the cluster
- Connect to the container with attached disk
  - e.g. `kubectl exec -it ravens-main-3834649790-lwb4v --container=ta3-main bash`
- Once in the container:
    ```
    # list the disks
    lsblk
    # find the DEVICE ID, e.g. `sdb`
    # run this command substituting the actual DEVICE ID:
    #   sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/[DEVICE_ID]
    #
    #
    mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
