import traceback
import pandas as pd
import os
from glob import glob
import traceback

""" PATH = "./DONAXNO_CSV" """
EXT = "*.csv"
""" csvFilesDonaxno = [file 
            for path, subdir, files in os.walk(PATH)
            for file in glob(os.path.join(path, EXT))]
# print(csvFilesDonaxno) """

PATH = "./NAVAXNO_CSV"

csvFilesNavaxno = [file 
            for path, subdir, files in os.walk(PATH)
            for file in glob(os.path.join(path, EXT))]
# print(csvFilesNavaxno)

""" for csv in csvFilesDonaxno:
    try:
        readFile = pd.read_csv(csv, delimiter=';')
    except Exception:
        traceback.print_exc()
    try:
        readFile.to_excel("./DONAXNO_XLSX\\" + os.path.basename(csv) + ".xlsx", index= None, header=True)
    except Exception:
        traceback.print_exc() """

# print("./DONAXNO_XLSX\\" + os.path.basename(csvFilesDonaxno[0]) + ".xlsx")

for csv in csvFilesNavaxno:
    try:
        readFile = pd.read_csv(csv, delimiter=';')
    except Exception:
        traceback.print_exc()
    try:
        readFile.to_excel("./NAVAXNO_XLSX\\" + os.path.basename(csv) + ".xlsx", index= None, header=True)
    except Exception:
        traceback.print_exc()

