import time
from time import gmtime, strftime


hosts_path = '/etc/hosts'
redirect_address = '127.0.0.1'
websites_blocked = ['heise.de', 'zeit.de']




#print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
#print(strftime("%M", gmtime()))
while True:
    if strftime("%M", gmtime()) < '59':
        with open('hosts', 'r+') as hosts:
            data = hosts.read()
            if all(list(map(lambda x: True if x in data else False, websites_blocked))):
                print('all in')
            else:
                print('write it in')
                for i in websites_blocked:
                    hosts.write(i)
        #print('Work Work Work')
    else:
        print('Happy Hour')
    time.sleep(5)
