# This file appends the ONET skills to the skills.csv file from pyresparser

# Set up
import os 
import glob
import pandas as pd 

directory = "C:\Repos\pyresparser\pyresparser"
os.chdir(directory)

# Use glob to match the pattern 'csv'
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Combine all files in the list and export as CSV
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_skills_onet.csv", index=False, encoding='utf-8-sig')