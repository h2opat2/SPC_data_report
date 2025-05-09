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
            characteristic = Characteristic(parts[1],  # name
                                            parts[2],  # code
                                            parts[7],  # meas
                                            parts[8],  # nom
                                            parts[9],  # dev
                                            parts[10], # tol upper
                                            parts[11], # tol lower
                                            parts[13]  # error
                                            )

            # add characteristic to characteristics dictionary
            if characteristic.name not in characteristics:
                characteristics[characteristic.name] = []
            characteristics[characteristic.name].append(characteristic)

# get measured values and create measurement list for characteristic
def get_measurements(char_name):
    measurements = []
    for char_item in characteristics[char_name]:
        measurements.append(float(char_item.meas))
    return measurements

# get characteristic properties based on first record
def get_char_properties(char_name):
    char0 = characteristics[char_name][0]
    properties = [
        char0.feature_name,
        char0.char_type,
        char0.nom,
        char0.tol_bottom,
        char0.tol_top]
    return properties

# print out characteristic info
def print_char_info(counter, char_properties, char_measurements):
    print(f"\n{counter:03d})")
    print("Characteristic properties:")
    print(f"{"Name:".ljust(15)}{char_properties[0]}\n"
          f"{"Type:".ljust(15)}{char_properties[1]}\n"
          f"{"Nominal:".ljust(15)}{char_properties[2]}\n"
          f"{"Tolerances:".ljust(15)}{char_properties[3]}, {char_properties[4]}")
    print("Measured values [mm]:")
    print(char_measurements)

# create final output list of characteristic in csv format
def create_output_data_list():
    csv_data = []
    counter=1
    for char in characteristics:

        char_output = get_char_properties(char)
        char_measurements = get_measurements(char)

        print_char_info(counter, char_output, char_measurements)

        char_measurements_str = [str(x) for x in char_measurements]
        char_output.extend(char_measurements_str)

        csv_data.append(char_output)
        counter+=1

    return csv_data

output = create_output_data_list()


