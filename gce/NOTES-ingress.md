
# SSL-related work

Create a global IP address:


```
> gcloud compute addresses create ip-2ravens-org-global --global
> gcloud compute addresses list
NAME                             REGION       ADDRESS          STATUS
ip-2ravens-org-global                         35.244.165.103   RESERVED


> gcloud compute addresses create ip-2ravens-org-us-central1

ip-2ravens-org-us-central1       us-central1  104.197.235.238  RESERVED

```