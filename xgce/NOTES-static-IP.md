
# IP assignment

### 1. Create an address by command line

```
gcloud compute addresses create ip-2ravens-org-us-central1

NAME  ADDRESS/RANGE    TYPE      PURPOSE  NETWORK  REGION SUBNET STATUS
ip-2ravens-org-us-central1  104.197.235.238  EXTERNAL us-central1       IN_USE
```

### 2. Google domains: 2ravens.org

Assign the @ and www records to 2ravens.org

1. Add A Record for '@':

Entries:  
  - Name: @
  - Type: A
  - TTL: 1H
  - Data: 104.197.235.238


2. Add A Record for 'www':

Entries:  
  - Name: www
  - Type: A
  - TTL: 1H
  - Data: 104.197.235.238

### 3. k8s file,

- Use IP "104.197.235.238" for *loadBalancerIP*

```
spec:
  type: LoadBalancer
  loadBalancerIP: 104.197.235.238  # 2ravens.org
```


# SSL-related work

Create a global IP address:


```
> gcloud compute addresses create ip-2ravens-org-global --global
> gcloud compute addresses list
NAME                             REGION       ADDRESS          STATUS
ip-2ravens-org-global                         35.244.165.103   RESERVED

```
