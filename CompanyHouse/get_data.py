import requests



r = requests.get('http://data.companieshouse.gov.uk/doc/company/12345678.csv')

print(r.content)