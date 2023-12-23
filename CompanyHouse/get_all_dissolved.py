import requests
import json
import csv
import logging
from datetime import datetime

logging.basicConfig(filename='./logs_cono.txt', filemode='a', format='%(asctime)s\t%(msecs)d %(name)s\t%(levelname)s\t%(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
logging.info('start')

get_current_date_and_time=datetime.now()
todays_date_time=get_current_date_and_time.strftime("%d-%m-%Y_%H%M%S")

input_file_path = f'input.txt'
output_file_name = f'./incoming/output/output_{todays_date_time}.csv'
error_log = f'./incoming/error_logs/error_log_{todays_date_time}.csv'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

cleaned_line = [line.strip() for line in lines]

# output file to write dissolved entities
with open(output_file_name, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='|')  # Create a CSV writer object
    writer.writerow(['CompanyNumber','CompanyName','CompanyCategory','CompanyStatus','SicText']) # Writing header
    
    # error_log file
    with open(error_log, mode='w', newline='') as exfile:
        csv_writer = csv.writer(exfile, delimiter='|')
        csv_writer.writerow(['CONO','StatusCode'])
        for cono in cleaned_line:
            logging.info(f'cono {cono}')
            r = requests.get(f'http://data.companieshouse.gov.uk/doc/company/{cono}.json')
            if r.status_code == 200:
                json_data = json.loads(r.content)
                if json_data["primaryTopic"]["CompanyStatus"] == "Dissolved" :
                    writer.writerow([json_data["primaryTopic"]["CompanyNumber"],json_data["primaryTopic"]["CompanyName"],json_data["primaryTopic"]["CompanyCategory"],json_data["primaryTopic"]["CompanyStatus"],json_data["primaryTopic"]["DissolutionDate"]])
            else:
                csv_writer.writerow([cono,r.status_code])

logging.info('end')