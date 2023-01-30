import csv
import json


def csv2json(csv_path: str, json_path: str):
    objects = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row_dict in reader:
            for k, v in row_dict.items():
                if v.isdigit():
                    row_dict[k] = int(v)
                elif v.count(".") == 1 and v.replace(".", "").isdigit():
                    row_dict[k] = float(v)
                objects.append(row_dict)
    with open(json_path, 'w') as f:
        json.dump(objects, f)


# def csv2json(csv_path: str, json_path: str):
#
#     with open(csv_path) as f:
#         reader = csv.DictReader(f)
#         objects = list(reader)
#     with open(json_path, 'w') as f:
#         json.dump(objects, f)


# def csv2json(csv_path: str, json_path: str):
#     with open(csv_path) as f:
#         reader = csv.DictReader(f)
#         with open(json_path, 'w') as f1:
#             json.dump(list(reader), f1)



if __name__ == '__main__':
    csv_path = "/Users/valeria/src/evening-ninjas/lesson12/files/data/AAPL.csv"
    csv2json(csv_path, "aapl.json")