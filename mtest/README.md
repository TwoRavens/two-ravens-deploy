
Bad example with a key added to the image but just to test the idea

```
docker build -t shuttle -f Dockerfile-sshuttle .
sudo docker run --name mongo-connect --rm --privileged -p 27017:27017 shuttle
```

Output

```
sudo docker run --privileged shuttle
Password:
Warning: Permanently added '178.xxx.xxx.xxx' (ECDSA) to the list of known hosts.
client: Connected.
```