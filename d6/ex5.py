# import os
#
# p = '/Users/valeria/src/evening-ninjas/lesson12'
# d = {}
# initial_depth = p.count(os.path.sep)+1
# for root, folders, files in os.walk(p):
#     print(root, folders, files)
#     curr_depth = root.count(os.path.sep)+1 - initial_depth
#     #/Users/valeria/src/evening-ninjas/lesson12/files/data
#     #curr depth - 2
#     keys_list = root.split('/')[:-curr_depth] # [files, data]
#     curr_dict = d
#     for k in keys_list:
#         curr_dict = curr_dict[k]
#     curr_dict['dirs'].update(folders)
import csv
import json


def json2csv(json_filepath: str, csv_filepath: str):
    with open(json_filepath, 'r') as f:
        my_json = json.load(f)
    headers = my_json[0]
    with open(csv_filepath, 'w') as f:
        my_csv = csv.DictWriter(f, fieldnames=headers)
        my_csv.writeheader()
        my_csv.writerows(my_json)

if __name__ == '__main__':
    json2csv('/Users/valeria/Downloads/username2.json', 't.csv')
