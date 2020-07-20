"""
# Starting with new base spec on 7/14/2020

Used by create_config for k8s template settings

IMPORTANT: When adding a new dict, make sure the name has 'spec' or 'SPEC' in it.
    examples: 'K8S_SPEC_001', 'taxi_spec_nyu', 'spec_poverty_mit'
"""

base_spec_01 = dict(\
    #
    template_name="gce_ravens_deploy_027-twopod.yaml",
    rendered_filename="gce_2ravens_2020_0714.yaml",   # overwritten for multi configs
    #
    # Volume mount and resource templates
    #
    VOLUME_MOUNTS_TEMPLATE_FILENAME="dm_volume_mounts_01.yaml",
    RESOURCES_TEMPLATE_FILENAME="resources_01.yaml",
    #
    #
    # server and cookies
    #
    RAVENS_SERVER_NAME="2ravens.org",
    SESSION_COOKIE_NAME="ravens_base",
    CSRF_COOKIE_NAME="ravens_base_csrf",
    #
    # NGINX
    #
    NGINX_MAX_UPLOAD_SIZE="28m",
    NGINX_SERVER_NAME=".2ravens.org",
    #
    # load balancer, changes with mutli config
    loadBalancerIP="104.197.235.238  # 2ravens.org",
    #
    # docker registry. e.g. 'tworavens' is on DockerHub
    #
    tworavens_registry="tworavens",
    # tag used for ravens_main, rook, and nginx
    tworavens_container_tag="comfrey-2020-0719",
    #
    #   TA2
    #
    ta2_image="dmartinez05/tamuta2:latest",
    ta2_image_comment="TAMU TA2!",
    #
    # pull policies
    pull_policy_ta2="IfNotPresent",
    pull_policy_ravens_main="Always",
    pull_policy_rook="Always",
    pull_policy_nginx="Always",
    #
    # web port
    externalPort=80,
    #
    # D3M variables
    #
    D3MRUN="ta2ta3",
    D3MINPUTDIR="/ravens_volume/test_data",
    D3MPROBLEMPATH="/ravens_volume/test_data/185_baseball/TRAIN/problem_TRAIN/problemDoc.json",
    D3MOUTPUTDIR="/ravens_volume/test_output",
    D3MLOCALDIR="/ravens_volume/test_output/local_dir",
    D3MSTATICDIR="/ravens_volume/test_output/static_dir",
    D3MCPU="1",
    D3MRAM="512Mi",
    D3MTIMEOUT="10",
    #
    # Variable for temp systems
    #
    SECRET_KEY_VALUE="f!@0^(7v_!45#c4t#!xjk433&x1y2vzo)u@v6s9pc&+gqz3s2&",
    #
    # Datamart Urls
    #
    DATAMART_URL_NYU="https://auctus.vida-nyu.org",
    DATAMART_URL_ISI="https://dsbox02.isi.edu:9000",
    #
    serviceNameSuffix="",
    #
    # CPU/Memory Resources by Container
    #
    ta2_resources=['20000Mi', '25000Mi', '2000m', '4000m'],
    ta3_resources=['1000Mi', '3000Mi', '1000m', '1500m'],
    celery_resources=['4500Mi', '6000Mi', '2000m', '2000m'],
    rook_resources=['1000Mi', '2000Mi', '500m', '1000m'],
    mongo_resources=['1000Mi', '2000Mi', '500m', '1000m'],
    redis_resources=['500Mi', '1000Mi', '500m', '500m'],
    nginx_resources=['256Mi', '500Mi', '500m', '500m'],
    postgres_resources=['1000Mi', '2000Mi', '500m', '1000m'],
    #
    # Wrapped solver settings
    #
    TA2_D3M_SOLVER_ENABLED="True",
    TA2_WRAPPED_SOLVERS=["two-ravens", "tpot"],
)

dm_summer_2020_0717 = dict(base_spec_01, **dict(\
    template_name="dm_state_one_pod_04.yaml",
    #
    externalPort=8080,  # D3M proxy tool maps to 8080 on pod
    #
    loadBalancerIP="10.108.34.30",  # 2ravens.org",
    #
    RESOURCES_TEMPLATE_FILENAME='resources_dm_01.yaml',
    RAVENS_SERVER_NAME='datadrivendiscovery.org',
    #
    NGINX_SERVER_NAME=".datadrivendiscovery.org",
    #
    #   TA2
    #
    ta2_image="dmartinez05/tamuta2:latest",
    ta2_image_comment="TAMU TA2!",
    #ta2_image="registry.datadrivendiscovery.org/sheath/cmu-ta:latest",
    #ta2_image_comment="CMU TA2!",
    ))

"""
from collections import OrderedDict
from config_specs import spec_gce_ireland_2020_0424

od = OrderedDict(spec_gce_ireland_2020_0424)
for k, v in od.items():
   if isinstance(v, str) and v.find(',') == -1:
     print(f'{k}="{v}",')
   else:
     print(f'{k}={v},')

"""
