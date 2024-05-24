import requests
from pprint import PrettyPrinter

# disablel warnings about self signed certs
import urllib3
urllib3.disable_warnings()

DEVICE_IPS = ['192.168.0.10',
              '192.168.0.11',
              '192.168.0.12',
              '192.168.0.13',
              '192.168.0.14',
              '192.168.0.15',
              '192.168.0.16',
              '192.168.0.17'
              ]

# Credentials
USERNAME = 'arista'
PASSWORD = 'aristalxpj'

if __name__ == '__main__':
    payload = {'jsonrpc': '2.0',
               'method': 'runCmds',
               'params': {
                 'version': 1,
                 # TODO: Modify the list of commands to run on the switches
                 'cmds': ["show hostname","show version"]
               },
               'id': '1'
              }

    pp = PrettyPrinter()

    # TODO: Add/modify the below code to iterate through all the IPs in the list 'DEVICE_IPS'
    for device in DEVICE_IPS:
        r = requests.post('https://{}:443/command-api'.format(device), json=payload, auth=(USERNAME, PASSWORD), verify=False)
        response = r.json()
        #pp.pprint(responses)
        print(f"{response['result'][0]['fqdn']} is a {response['result'][1]['modelName']} with serial number {response['result'][1]['serialNumber']} and system MAC address {response['result'][1]['hwMacAddress']}")


      


