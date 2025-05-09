import os
import re

from CharacteristicRecord import CharacteristicRecord
from Characteristic import Characteristic

characteristics = {}
measurement_count = 0

# Create characteristic dictionary from report files
def read_data(folder_name):

    # Reading measurement report files
    report_list_all = os.listdir(folder_name)

    # get only DTA files
    report_list = []
    for file in report_list_all:
        if os.path.isfile(os.path.join(folder_name, file)) and file.endswith(".dta"):
            report_list.append(file)

    global measurement_count
    measurement_count = len(report_list)

    # read files
    for file in report_list:
        with open(os.path.join(folder_name, file), "r") as f:
            for row in f:
                parts = re.split(r'\s+', row.strip())
                characteristic_record = CharacteristicRecord(parts[1],  # name
                                                parts[2],  # code
                                                parts[7],  # meas
                                                parts[8],  # nom
                                                parts[9],  # dev
                                                parts[10], # tol upper
                                                parts[11], # tol lower
                                                parts[13]  # error
                                                )

                # add characteristic to characteristics dictionary
                if characteristic_record.name not in characteristics:
                    characteristics[characteristic_record.name] = Characteristic(characteristic_record)
                characteristics[characteristic_record.name].insert_measurement(float(characteristic_record.meas))

# print out characteristic info
def print_char_info(counter, char):

    print(f"\n" + "_" * 50)
    print(f"{counter:03d})")

    print("Characteristic properties:")
    print(f"{"Name:".ljust(15)}{char.feature_name}\n"
          f"{"Type:".ljust(15)}{char.char_type}\n"
          f"{"Nominal:".ljust(15)}{char.nom}\n"
          f"{"Tolerances:".ljust(15)}{char.tol_bottom}, {char.tol_top}\n")
    print("Measured values [mm]:")
    print(char.meas)
    print("\nStatistics [mm]:")
    print(f"Mean: {char.mean:.4f}")
    print(f"Standard deviation: {char.std:.4f}")
    print(f"Min. value: {char.min:.4f}")
    print(f"Max. value: {char.max:.4f}")
    print(f"Range: {char.range:.4f}")
    print(f"Status: {char.status}")


# create final output list of characteristic in csv format
def create_output_data_list():
    # header of CSV
    meas_header = []
    for i in range(measurement_count):
        meas_header.append(f"Meas {i+1:02d}")
    header = [
        "Name",
        "Type",
        "Nominal",
        "Low tolerance",
        "High tolerance",
        ",".join(meas_header),
        "Mean",
        "Standard deviation",
        "Min value",
        "Max value",
        "Range",
        "Status"
    ]

    csv_data = [",".join(header)]

    # one row per characteristic
    counter=1
    for key in characteristics:

        char = characteristics[key]

        # compute statistics of characteristic
        char.compute_statistics()

        # append row to csv output list
        csv_data.append(char.csv_format())

        print_char_info(counter, char)

        counter += 1

    return csv_data

# write csv file into specified directory
def write_to_file(folder_name, csv_data):
    with open(os.path.join(folder_name, "report.csv"), "w") as f:
        for row in csv_data:
            f.write(row + "\n")

# running program
read_data("Data")
output = create_output_data_list()

write_to_file("Data", output)






