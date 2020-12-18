"""List of colors / IPs for domains"""
import socket

alt_problem_path = ('/ravens_volume/test_data/TR85_Ethiopia_zone_mon_sub'
                    '/TRAIN/problem_TRAIN/problemDoc.json')
alt_problem_args = dict(D3MPROBLEMPATH=alt_problem_path,)

GCE_DEMO_INFO = [('demo', '35.193.45.98', {})]

AZURE_DEMO_INFO = [#('apricot', '40.76.171.8', {}),
                   ('demo', '20.62.216.240', {}),
                   #('testing', '20.62.247.224', {}),
                   ]


GCE_COLOR_DOMAIN_PAIRS = [\
        #('apricot', '34.69.254.93', {}),  # apricot.2ravens.org (GCE)
        #('testing', '35.223.87.48', {}),     # cyan.2ravens.org (GCE)
        #('demo', '35.193.45.98', {}),     # cyan.2ravens.org (GCE)
        #('cyan', '104.154.189.22', {}),     # cyan.2ravens.org (GCE)

        #('blue', '35.222.247.157', {}),      # blue.2ravens.org (GCE) raven-ip-blue
        #('lime', '35.222.64.114', {}),       # lime.2ravens.org (GCE)    raven-ip-lime
        #('magenta', '35.192.35.125', {}),  # magenta.2ravens.org (GCE)  raven-ip-magenta
        #('mint', '35.225.129.2', {}), # mint.2ravens.org (GCE) raven-ip-mint
        #('navy', '34.72.175.15', {}), # navy.2ravens.org (GCE) raven-ip-navy

        #('olive', '35.232.148.148', {}),    # olive.2ravens.org (GCE)     raven-ip-olive
        #('orange', '35.223.135.139', {}), # orange.2ravens.org (GCE) raven-ip-orange
        #('purple', '34.71.71.11', {}), # purple.2ravens.org (GCE) raven-ip-purple
        #('red', '104.197.86.199', {}), # red.2ravens.org (GCE)   raven-ip-red
        #('yellow', '34.72.173.46', {}),   # red.2ravens.org (GCE)  raven-ip-yellow

        #('pink', ''),
        #('white', ''),

        ]

# see https://datadrivendiscovery.org/wiki/pages/viewpage.action?spaceKey=gov&title=Creating+Services
DM_COLOR_DOMAIN_PAIRS = [\
            # ('2ravens', '10.108.29.7', {}),  # https://2ravens.datadrivendiscovery.org/ (DM)

            #('2ravens-summer', '10.108.34.30', {}),  # https://2ravens.datadrivendiscovery.org/ (DM)
            ('', '10.108.34.30', {}), # EVAL!! # https://2ravens.datadrivendiscovery.org/ (DM)

            #('red-2ravens', '10.108.29.15', {}), # 10.108.29.9 tworavens1.datadrivendiscovery.org (GCE)
            #('blue-2ravens', '10.108.29.10', {}), # tworavens1.datadrivendiscovery.org (GCE)
            #('lime-2ravens', '10.108.29.11'), # tworavens1.datadrivendiscovery.org (GCE)
            #('maroon-2ravens', '10.108.29.12'), # tworavens1.datadrivendiscovery.org (GCE)
            #('white-2ravens', '10.108.29.13'), # tworavens1.datadrivendiscovery.org (GCE)
            #('orange-2ravens', '10.108.29.14'), # tworavens1.datadrivendiscovery.org (GCE)
            #('lime', '34.67.169.83'),   # lime.2ravens.org (GCE)
            #('', '104.197.235.238'), # 2ravens.org (GCE)
            #
            ]

#COLOR_DOMAIN_PAIRS = DM_COLOR_DOMAIN_PAIRS
#COLOR_DOMAIN_PAIRS = GCE_COLOR_DOMAIN_PAIRS

def is_domain_set(dcolor, ip_address, cnt=''):
    """
    Check if the subdomain as been set
    > socket.gethostbyname_ex('red.2ravens.org')
    ('red.2ravens.org', [], ['35.224.128.61'])
    """
    hostname = f'{dcolor}.2ravens.org'
    if cnt:
        cnt = f'({cnt})'
    print(f'\n-- {cnt} {hostname}: {ip_address} --')
    #
    try:
        domain_info = socket.gethostbyname_ex(hostname)
    except socket.gaierror as err_obj:
        print('    > ERROR! ', err_obj)
        return
    #
    if len(domain_info) >= 3:
        ip_list = domain_info[2]
        if ip_list and ip_address == ip_list[0]:
            print('    > looks good!')
        else:
            print('    > ERROR!')
            print('domain_info', domain_info)

def check_domains(color_pairs=GCE_COLOR_DOMAIN_PAIRS):
    """Check if the domain is set to the expected IP"""
    cnt = 0
    for dcolor, ip_address in color_pairs:
        #print(f'{dcolor}.2ravens.org')
        cnt += 1
        is_domain_set(dcolor, ip_address, cnt=cnt)


if __name__ == '__main__':
    check_domains()
