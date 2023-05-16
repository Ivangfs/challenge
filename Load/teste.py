import json
import csv

def Verify ():
    load = input ("Coloque o endereço:")
    save = input ("Coloque o endereço:")
    return (load, save)

def transform(file_to_trasform):

    lista_header = set()
    for i in file_to_trasform:
        lista_prov = list(i.keys())
        lista_header.update(lista_prov)
    return list(lista_header)

def load_transform_save(path_to_json_file, func, path_to_csv_file):

    with open(path_to_json_file) as file:
        file_load = json.load(file)
        headers = func(file_load)
    with open(path_to_csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for row in file_load:
            writer.writerow(row)
            
def main():

    respostas = Verify()
    load_transform_save(respostas[0], transform, respostas[1])


if __name__ == "__main__":
    main()