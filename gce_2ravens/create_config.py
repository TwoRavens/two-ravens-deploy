"""
Render k8s; adding D3M environment variables to config
"""
import shutil
import sys
from os.path import abspath, dirname, join, normpath, isdir, isfile
from jinja2 import (Template,
                    Environment,
                    BaseLoader,
                    PackageLoader,
                    select_autoescape)

import config_specs

CURRENT_DIR = dirname(abspath(__file__))
BASE_DIR = dirname(CURRENT_DIR)
TEMPLATE_DIR = join(CURRENT_DIR, 'templates')
#SNIPPET_DIR = join(CURRENT_DIR, 'snippets')
print('TEMPLATE_DIR', TEMPLATE_DIR)
# adding this path for the PackageLoader
print('CURRENT_DIR', CURRENT_DIR)
sys.path.append(dirname(CURRENT_DIR))


class TemplateRenderHelper(object):

    def __init__(self, template_dict, template_name, **kwargs):
        """execute main method"""
        self.jinja_env = Environment(\
            loader=PackageLoader('gce_2ravens'),
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



def fillin_for_test(template_name, rendered_filename='ta3.yml', **kwargs):
    """Run for DM template winter eval as in
    https://datadrivendiscovery.org/wiki/pages/viewpage.action?pageId=11276800
    """
    global CURRENT_DIR

    info_dict = dict(\
        tworavens_registry=('registry.datadrivendiscovery.org/ta3-submissions/'
                            'ta3-two-ravens/ravens-deploy-may2019'),
        # loadBalancerIP='10.108.29.7', # 2ravens.datadrivendiscovery.org
        loadBalancerIP='10.108.29.8', # 2ravens-summer.datadrivendiscovery.org
        eval_dataset_path=('/datasets/opt/datasets/seed_datasets_current'
                           '/185_baseball'),
        #eval_dataset_path=('/datasets/opt/datasets/seed_datasets_data_augmentation'
        #                   '/DA_college_debt # todo replace me'),
        static_dataset_path=('/opt/static_files'),
        D3MRUN='ta2ta3',
        D3MINPUTDIR='/input',
        D3MPROBLEMPATH='/input/TRAIN/problem_TRAIN/problemDoc.json',
        D3MLOCALDIR='/output/D3MLOCALDIR',
        )

    # Add or overwrite any arguments
    #
    additional_info = kwargs.get('additional_info', {})
    info_dict.update(additional_info)

    # template_name = 'dm_ravens_deploy_17_ta2_Brown.yml'

    rendered_filename = join(CURRENT_DIR,
                             'rendered',
                             rendered_filename)

    trh = TemplateRenderHelper(info_dict,
                               template_name,
                               rendered_filename=rendered_filename)

    ta3_copy_filepath = join(BASE_DIR, 'ta3.yaml')
    shutil.copyfile(rendered_filename, ta3_copy_filepath)
    print('file copied: %s' % ta3_copy_filepath)

def run_brown_template_debt():
    """Run Brown template"""

    registry_name = ('registry.datadrivendiscovery.org'
                     '/ta3-submissions/ta3-two-ravens/summer2019')

    xregistry_name = ('tworavens')

    extra_args = dict(\
            tworavens_registry=registry_name,
            eval_dataset_path=('/datasets/opt/datasets/'
                               'seed_datasets_data_augmentation/'
                               'DA_poverty_estimation'),)

    fillin_for_test(template_name=get_current_template(),
                    rendered_filename='ta3.yaml',
                    **dict(additional_info=extra_args))



def run_brown_template_baseball():
    """Run Brown template"""

    extra_args = dict(\
            tworavens_registry='tworavens',
            eval_dataset_path=('/datasets/opt/datasets/seed_datasets_current/'
                               '185_baseball'),)

    fillin_for_test(template_name=get_current_template(),
                    rendered_filename='ta3-july-baseball.yml',
                    **dict(additional_info=extra_args))


def run_from_specs(specs):
    """Create a template from specs"""
    assert isinstance(specs, dict), \
        "specs is not a python dictionary"

    fillin_for_test(template_name=specs['template_name'],
                    rendered_filename=specs['rendered_filename'],
                    **dict(additional_info=specs))


def get_current_template():
    """Return latest template"""
    return 'dm_ravens_deploy_09_ta2_Brown.yaml'

if __name__ == '__main__':
    # run_brown_template_debt_final()
    #run_brown_template_baseball()
    #run_brown_template_debt()

    run_from_specs(config_specs.gce_specs_01)
