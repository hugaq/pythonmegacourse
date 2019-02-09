import time
from time import gmtime, strftime


hosts_path = '/etc/hosts'
redirect_address = '127.0.0.1'
websites_blocked = ['heise.de', 'zeit.de']




print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print(strftime("%M", gmtime()))
