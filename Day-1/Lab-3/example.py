import requests
from jinja2 import Environment, FileSystemLoader
from pprint import PrettyPrinter

#disable self-signed certs
import urllib3
urllib3.disable_warnings()

CVP_IP = "192.168.0.5"

# Credentials
USERNAME = 'arista'
PASSWORD = 'aristavmnt'

if __name__ == '__main__':
    pp =PrettyPrinter()
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("example.j2")

    with open('token.tok') as infile:
        access_token = infile.read()

    s = requests.session()
    s.verify = False
    s.cookies.set("access_token", access_token)

    images = {}
    containers = {}

    # Get images list
    r = s.get('https://{}/cvpservice/image/getImages.do?startIndex=0&endIndex=0'.format(CVP_IP))
    response_images = r.json()

    #pp.pprint(response_images)

    # Get containers in CVP
    r = s.get('https://{}/cvpservice/inventory/containers'.format(CVP_IP))
    responses_containers = r.json()

    #pp.pprint(responses_containers)

    images = response_images['data']
    containers = responses_containers

    #print(images)

    #print(containers)

    # Pass the data you collected above to the jinja tempalte
    print(template.render(images=images, containers=containers))