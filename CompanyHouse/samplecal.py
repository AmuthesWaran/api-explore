import requests
import json
from pprint import pprint

r = requests.get('https://data.companieshouse.gov.uk/doc/company/13970990.json')
json_data = json.loads(r.content)
pprint(json_data)