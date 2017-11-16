

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
-
