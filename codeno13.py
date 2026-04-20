import csv
import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('data.csv', 'w', newline='') as csv_file:
    if isinstance(data, list):
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    else:
        fieldnames = data.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)

print("JSON data successfully converted to CSV.")