__author__ = 'tkraus-m, Olli'
__credits__ = ['tkraus-m', 'https://github.com/tkrausjr/dcos-python']
__version__ = '0.0.1'
__maintainer__ = 'Olli'
__email__ = 'olli@csow.de'
__status__ = 'Development'

from modules import dcos
from prettytable import PrettyTable


import json


with open('config.json','r') as f:
    dcos_config = json.load(f)



dcos_master = dcos_config['TRU']['dcos_master']
userid = dcos_config['TRU']['dcos_userid']
password = dcos_config['TRU']['dcos_password']
'''
dcos_master = 'https://1.2.3.4'
userid = input('Enter the username for the DCOS cluster '+dcos_master +' : ')
password = input('Enter the password for the DCOS cluster '+dcos_master +' : ')
'''
## marathon_app_json = '/Users/tkraus/sandbox/marathon/12b-siege.json'

## Login to DCOS to retrieve an API TOKEN
dcos_token = dcos.dcos_auth_login(dcos_master,userid,password)
if dcos_token != '':
    print('{}{}'.format("DCOS TOKEN = ", dcos_token))
else:
    exit(1)
print('-----------------------------')



## Initialize new Marathon Instance of Marathon Class
new_marathon = dcos.marathon(dcos_master,dcos_token)

## List Marathon Apps Method
marathon_apps = new_marathon.get_all_apps()
print ("The following apps exist in Marathon...", marathon_apps)
print('-----------------------------')

# Create ascii table
apptable = PrettyTable(["App","Tasks", "Health"])
#apptable.field_names = ["App","Tasks", "Health"]

## Get Marathon App Details Method - List Tasks & Agents for all Marathon Apps
if marathon_apps != None:
    for app in marathon_apps:
        ####app_details = new_marathon.get_app_details(app)
        app_status = new_marathon.get_task_status(app)
        
        try:
            #print (app_status['tasks'])
            apptable.add_row([app,app_status['tasks'],"X"])
        except TypeError:
            #print ("Keine Tasks")
            apptable.add_row([app,0,"X"])

        
        
        
        ####print('{}{}'.format("Marathon App details = ", app_details))
        ####print('-----------------------------')
        print(app_status)
    apptable.align["App"] = "l"
    print(apptable)
        




## new_app = new_marathon.add_app(marathon_app_json)
## print('Marathon App ID is ' + new_app)

