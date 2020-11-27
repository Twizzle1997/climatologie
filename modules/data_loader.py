import os
from os import path, listdir, getcwd, makedirs

import csv
# import requests
import sys
# import zipfile

# import pandas as pd

DATA_PATH = 'data/'
DATASET_PATH = DATA_PATH + 'filtered_temperatures.csv'
CURATED_LOCAL_PATH = DATA_PATH + 'curated/'
COUNTRY = 'country/'



class DataSpliter:

    def split_data_country(self):
        '''
        Break raw data into many files
        '''

        with open(DATASET_PATH, encoding='utf-8') as file_stream:    
            file_stream_reader = csv.DictReader(file_stream, delimiter=',')
            
            open_files_references = {}

            for row in file_stream_reader:
                country = row['Country']
                # Open a new file and write the header
                if path.exists(CURATED_LOCAL_PATH + COUNTRY) == False:
                    try:
                        os.makedirs(CURATED_LOCAL_PATH + COUNTRY)
                    except OSError:
                        print ("Creation of the directory %s failed" % path)
                        exit(1)

                if country not in open_files_references:
                    output_file = open(CURATED_LOCAL_PATH + COUNTRY +'{}.csv'.format(country), 'w', encoding='utf-8', newline='')
                    dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                    dictionary_writer.writeheader()
                    open_files_references[country] = output_file, dictionary_writer
                # Always write the row
                open_files_references[country][1].writerow(row)
            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()



