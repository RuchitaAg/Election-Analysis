import csv
from fileinput import close
import os

# create a path to read the CSV file
file_to_load = os.path.join('Resources','election_results.csv')

# create a file to save the election analysis
file_to_save = os.path.join("analysis","election_results.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# To print rows from the CSV file
    #for row in (file_reader):
        #print(row)

# Print header
    header = next(file_reader)
    print(header)

# Input name of the counties in text file
#with open(file_to_save,"w") as txt_file:
    #txt_file.write("Name of Counties:")
    #txt_file.write("\n-------------------")
    #txt_file.write("\nArapahaoe\nDenver\nJefferson")

#txt_file.close
