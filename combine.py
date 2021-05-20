import os
import glob
import pandas as pd

os.chdir("./NAVAXNO_CSV/1")
# os.chdir("./test")
filter = open("filter.txt").read().splitlines()

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f, delimiter=';') for f in all_filenames])
combined_csv.drop(combined_csv.columns.difference(filter), 1, inplace=True)
filter.pop(0)
combined_csv.dropna(axis=0, how='all', subset=filter, inplace=True)
# combined_csv.drop(combined_csv[combined_csv['SI-17105R/ANA.QOUT'] < 100.00].index, inplace=True)
combined_csv.query('`SI-17105R/ANA.QOUT` > 100', inplace=True)
combined_csv.to_csv("filtered_NaN_timestamp_100RPM_csv1.csv", index=False, encoding='utf-8-sig')