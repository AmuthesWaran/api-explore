import requests
import json
import csv
import logging

logging.basicConfig(filename='./logs_cono.txt', filemode='a', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
logging.info('start')

# input file must contain only cono in a single column
input_file_path = 'input.txt'
output_file_path = 'output.csv'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

cleaned_line = [line.strip() for line in lines]

# print(cleaned_line)
# print(type(cleaned_line))

file_name = 'output.csv'

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='|')  # Create a CSV writer object
    writer.writerow(['CompanyNumber','CompanyName','CompanyCategory','CompanyStatus','SicText']) # Writing header

    for cono in cleaned_line:
        logging.info(f'cono {cono}')
        r = requests.get(f'http://data.companieshouse.gov.uk/doc/company/{cono}.json')
        json_data = json.loads(r.content)
        # print(type(json_data))
        # print(json_data["primaryTopic"]["CompanyNumber"],json_data["primaryTopic"]["CompanyName"],json_data["primaryTopic"]["CompanyCategory"],json_data["primaryTopic"]["CompanyStatus"],json_data["primaryTopic"]["SICCodes"]["SicText"])
        writer.writerow([json_data["primaryTopic"]["CompanyNumber"],json_data["primaryTopic"]["CompanyName"],json_data["primaryTopic"]["CompanyCategory"],json_data["primaryTopic"]["CompanyStatus"],json_data["primaryTopic"]["SICCodes"]["SicText"]])

logging.info('end')