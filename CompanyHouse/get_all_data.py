import requests
import json

r = requests.get('http://data.companieshouse.gov.uk/doc/company/12345678.json')

# print(r.content)

json_data = json.loads(r.content)

print(type(json_data))

print(json_data["primaryTopic"]["CompanyName"])