import os
import re
from Characteristic import Characteristic


# Reading measurement report files
data_folder = "Data"
report_list_all = os.listdir(data_folder)

# get only DTA files
report_list = []
for file in report_list_all:
    if os.path.isfile(os.path.join(data_folder, file)) and file.endswith(".dta"):
        report_list.append(file)

characteristics = {}

# read files
for file in report_list:
    with open(os.path.join(data_folder, file), "r") as f:
        for row in f:
            parts = re.split(r'\s+', row.strip())
            characteristic = Characteristic(parts[1],
                                            parts[2],
                                            parts[7],
                                            parts[8],
                                            parts[9],
                                            parts[10],
                                            parts[11],
                                            parts[13]
                                            )

            # add characteristic to characteristics dictionary
            if characteristic.name not in characteristics:
                characteristics[characteristic.name] = []
            characteristics[characteristic.name].append(characteristic)

for name, items in characteristics.items():
    print(f"{name}:")
    for item in items:
        print(f"  - {item}")
