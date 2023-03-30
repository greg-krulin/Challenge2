# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(list_a, csvpath):
    """
    Saves a list to a CSV file from path provided. If path is not a csv.file, function will create one when
    it starts to write.

    Args:
    list_a: A list of any objects
    csvpath: A path for the CSV file which will have list written on it

    Returns:
    Doesn't return anything, just let user knows that csv file has been saved.
    
    
    
    """
    #Uses function open from csv import to open the csv file, write on file, and let program know it is a csv file. 
    #If the file does not exist it will be created.
    with open(csvpath, 'w', newline = '') as csvfile:

        csvwriter = csv.writer(csvfile) #Calls writer function.

        #Assigns header as a list of strings which will be our header for the csv file.
        header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit Score', 'Interest Rate']

        #Writes header values before filling in values from qualifying loans.
        csvwriter.writerow(header)

        #Goes through list provider by user and writes each entry into csv file.
        for a in list_a:
            csvwriter.writerow(a)

    print("Finished saving to a CSV.")
