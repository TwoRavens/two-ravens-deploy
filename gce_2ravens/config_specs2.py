"""
# Starting with new base spec on 7/14/2020

Used by create_config for k8s template settings

IMPORTANT: When adding a new dict, make sure the name has 'spec' or 'SPEC' in it.
    examples: 'K8S_SPEC_001', 'taxi_spec_nyu', 'spec_poverty_mit'
"""

base_spec_01 = dict(\
    #
    #template_name="gce_ravens_deploy_029-onepod.yaml",
    template_name="gce_ravens_deploy_030-onepod.yaml",
    #rendered_filename="gce_2ravens_2020_0714.yaml",   # overwritten for multi configs
    #
    # Volume mount and resource templates
    #
    VOLUME_MOUNTS_TEMPLATE_FILENAME="dm_volume_mounts_01.yaml",
    RESOURCES_TEMPLATE_FILENAME="resources_01.yaml",
    #
    #
    DJANGO_SETTINGS_MODULE="tworavensproject.settings.gce_settings",
    #
    # server and cookies
    #
    RAVENS_SERVER_NAME="2ravens.org",
    SESSION_COOKIE_NAME="ravens_base",
    CSRF_COOKIE_NAME="ravens_base_csrf",
    #
    # NGINX
    #
    NGINX_SERVER_NAME=".2ravens.org",
    # 24 mb
    NGINX_MAX_UPLOAD_SIZE="24m",
    # 24 mb
    DATA_UPLOAD_MAX_MEMORY_SIZE="25165824",
    #
    # load balancer, changes with mutli config
    loadBalancerIP="104.197.235.238  # 2ravens.org",
    #
    # docker registry. e.g. 'tworavens' is on DockerHub
    #
    tworavens_registry="tworavens",
    # tag used for ravens_main, rook, and nginx
    #tworavens_container_tag="comfrey-2020-1110-map",
    tworavens_container_tag="comfrey-2020-1013",
    #
    #   TA2
    #
    #ta2_image="dmartinez05/tamuta2:latest",
    #ta2_image_comment="TAMU TA2!",
    #ta2_image="registry.gitlab.com/vida-nyu/d3m/ta2:latest",
    #ta2_image_comment="NYU TA2!",
    #ta2_image="registry.datadrivendiscovery.org/sheath/cmu-ta2:latest",
    #ta2_image="gcr.io/raven2-186120/cmu-ta2:2020-0929",
    ta2_image="ravenscontainerregistry.azurecr.io/cmu-ta2:2020-0929",
    ta2_image_comment="CMU TA2!",
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
    #D3MPROBLEMPATH="/ravens_volume/test_data/185_baseball/TRAIN/problem_TRAIN/problemDoc.json",
    D3MPROBLEMPATH=('/ravens_volume/test_data/TR92_pgm_grid_samp'
                    '/TRAIN/problem_TRAIN/problemDoc.json'),
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
    #ta2_resources=['20000Mi', '25000Mi', '3000m', '4000m'],
    ta2_resources=['20000Mi', '25000Mi', '6000m', '8000m'],
    ta3_resources=['1000Mi', '3000Mi', '1000m', '1500m'],
    celery_resources=['4500Mi', '6000Mi', '2000m', '2000m'],
    rook_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
    mongo_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
    redis_resources=['500Mi', '1000Mi', '500m', '500m'],
    nginx_resources=['256Mi', '500Mi', '500m', '500m'],
    postgres_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
    #
    # Wrapped solver settings
    #
    TA2_D3M_SOLVER_ENABLED="True",
    TA2_WRAPPED_SOLVERS=["TwoRavens", "tpot"],
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
    #ta2_image="dmartinez05/tamuta2:latest",
    #ta2_image_comment="TAMU TA2!",
    #ta2_image="registry.datadrivendiscovery.org/sheath/cmu-ta2:latest",
    #ta2_image_comment="CMU TA2!",
    ))

dm_eval_2020_08 = dict(dm_summer_2020_0717, **dict(\
    template_name="dm_summer_eval_pod_02.yaml",
    #
    externalPort=8080,  # D3M proxy tool maps to 8080 on pod
    #
    loadBalancerIP="10.108.34.30",  # 2ravens.org",
    #
    VOLUME_MOUNTS_TEMPLATE_FILENAME="dm_volume_mounts_02_eval.yaml",
    #
    RESOURCES_TEMPLATE_FILENAME='resources_dm_01.yaml',
    RAVENS_SERVER_NAME='datadrivendiscovery.org',
    #
    NGINX_SERVER_NAME=".datadrivendiscovery.org",
    #
    # 100 mb
    NGINX_MAX_UPLOAD_SIZE="100m",
    # 100 mb
    DATA_UPLOAD_MAX_MEMORY_SIZE="104857600",
    # respository
    tworavens_registry="registry.datadrivendiscovery.org/ta3-submissions/ta3-two-ravens/summer2020evaluation",
    tworavens_container_tag="yarrow",
    #
    # pull policies
    pull_policy_ta2="Always",
    pull_policy_ravens_main="Always",
    pull_policy_rook="Always",
    pull_policy_nginx="Always",
    #
    #   TA2
    #
    ta2_image_comment="NYU TA2!",
    ta2_image="registry.datadrivendiscovery.org/ta2-submissions/ta2-nyu/summer2020evaluation:latest",
    #ta2_image="registry.gitlab.com/vida-nyu/d3m/ta2:latest",
    #
    #ta2_image_comment="TAMU TA2!",
    #ta2_image="dmartinez05/tamuta2:latest",
    #
    #ta2_image_comment="CMU TA2!",
    #ta2_image="registry.datadrivendiscovery.org/sheath/cmu-ta2:latest",
    #
    # D3M variables
    #
    D3MRUN="ta2ta3",
    D3MINPUTDIR="/input",
    D3MOUTPUTDIR="/output",
    D3MSTATICDIR="/static",
    D3MPROBLEMPATH="/input/LL1_h1b_visa_apps_7480/TRAIN/problem_TRAIN/problemDoc.json",
    D3MLOCALDIR="/output/D3MLOCALDIR",
    #D3MCPU="14",
    #D3MRAM="56Gi",
    D3MTIMEOUT="3600",
    D3MCONTEXT="TESTING",
    #
    # Datamart
    #
    # DATAMART_URL_NYU
    DATAMART_URL_NYU="http://10.108.33.5:8002",
    DATAMART_URL_ISI="http://10.108.20.4:14080"
    ))


azure_demo_site = dict(base_spec_01, **dict(\
    #
    tworavens_registry="ghcr.io/tworavens/tworavens",
    tworavens_container_tag="2021-0523-disco-922",
    #
    #ta2_image="ravenscontainerregistry.azurecr.io/cmu-ta2:2021-0222",
    #
    DJANGO_SETTINGS_MODULE="tworavensproject.settings.azure_settings",
    #D3MPROBLEMPATH="/ravens_volume/test_data/TR103_germany_state/TRAIN/problem_TRAIN/problemDoc.json",
    D3MPROBLEMPATH="/ravens_volume/test_data/TR104_Police_Incidents/TRAIN/problem_TRAIN/problemDoc.json",
    #
    #template_name="gce_ravens_demo-01-noTA2.yaml",
    template_name="azure_ravens_deploy_032-onepod.yaml",
    #
    # 2 mb
    NGINX_MAX_UPLOAD_SIZE="2m",
    # 2 mb
    DATA_UPLOAD_MAX_MEMORY_SIZE="2097152",
    #
    #TA2_D3M_SOLVER_ENABLED="False",
    #TA2_WRAPPED_SOLVERS="['TwoRavens']",
    #
    #TEST_DATASETS="185_baseball 196_autoMpg",
    #
    DISPLAY_DATAMART_UI="False",
    #
    # Dataset mode, hide/show tabs
    #
    DATASET_SHOW_TAB_PRESETS="True",
    DATASET_SHOW_TAB_UPLOAD="False",
    DATASET_SHOW_TAB_ONLINE="False",
    #
    # Auto-login
    #
    #DEMO_AUTO_LOGIN="True",
    #
    #ta2_resources=['20000Mi', '25000Mi', '6000m', '8000m'],
    #nginx_resources=['256Mi', '500Mi', '500m', '500m'],
    #ta3_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
    #celery_resources=['4500Mi', '6000Mi', '1000m', '1500m'],
    #rook_resources=['1000Mi', '1000Mi', '800m', '800m'],
    #mongo_resources=['1000Mi', '1000Mi', '500m', '1000m'],
    #redis_resources=['500Mi', '500Mi', '500m', '500m'],
    #postgres_resources=['500Mi', '1000Mi', '500m', '500m'],
    #
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
