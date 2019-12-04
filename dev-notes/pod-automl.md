

```
NAME                                                CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
gke-high-mem-cluster-3-default-pool-5d7611e4-1hmf   122m         0%     757Mi           0%
gke-high-mem-cluster-3-default-pool-5d7611e4-lrww   65m          0%     623Mi           0%
gke-high-mem-cluster-3-default-pool-5d7611e4-n7zj   15999m       100%   8940Mi          9%
prasad@cloudshell:~/two-ravens-deploy/gce_2ravens/rendered (raven2-186120)$ kubectl get pods
NAME                READY   STATUS    RESTARTS   AGE
tworavensweb-blue   7/7     Running   0          6m47s
prasad@cloudshell:~/two-ravens-deploy/gce_2ravens/rendered (raven2-186120)$ kubectl top pods
NAME                CPU(cores)   MEMORY(bytes)
tworavensweb-blue   15922m       5297Mi
```
