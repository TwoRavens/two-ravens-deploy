import requests

PROJECT_ID = 'raven2-186120'
REGION = 'us-central1'


def make_request(address_name):
    """Create an IP"""
    base_url = (f'https://compute.googleapis.com/compute/v1/projects'
                f'/{PROJECT_ID}/regions/{REGION}/addresses')
    params = dict(name=address_name)
    r = requests.post(base_url, data=params)
    print(r.status_code)
    print(r.text)


"""
gcloud compute addresses create [ADDRESS_NAME] \
    [--region [REGION] | --global ] \
    [--ip-version [IPV4 | IPV6]]

gcloud compute addresses create apricot-2ravens \
--region us-central1 --ip-version IPV4
"""
