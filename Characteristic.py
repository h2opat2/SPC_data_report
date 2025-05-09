import statistics

class Characteristic:

    def __init__(self,characteristic_record):
        self.feature_name = characteristic_record.feature_name
        self.char_type = characteristic_record.char_type
        self.nom = float(characteristic_record.nom)
        self.tol_top = float(characteristic_record.tol_top)
        self.tol_bottom = float(characteristic_record.tol_bottom)
        self.meas = []
        self.mean = None
        self.std = None
        self.max = None
        self.min = None
        self.range = None
        self.status = None
        self.in_tol = None


    def __str__(self):
        return f"{self.feature_name}, {self.char_type}, {self.nom}, {self.tol_bottom}, {self.tol_top},  {self.meas}"


    def insert_measurement(self,value):
        self.meas.append(value)

    def compute_statistics(self):
        self.mean = statistics.mean(self.meas)
        self.std = statistics.stdev(self.meas)
        self.max = max(self.meas)
        self.min = min(self.meas)
        self.range = abs(self.max - self.min)

        upper_value = self.nom + self.tol_top
        lower_value = self.nom + self.tol_bottom
        self.in_tol = [value for value in self.meas if lower_value <= value <= upper_value]
        out_tol = [value for value in self.meas if value < lower_value or value > upper_value]

        if len(out_tol) > 0:
            self.status = f"Failed - {len(self.in_tol)}/{len(self.meas)} OK = {len(self.in_tol)/len(self.meas)*100:.0f} %"
        else:
            self.status = f"Successful measurement! - {len(self.in_tol)}/{len(self.meas)} OK = {len(self.in_tol)/len(self.meas)*100:.0f} %"

    def csv_format(self):
        str_measurements = ",".join([f"{x:.4f}" for x in self.meas])
        row = [
            self.feature_name,
            self.char_type,
            f"{self.nom:.4f}",
            f"{self.tol_bottom:.4f}",
            f"{self.tol_top:.4f}",
            str_measurements,
            f"{self.mean:.4f}",
            f"{self.std:.4f}",
            f"{self.max:.4f}",
            f"{self.min:.4f}",
            f"{self.range:.4f}",
            f"{(len(self.in_tol) / len(self.meas) * 100):.0f}"
        ]
        return ",".join(row)

