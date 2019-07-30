"""
Used by create_config for k8s template settings
"""

"""
Poverty dataset with MIT TA2
"""
K8S_SPECS_01 = dict(\
    #
    template_name='gce_ravens_deploy_012_poverty_w_probe.yaml',
    rendered_filename='ta3_fl_poverty_2019_0730.yaml',
    #
    ta2_image='gcr.io/raven2-186120/mit-fl-ta2:july-2019',
    ta2_image_comment='FL TA2',
    #
    loadBalancerIP='104.197.235.238  # 2ravens.org',
    tworavens_registry='tworavens',
    tworavens_container_tag='july-2019',  # nginx, ravens-main, rook
    #
    pull_policy_ta2='IfNotPresent',
    pull_policy_ravens_main='Always',
    pull_policy_rook='Always',
    #
    externalPort=80,
    #
    #
    D3MRUN='ta2ta3',
    D3MINPUTDIR='/ravens_volume/test_data/DA_poverty_estimation',
    D3MPROBLEMPATH=('/ravens_volume/test_data/DA_poverty_estimation'
                    '/TRAIN/problem_TRAIN/problemDoc.json'),
    D3MOUTPUTDIR='/ravens_volume/test_output/DA_poverty_estimation',
    D3MLOCALDIR='/ravens_volume/test_output/local_dir',
    D3MSTATICDIR='/ravens_volume/test_output/static_dir',
    D3MCPU="1",
    D3MRAM="512Mi",
    D3MTIMEOUT="10",
    #
    #
    DATAMART_URL_NYU="https://auctus.vida-nyu.org",
    DATAMART_URL_ISI="http://dsbox02.isi.edu:9000"
    )

"""
Poverty dataset with Brown TA2
"""
K8S_SPECS_02 = dict(K8S_SPECS_01, **dict(\
                rendered_filename='ta3_brown_poverty_2019_0730.yaml',
                #
                ta2_image='gcr.io/raven2-186120/brown-ta2:summer-2019',
                ta2_image_comment='Brown TA2',))
