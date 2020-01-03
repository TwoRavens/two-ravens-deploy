
```
docker run -it --rm --name py-test python:3.7 /bin/bash
docker run -it --rm -p 8070:8070 nginx --name py-test python:3.7 /bin/bash

docker run -it --rm --name nginx-test -p 80:8080 nginx /bin/bash

docker run --rm --name nginxest -p 8070:80 nginx
```
