"""
Used for the 11/2019 user testing
"""
from os.path import abspath, dirname, join
import sys

CURRENT_DIR = dirname(abspath(__file__))
sys.path.append(dirname(CURRENT_DIR))
#sys.path.append(join(dirname(CURRENT_DIR), 'gce_ips'))

from config_specs import spec_multi_brown
from gce_ips.color_ip_table import COLOR_DOMAIN_PAIRS
from create_config import run_from_specs


def create_single_test_config(color_name, ip_address, cnt=None):
    """Create a single k8s config"""
    if cnt:
        cnt = f'({cnt})'

    print(f'\n-- {cnt} {color_name}.2ravens.org: {ip_address} --')

    color_specs = dict(spec_multi_brown, **dict(\
                rendered_filename=f'test_{color_name}_brown_2019_1108.yaml',
                loadBalancerIP=f'{ip_address}',
                #
                RAVENS_SERVER_NAME=f'{color_name}.2ravens.org',
                SESSION_COOKIE_NAME=f'ravens_{color_name}',
                CSRF_COOKIE_NAME=f'ravens_{color_name}_csrf',
                #
                installName=f'{color_name}',
                serviceNameSuffix=f'-{color_name}',))

    return run_from_specs(color_specs)


def create_configs():
    """Create k8s configs"""
    file_list = []
    cnt = 0
    for dcolor, ip_address in COLOR_DOMAIN_PAIRS:
        cnt += 1
        new_k8s_file = create_single_test_config(dcolor, ip_address, cnt=cnt)
        file_list.append(new_k8s_file)
        #if cnt == 5:
        #    break

    big_file_contents = []
    for fname in file_list:
        if fname.find('terra') > -1:
            continue
        contents = open(fname, 'r').read()
        big_file_contents.append(contents)
    all_contents = '\n'.join(big_file_contents)
    final_fname = join(CURRENT_DIR, 'rendered', 'TEST_ALL_INSTANCES.yaml')
    open(final_fname, 'w').write(all_contents)
    print('final_file', final_fname)


if __name__ == '__main__':
    create_configs()
