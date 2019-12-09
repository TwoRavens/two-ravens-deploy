"""
Used by create_config for k8s template settings

IMPORTANT: When adding a new dict, make sure the name has 'spec' or 'SPEC' in it.
    examples: 'K8S_SPEC_001', 'taxi_spec_nyu', 'spec_poverty_mit'
"""

"""
Poverty dataset with MIT TA2
"""
spec_base = dict(\
    #
    template_name='gce_ravens_deploy_016_terra_mongo_container.yaml',
    #rendered_filename='ta3_fl_poverty_2019_1015.yaml',
    #
    RAVENS_SERVER_NAME='2ravens.org',
    SESSION_COOKIE_NAME=f'ravens_base',
    CSRF_COOKIE_NAME=f'ravens_base_csrf',
    #ta2_image='gcr.io/raven2-186120/mit-fl-ta2:july-2019',
    #ta2_image_comment='FL TA2',
    #
    loadBalancerIP='104.197.235.238  # 2ravens.org',
    tworavens_registry='tworavens',
    tworavens_container_tag='july-2019',  # nginx, ravens-main, rook
    #
    pull_policy_ta2='IfNotPresent',
    pull_policy_ravens_main='Always',
    pull_policy_rook='Always',
    pull_policy_nginx='Always',
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
xspec_poverty_brown = dict(spec_base, **dict(\
                rendered_filename='ta3_brown_poverty_2019_1015.yaml',
                #
                ta2_image='gcr.io/raven2-186120/brown-ta2:summer-2019',
                ta2_image_comment='Brown TA2',
                #
                pull_policy_ta2='IfNotPresent',
                pull_policy_ravens_main='IfNotPresent',
                pull_policy_rook='IfNotPresent',
                ))


spec_autompg_brown = dict(spec_base, **dict(\
                rendered_filename='ta3_brown_autompg_2019_1015.yaml',
                #
                ta2_image='gcr.io/raven2-186120/brown-ta2:summer-2019',
                ta2_image_comment='Brown TA2',
                #
                pull_policy_ta2='IfNotPresent',
                pull_policy_ravens_main='IfNotPresent',
                pull_policy_rook='IfNotPresent',
                #
                D3MINPUTDIR='/ravens_volume/test_data/196_autoMpg',
                D3MPROBLEMPATH=('/ravens_volume/test_data/196_autoMpg'
                                '/TRAIN/problem_TRAIN/problemDoc.json'),
                D3MOUTPUTDIR='/ravens_volume/test_output/196_autoMpg',
                ))

xspec_terra_brown = dict(spec_base, **dict(\
                rendered_filename='ta3_brown_terra_2019_1104.yaml',
                #
                ta2_image='gcr.io/raven2-186120/brown-ta2:summer-2019',
                ta2_image_comment='Brown TA2',
                #
                pull_policy_ta2='IfNotPresent',
                pull_policy_ravens_main='IfNotPresent',
                pull_policy_rook='IfNotPresent',
                #
                D3MINPUTDIR='/ravens_volume/test_data/LL1_terra_canopy_height_long_form_s4_70',
                D3MPROBLEMPATH=('/ravens_volume/test_data/LL1_terra_canopy_height_long_form_s4_70'
                                '/TRAIN/problem_TRAIN/problemDoc.json'),
                D3MOUTPUTDIR='/ravens_volume/test_output/LL1_terra_canopy_height_long_form_s4_70',
                ))

spec_multi_brown = dict(spec_base, **dict(\
                template_name='gce_ravens_deploy_018_multi_container.yaml',
                rendered_filename='ta3_brown_multi_2019_1106.yaml',
                #
                ta2_image='gcr.io/raven2-186120/brown-ta2:summer-2019',
                ta2_image_comment='Brown TA2',
                #
                tworavens_container_tag='nov-test',
                #
                pull_policy_ta2='IfNotPresent',
                pull_policy_ravens_main='Always',
                pull_policy_rook='IfNotPresent',
                #
                D3MINPUTDIR='/ravens_volume/test_data',
                D3MPROBLEMPATH=('/ravens_volume/test_data/185_baseball'
                                '/TRAIN/problem_TRAIN/problemDoc.json'),
                D3MOUTPUTDIR='/ravens_volume/test_output',
                #
                #
                serviceNameSuffix='',
                ))

spec_multi_brown2 = dict(spec_multi_brown, **dict(\
                template_name='gce_ravens_deploy_020_auto_ml.yaml',
                rendered_filename='ta3_brown_multi_2019_1205.yaml',
                #
                tworavens_container_tag='dec-test',
                #
                #   memory requested, memory limit, cpu requested, cpu limit
                #
                ta2_resources=['20000Mi', '25000Mi', '3000m', '3000m'],
                # 14 CPUs and 56GB, that was our configuration for summer evaluation
                #
                ta3_resources=['1000Mi', '3000Mi', '1000m', '1500m'],
                celery_resources=['9000Mi', '12000Mi', '4000m', '4000m'],
                #
                rook_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
                #
                mongo_resources=['1000Mi', '2000Mi', '500m', '1000m'],
                redis_resources=['500Mi', '1000Mi', '500m', '1000m'],
                nginx_resources=['256Mi', '500Mi', '500m', '500m'],
                ))

#
#   Bring down the CPU/Memory resources
#
spec_multi_brown2a = dict(spec_multi_brown, **dict(\
                template_name='gce_ravens_deploy_020_auto_ml.yaml',
                rendered_filename='ta3_brown_multi_2019_1205.yaml',
                #
                tworavens_container_tag='dec-test',
                #
                #   memory requested, memory limit, cpu requested, cpu limit
                #
                ta2_resources=['10000Mi', '11000Mi', '2000m', '2000m'],
                # 14 CPUs and 56GB, that was our configuration for summer evaluation
                #
                ta3_resources=['1000Mi', '3000Mi', '500m', '500m'],
                celery_resources=['9000Mi', '12000Mi', '2000m', '3000m'],
                #
                rook_resources=['1000Mi', '2000Mi', '500m', '500m'],
                #
                mongo_resources=['1000Mi', '2000Mi', '500m', '1000m'],
                redis_resources=['500Mi', '1000Mi', '500m', '500m'],
                nginx_resources=['256Mi', '500Mi', '500m', '500m'],
                ))

spec_multi_brown3_NOT_automl = dict(spec_multi_brown, **dict(\
                template_name='gce_ravens_deploy_020_auto_ml.yaml',
                rendered_filename='nov_ta3_brown_multi_2019_1205.yaml',
                #
                tworavens_container_tag='nov-test',
                #
                #   memory requested, memory limit, cpu requested, cpu limit
                #
                ta2_resources=['20000Mi', '25000Mi', '3000m', '3000m'],
                # 14 CPUs and 56GB, that was our configuration for summer evaluation
                #
                ta3_resources=['1000Mi', '3000Mi', '1000m', '1500m'],
                celery_resources=['4000Mi', '8000Mi', '1000m', '2000m'],
                #
                rook_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
                #
                mongo_resources=['1000Mi', '2000Mi', '500m', '1000m'],
                redis_resources=['500Mi', '1000Mi', '500m', '1000m'],
                nginx_resources=['256Mi', '500Mi', '500m', '500m'],
                ))

spec_d3m_automl_dec = dict(spec_multi_brown2, **dict(\
                template_name='gce_ravens_deploy_021a_d3m_auto_ml.yaml',
                rendered_filename='d3m_2019_1209.yaml',
                #
                tworavens_container_tag='dec-test',
                #
                ta2_image='registry.datadrivendiscovery.org/ta2-submissions/ta2-brown/summer2019',
                #
                D3MRUN='ta2ta3',
                # ------------------------------
                D3MINPUTDIR='/ravens_volume/test_data/185_baseball',
                D3MPROBLEMPATH=('/ravens_volume/test_data/185_baseball'
                                '/TRAIN/problem_TRAIN/problemDoc.json'),
                D3MOUTPUTDIR='/ravens_volume/test_output/185_baseball',
                D3MLOCALDIR='/ravens_volume/test_output/local_dir',
                D3MSTATICDIR='/ravens_volume/test_output/static_dir',
                # ------------------------------
                #D3MINPUTDIR='/input',
                #D3MOUTPUTDIR='/output',
                #D3MSTATICDIR='/static',
                #D3MPROBLEMPATH='/opt/datasets/seed_datasets_current/196_autoMpg/TRAIN',
                #D3MPROBLEMPATH='/ravens_volume/test_data/185_baseball',
                #D3MLOCALDIR='/output',
                #   memory requested, memory limit, cpu requested, cpu limit
                #
                ta2_resources=['20000Mi', '25000Mi', '3000m', '5000m'],
                # 14 CPUs and 56GB, that was our configuration for summer evaluation
                #
                ta3_resources=['1000Mi', '3000Mi', '1000m', '1500m'],
                celery_resources=['4000Mi', '8000Mi', '2000m', '4000m'],
                #
                rook_resources=['1000Mi', '2000Mi', '1000m', '1000m'],
                #
                mongo_resources=['1000Mi', '2000Mi', '500m', '1000m'],
                redis_resources=['500Mi', '1000Mi', '500m', '1000m'],
                nginx_resources=['256Mi', '500Mi', '500m', '500m'],
                ))
