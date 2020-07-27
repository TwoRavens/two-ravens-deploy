# Summer 2020

Submission for dry run.

This directory contains a `ta3.yaml` kubernetes (k8s) configuration file which has been tested on the DM infrastructure through this url:

  - https://2ravens-summer.datadrivendiscovery.org
      - Internal IP: 10.108.34.30:8080

The container registry used by the TA3 within the k8s configuration file is:

  - https://gitlab.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2020evaluation/container_registry

## Dockerfiles

The TA3 Dockerfiles used to create the images pulled by the `ta3.yaml` file may be seen here:

1. **Image**: registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2020evaluation/ravens-main:july-2020
    - **Dockerfile**: https://github.com/TwoRavens/TwoRavens/blob/develop/Dockerfile
2. **Image**: registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2020evaluation/ravens-r-service:july-2020
    - **Dockerfile**: https://github.com/TwoRavens/TwoRavens/blob/develop/Dockerfile-r-service
3. **Image**:  registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2020evaluation/ravens-nginx:july-2020
    - **Dockerfile**: https://github.com/TwoRavens/TwoRavens/blob/develop/setup/nginx/Dockerfile

---
