

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

- Initial command using gcloud SDK:
  ```
  gcloud compute disks create --size=500GB --zone=us-central1-a raven-disk-01
  ```

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
