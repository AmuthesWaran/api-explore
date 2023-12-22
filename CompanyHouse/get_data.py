import requests



r = requests.get('http://data.companieshouse.gov.uk/doc/company/12345678.csv')

print(r.status_code)
print(r.content)
json_data = r.json()
print(json_data["primaryTopic"]["CompanyName"])
