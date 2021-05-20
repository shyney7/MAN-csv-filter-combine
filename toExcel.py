import pandas as pd
import os
from glob import glob
import traceback

# readFile = pd.read_csv("filtered_timestamp_combined_csv.csv", nrows= 20)
# readFile.to_excel("filtered_timestamp_combined.xlsx", index= None, header=True)

""" PATH = "./DONAXNO_CSV" """
EXT = "*.csv"
""" csvFilesDonaxno = [file 
            for path, subdir, files in os.walk(PATH)
            for file in glob(os.path.join(path, EXT))]
# print(csvFilesDonaxno) """

PATH = "./split2excel"

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
        readFile = pd.read_csv(csv)
    except Exception:
        traceback.print_exc()
    try:
        readFile.to_excel("./split_XLSX\\" + os.path.basename(csv) + ".xlsx", index= None, header=True)
    except Exception:
        traceback.print_exc()

