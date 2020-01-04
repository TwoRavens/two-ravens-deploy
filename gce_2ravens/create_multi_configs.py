"""
Used for the 11/2019 user testing
"""
from os.path import abspath, dirname, join
import sys
from datetime import datetime

CURRENT_DIR = dirname(abspath(__file__))
sys.path.append(dirname(CURRENT_DIR))
#sys.path.append(join(dirname(CURRENT_DIR), 'gce_ips'))

from config_specs import \
    (spec_multi_brown,
     spec_multi_brown2,
     spec_multi_brown2a, # less cpu/memory
     spec_multi_brown3_NOT_automl,
     spec_d3m_automl_dec,
     spec_automl_brown_2020_01)
from gce_ips.color_ip_table import COLOR_DOMAIN_PAIRS
from create_config import run_from_specs


CURR_YYYY_MMDD = None
def get_current_year_day():
    """YYYY_MMDD - e.g. '2020_0104', or similar"""
    global CURR_YYYY_MMDD

    if not CURR_YYYY_MMDD:
        dt_now = datetime.now()
        CURR_YYYY_MMDD = '%s_%s%s' % (dt_now.year,
                                      str(dt_now.month).zfill(2),
                                      str(dt_now.day).zfill(2),)

    return CURR_YYYY_MMDD

def create_single_test_config(the_specs, color_name, ip_address, **kwargs):
    """Create a single k8s config"""
    cnt = kwargs.get('cnt')
    rendered_fname_prefix = kwargs.get('rendered_fname_prefix', 'automl')

    if cnt:
        cnt = f'({cnt})'

    print(f'\n-- {cnt} {color_name}.2ravens.org: {ip_address} --')

    nameSuffix = ''
    serverName = '2ravens.org'
    hyphenColorName = ''
    if color_name:
        nameSuffix = f'-{color_name}'
        serverName = f'{color_name}.2ravens.org'
        hyphenColorName = f'_{color_name}'

    color_specs = dict(the_specs, **dict(\
                rendered_filename=f'{rendered_fname_prefix}{hyphenColorName}_{get_current_year_day()}.yaml',
                loadBalancerIP=f'{ip_address}',
                #
                RAVENS_SERVER_NAME=serverName,
                SESSION_COOKIE_NAME=f'ravens{hyphenColorName}_cookie',
                CSRF_COOKIE_NAME=f'ravens{hyphenColorName}_csrf_cookie',
                #
                installName=f'{color_name}',
                serviceNameSuffix=nameSuffix,))

    return run_from_specs(color_specs)


def create_configs(the_specs, rendered_fname_prefix, make_ALL_files=False):
    """Create k8s configs"""
    file_list = []
    cnt = 0
    for dcolor, ip_address in COLOR_DOMAIN_PAIRS:
        cnt += 1
        #if cnt < 11: continue
        if dcolor in ['terra',]:
            continue

        if dcolor == '':
            rendered_fname_prefix += '_2ravens'

        params = dict(rendered_fname_prefix=rendered_fname_prefix,
                      cnt=cnt)

        new_k8s_file = create_single_test_config(the_specs, dcolor,
                                                 ip_address, **params)
        file_list.append(new_k8s_file)
        #if cnt == 10:
        #    break

    big_file_contents = []
    for fname in file_list:
        if fname.find('terra') > -1:
            continue
        contents = open(fname, 'r').read()
        big_file_contents.append(contents)

    if make_ALL_files:
        all_contents = '\n'.join(big_file_contents)
        final_fname = join(CURRENT_DIR,
                           'rendered',
                           'TEST_20_ALL_INSTANCES_{get_current_year_day()}.yaml')
        open(final_fname, 'w').write(all_contents)
        print('final_file', final_fname)


if __name__ == '__main__':
    # spec_multi_brown2,
    # spec_multi_brown3_NOT_automl

    # D3M AutoML command
    #create_configs(spec_d3m_automl_dec,
    #               rendered_fname_prefix='demo_d3m',
    #               make_ALL_files=False)

    # AutoML command
    create_configs(spec_automl_brown_2020_01,
                   rendered_fname_prefix='autoML',
                   make_ALL_files=False)

    #create_configs(spec_multi_brown3_NOT_automl,
    #               rendered_fname_prefix='NOT_autoML',
    #               make_ALL_files=False)
