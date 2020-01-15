"""List of colors / IPs for domains"""
import socket

GCE_COLOR_DOMAIN_PAIRS = [\
            ('blue', '35.225.184.21'),  # blue.2ravens.org (GCE)
            ('cyan', '104.154.189.22'), # cyan.2ravens.org (GCE)
            ('lime', '34.67.169.83'),   # lime.2ravens.org (GCE)
            ('', '104.197.235.238'), # 2ravens.org (GCE)
            #
            #('', '10.108.29.7'), # 2ravens.datadrivendiscovery.org
            ]

DM_COLOR_DOMAIN_PAIRS = [\
            ('summer', '10.108.29.7'),  # https://2ravens-summer.datadrivendiscovery.org/ (DM)
            #('cyan', '104.154.189.22'), # cyan.2ravens.org (GCE)
            #('lime', '34.67.169.83'),   # lime.2ravens.org (GCE)
            #('', '104.197.235.238'), # 2ravens.org (GCE)
            #
            ]

COLOR_DOMAIN_PAIRS = DM_COLOR_DOMAIN_PAIRS

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

def check_domains():
    """Check if the domain is set to the expected IP"""
    cnt = 0
    for dcolor, ip_address in COLOR_DOMAIN_PAIRS:
        #print(f'{dcolor}.2ravens.org')
        cnt += 1
        is_domain_set(dcolor, ip_address, cnt=cnt)


if __name__ == '__main__':
    check_domains()
