import json
import csv







def load():
    
with open('file.json', 'r') as List:
    file = json.load(List) 
    headers = file[0].keys()

with open('file.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
    
def main():
    pass

if __name__ == "__main__":
    main()