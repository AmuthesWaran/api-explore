import requests
import json
import csv

input_file_path = 'input.txt'

with open(input_file_path, 'r') as file:
    lines = file.readlines()

cleaned_line = [line.strip() for line in lines]

print(cleaned_line)
leis_string=','.join(cleaned_line)
print(leis_string)

r = requests.get(
    f'https://api.gleif.org/api/v1/lei-records?filter%5Blei%5D={leis_string}')

print(r)
response = r.content
json_data = json.loads(response)

list_lei = json_data["data"]

file_name = 'output.csv'

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='|')  # Create a CSV writer object
    writer.writerow(['LEI', 'LEGAL_NAME']) # Writing header

    for leis in list_lei:
        writer.writerow([leis["attributes"]["lei"], leis["attributes"]["entity"]["legalName"]["name"]])

