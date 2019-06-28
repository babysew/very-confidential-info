import os
import glob
import pandas as pd


os.chdir('C:\\Tushar\\notebookk\\new outputs\\27_06')

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

#export to csv
combined_csv.to_csv( 'combined_csv.csv', index=False, encoding='utf-8-sig')



import os
import glob
import pandas as pd


path = r'C:\Tushar\notebookk\new outputs\27_06'                    
all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f, index_col=None, header=None) for f in all_files)
concatenated_df = pd.concat(df_from_each_file, ignore_index=True, sort=False)
concatenated_df