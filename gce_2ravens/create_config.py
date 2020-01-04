"""
Render k8s; adding D3M environment variables to config
"""
from importlib import import_module
import re
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
        print('')
        print('-' * 40)
        print('Success!')
        print('K8s Template written: %s' % self.rendered_filename)
        print('')
        print('-' * 40)



def fillin_for_test(template_name, rendered_filename='ta3.yml', **kwargs):
    """Run for DM template winter eval as in
    https://datadrivendiscovery.org/wiki/pages/viewpage.action?pageId=11276800
    """
    global CURRENT_DIR

    info_dict = dict()

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

    return rendered_filename
    #ta3_copy_filepath = join(BASE_DIR, 'ta3.yaml')
    #shutil.copyfile(rendered_filename, ta3_copy_filepath)
    #print('file copied: %s' % ta3_copy_filepath)


def run_from_specs(specs):
    """Create a template from specs"""
    assert isinstance(specs, dict), \
        "specs is not a python dictionary"

    # Pre-render memory snippets
    #
    resource_lists = []
    for key_name, vals in specs.items():

        if key_name.startswith('resources') or \
            key_name.endswith('resources'):

            # for summing totals
            resource_lists.append([int(re.sub("[^0-9]", "", x)) for x in vals])

            # dict for resources template (snippet for k8s)
            info_dict = dict(name=key_name,
                             memory_request=vals[0],
                             memory_limit=vals[1],
                             cpu_request=vals[2],
                             cpu_limit=vals[3])

            # Render/Add resource information
            #
            trh = TemplateRenderHelper(info_dict,
                                       'resources_01.yaml',
                                       **dict(get_as_string=True))
            # print(trh.content_string)
            specs[key_name] = trh.content_string

    sum_list = [sum(i) for i in zip(*resource_lists)]
    resource_lists.append(['=======' for x in range(1, 5)])
    resource_lists.append(sum_list)
    resource_lists.insert(0, ['-------' for x in range(1, 5)] )
    resource_lists.insert(0, ['Mem req', 'Mem max', 'CPU req', 'CPU max', ] )
    for row in resource_lists:
        print('\t\t'.join([str(x) for x in row]))
    #print(sum_list)

    # ----------------------------
    # shared volume mounts
    # ----------------------------
    trh2 = TemplateRenderHelper(specs,
                               'volume_mounts_gce_02.yaml',
                               **dict(get_as_string=True))
    # print(trh.content_string)
    specs['shared_volume_mounts'] = trh2.content_string

    new_k8s_file = fillin_for_test(\
                        template_name=specs['template_name'],
                        rendered_filename=specs['rendered_filename'],
                        **dict(additional_info=specs))

    return new_k8s_file


def is_valid_choice(choice_str, num_choices):
    """Check that the choice is a valid integer"""
    if not isinstance(num_choices, int):
        return False

    if num_choices < 1:
        return False

    if not isinstance(choice_str, str):
        return False

    if not choice_str.isdigit():
        return False

    choice_int = int(choice_str)

    if choice_int < 1 or choice_int > num_choices:
        return False

    return True


def show_choices():
    """List config specs"""
    config_names = [x for x in dir(config_specs)
                    if x.upper().find('SPEC') > -1 and \
                       x.upper().find('XSPEC') == -1 and \
                        not x.startswith('_')]
    config_names.sort()

    print('-' * 40)
    print('The following specs were found to create a K8s template:\n')

    for idx, cnt in enumerate(config_names):
        user_msg = (f'({idx+1}) {cnt}')
        print(user_msg)

    choose_msg = (f"\nPlease choose a number between 1 and"
                  f" {len(config_names)}: ")

    chosen_num = input(choose_msg)

    while not is_valid_choice(chosen_num, len(config_names)):
        print('\n>> Oops! Not a valid choice!')
        chosen_num = input(choose_msg)

    chosen_spec = config_names[int(chosen_num) - 1]

    run_from_specs(eval(f'config_specs.{chosen_spec}'))


if __name__ == '__main__':
    show_choices()
