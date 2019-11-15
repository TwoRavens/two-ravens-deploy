"""List of colors / IPs for domains"""
import socket

COLOR_DOMAIN_PAIRS = [\
            ('apricot', '35.193.191.129'),
            ('black', '35.232.106.12'),
            ('blue', '35.225.184.21'),
            ('brown', '35.188.19.147'),
            ('cyan', '104.154.189.22'),
            ('green', '34.69.233.100'),
            ('grey', '35.192.115.217'),
            ('lavender', '35.202.146.137'),
            ('lime', '34.67.169.83'),
            ('magneta', '35.232.230.212'),
            #
            ('maroon', '35.224.8.63'),
            ('mint', '35.193.94.42'),
            ('navy', '35.225.211.121'),
            ('olive', '35.232.25.205'),
            ('orange', '35.238.5.40'),
            ('pink', '35.224.169.201'),
            ('purple', '34.67.168.183'),
            ('red', '35.224.128.61'),
            ('white', '35.223.181.244'),
            ('yellow', '34.66.28.61'),
            #
            ('terra', '35.222.64.114'),
            #
            ('', '104.197.235.238'), # 2ravens.org
            ]

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
