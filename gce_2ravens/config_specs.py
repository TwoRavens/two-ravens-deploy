"""
Used by create_config for k8s template settings

IMPORTANT: When adding a new dict, make sure the name has 'spec' or 'SPEC' in it.
    examples: 'K8S_SPEC_001', 'taxi_spec_nyu', 'spec_poverty_mit'
"""

"""
Poverty dataset with MIT TA2
"""
spec_poverty_mit = dict(\
    #
    template_name='gce_ravens_deploy_015_poverty_no_probe.yaml',
    rendered_filename='ta3_fl_poverty_2019_1015.yaml',
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
spec_poverty_brown = dict(spec_poverty_mit, **dict(\
                rendered_filename='ta3_brown_poverty_2019_1015.yaml',
                #
                ta2_image='gcr.io/raven2-186120/brown-ta2:summer-2019',
                ta2_image_comment='Brown TA2',))
