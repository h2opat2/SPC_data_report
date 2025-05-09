
class CharacteristicRecord:
    char_type_dict ={
        "01": "X",
        "02": "Y",
        "03": "Z",
        "04": "Diameter",
        "05": "Radius",
        "06": "Angle",
        "07": "Length",
        "08": "Width",
        "09": "Point-Profile",
        "10": "TruePosition-Radius",
        "11": "TruePosition-Angle",
        "12": "Roundness",
        "13": "Flatness",
        "14": "Straightness",
        "15": "X.D.Cosine",
        "16": "Y.D.Cosine",
        "17": "Z.D.Cosine",
        "18": "Laser",
        "19": "Inc.Angle",
        "20": "Straight_P",
        "21": "Straight_D",
        "22": "Straight_X",
        "23": "Straight_Y",
        "24": "Straight_Z",
        "25": "Parallel",
        "26": "Parallel_P",
        "27": "Parallel_D",
        "28": "Parallel_X",
        "29": "Parallel_Y",
        "30": "Parallel_Z",
        "31": "Square",
        "32": "Square_P",
        "33": "Square_D",
        "34": "Square_X",
        "35": "Square_Y",
        "36": "Square_Z",
        "37": "Angular",
        "38": "Angular_P",
        "39": "Angular_D",
        "40": "Concentric",
        "41": "TruePosition-Diameter",
        "42": "Cylindric",
        "43": "Max-Diam",
        "44": "Min-Diam",
        "50": "Position2D",
        "51": "Position3D",
        "52": "Line-Profile",
        "60": "Distance-P2P"
    }

    def __init__(self, name_feature, code, meas, nom, dev, tol_top, tol_bottom, error):
        self.feature_name = name_feature
        self.code = code
        self.char_type = self.get_char_type()
        self.name = name_feature + " " + self.char_type
        self.nom = nom
        self.meas = meas
        self.dev = dev
        self.tol_top = tol_top
        self.tol_bottom = tol_bottom
        self.error = error

    def __str__(self):
        return f"{self.name}, {self.nom}, {self.meas}, {self.dev}, Is OK: {str(not float(self.error)>0.0)}"

    def get_char_type(self):
        return self.char_type_dict[self.code]
