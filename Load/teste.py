import json
import csv
import os


def input_path():
    print ("Put the path of the .Json file. Ex: C:/files/name.json")
    load = input ("Json path: ")
    if os.path.exists(load):   #Verify if is getting a existing file
        print ("Choose where the .csv will be create. Ex: C:/files/name.csv")
        save = input ("CSV path: ")
        return (load, save)
    else:
        print ("File not found")
        return input_path()
    
def VerifyJson(file):
    try:
        file
    except ValueError as err:
        if True :
            print ("File corrupt ou invalid")
            return input_path()
        
    
    
   
def load_transform_save(path_to_json_file, path_to_csv_file):

    with open(path_to_json_file, 'r') as List:
        file = json.loads(List)
        headers = file[0].keys()

    with open(path_to_csv_file, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(file)

def main():
   Path = input_path()
   load_transform_save(Path[0], Path[1])
   
if __name__ == "__main__":
    main()