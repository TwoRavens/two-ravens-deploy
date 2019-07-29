"""
Render k8s; adding D3M environment variables to config
"""
import sys
from os.path import abspath, dirname, join, normpath, isdir, isfile
from jinja2 import (Template,
                    Environment,
                    BaseLoader,
                    PackageLoader,
                    select_autoescape)

CURRENT_DIR = dirname(abspath(__file__))
TEMPLATE_DIR = join(CURRENT_DIR, 'ci_templates')
#SNIPPET_DIR = join(CURRENT_DIR, 'snippets')
print('TEMPLATE_DIR', TEMPLATE_DIR)
# adding this path for the PackageLoader
print('CURRENT_DIR', CURRENT_DIR)
sys.path.append(dirname(CURRENT_DIR))

from jinja2 import Environment, FileSystemLoader
template_dir = '/home/colin/template_dir'
env = Environment(loader=FileSystemLoader(template_dir))

class TemplateRenderHelper(object):

    def __init__(self, template_dict, template_name, **kwargs):
        """execute main method"""
        self.jinja_env = Environment(\
            #loader=PackageLoader('dm_test_files_2019'),
            loader=FileSystemLoader(TEMPLATE_DIR),
            autoescape=select_autoescape(['html', 'xml']))

        self.content_string = None

        self.rendered_filename = kwargs.get('rendered_filename', None)
        self.get_as_string = kwargs.get('get_as_string', False)


        self.render_template(template_dict,
                             template_name)



    def render_template(self, template_dict, template_name):
        """Make a simple template and write it to the output directory"""
        assert template_dict, 'template_dict cannot be None'

        template = self.jinja_env.get_template(template_name)

        # create content
        #
        content = template.render(template_dict)

        if self.get_as_string:
            self.content_string = content
            return

        # write file out
        #
        open(self.rendered_filename, 'w').write(content)
        print('-' * 40)
        print('template written: %s' % self.rendered_filename)
        print('-' * 40)



def get_d3m_snippet(info_dict, template_name):
    """Render a snippet"""
    trh = TemplateRenderHelper(info_dict,
                               template_name,
                               get_as_string=True)

    return trh.content_string


def fillin_for_ci(template_name, rendered_filename='ta3.yml', **kwargs):
    """Run for DM template winter eval as in
    https://datadrivendiscovery.org/wiki/pages/viewpage.action?pageId=11276800
    """
    global CURRENT_DIR

    FOR_CI_ONLY = kwargs.get('FOR_CI_ONLY', False)

    info_dict = dict(\
        loadBalancerIP='10.108.29.7',
        eval_dataset_path=('/datasets/opt/datasets/seed_datasets_current'
                           '/185_baseball # todo replace me'),
        #eval_dataset_path=('/datasets/opt/datasets/seed_datasets_data_augmentation'
        #                   '/DA_college_debt # todo replace me'),
        static_dataset_path=('/opt/static_files'),
        D3MRUN='ta2ta3',
        D3MINPUTDIR='/input',
        D3MPROBLEMPATH='/input/TRAIN/problem_TRAIN/problemDoc.json',
        D3MLOCALDIR='/output/D3MLOCALDIR',
        )

    if FOR_CI_ONLY:

        # Different D3MPROBLEMPATH. Removes multiple variables
        #
        info_dict['ravens_config_d3m'] = get_d3m_snippet(\
                                            info_dict,
                                            'ravens-config-d3m-04-CI.yml')

        # Differs by
        #   - TA2_TEST_SERVER_URL
        #   - WEBSOCKET_PREFIX
        info_dict['ravens_config_ta3'] = get_d3m_snippet(\
                                            info_dict,
                                            'ravens-config-ta3-CI.yml')

        # Same as DM
        #
        info_dict['container_volume_mounts'] = get_d3m_snippet(\
                                info_dict,
                                'container-volume-mounts-03.yml')

        # Remove load balancer
        #
        info_dict['load_balancer'] = ''

        

    else:
        info_dict['ravens_config_d3m'] = get_d3m_snippet(\
                                            info_dict,
                                            'ravens-config-d3m-03.yml')

        info_dict['ravens_config_ta3'] = get_d3m_snippet(\
                                            info_dict,
                                            'ravens-config-ta3.yml')

        info_dict['container_volume_mounts'] = get_d3m_snippet(\
                                        info_dict,
                                        'container-volume-mounts-03.yml')

        info_dict['load_balancer'] = get_d3m_snippet(\
                                    info_dict,
                                    'load_balancer_01.yml')

        info_dict['volumes_baseball'] = get_d3m_snippet(\
                                    info_dict,
                                    'volumes_baseball.yml')

    # info_dict['pod_presets'] = get_d3m_snippet(\
    #                                info_dict,
    #                                'pod-preset-01.yml')
    # Add or overwrite any arguments
    #
    additional_info = kwargs.get('additional_info', {})
    info_dict.update(additional_info)

    # template_name = 'dm_ravens_deploy_17_ta2_Brown.yml'

    rendered_filename = join(CURRENT_DIR,
                             'ci_rendered',
                             rendered_filename)

    trh = TemplateRenderHelper(info_dict,
                               template_name,
                               rendered_filename=rendered_filename)



if __name__ == '__main__':

    fillin_for_ci(template_name='system_06-ta2ta3.yml',
                  #rendered_filename='ta3-2019-tr7-greed-augmented.yml',
                  rendered_filename='system-ta2ta3.yml',
                  **{})
