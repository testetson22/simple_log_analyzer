import csv, sys
from typing import List

args = sys.argv[1:]
file_name = str(args[0])
error_col = int(args[1])
filename_col = int(args[2])

error_file_names: List[str] = []

with open(file_name, 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for row in reader:
        if row[error_col] == "ERROR":
            error_file_names.append(str(row[filename_col]))

file_count_dict = {}
for file_name in error_file_names:
    if not file_name in file_count_dict:
        file_count_dict[file_name] = 1
    else:
        file_count_dict[file_name] += 1
        
for k, v in file_count_dict.items():
    print(f'{k} {v}')
