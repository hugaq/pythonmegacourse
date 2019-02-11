import time
from time import gmtime, strftime


hosts_path = '/etc/hosts'
redirect_address = '127.0.0.1'
websites_blocked = ['heise.de', 'zeit.de']
default = '''#Sample for hosts file

127.0.0.1	localhost
127.0.1.1	denkpolster-pc
::1	localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters'''


while True:
    if strftime("%M", gmtime()) < '57':
        with open('hosts', 'r+') as hosts:
            data = hosts.read()
            if not all(list(map(lambda x: True if x in data else False, websites_blocked))):
                print('write it in')
                for i in websites_blocked:
                    hosts.write(' '.join([redirect_address,i,'\n']))
            else:
                print('all in')
    else:
        if any(list(map(lambda x: True if x in data else False, websites_blocked))):
            print('Happy Hour')
            with open('hosts', 'w') as hosts:
                hosts.write(default)
    time.sleep(5)
