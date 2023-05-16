import csv
import json

json_string = '[{"firstName": "John", "lastName": "Doe", "age": 30, "city": "New York"},  {"firstName": "Jane", "lastName": "Doe", "age": 25, "city": "Chicago"}]'
data = json.loads(json_string)
headers = data[0].keys()

with open('file.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)