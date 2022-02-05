from os.path import exists
import csv
from TestDone import TestDone

# ==========================================
# HELP PRINTER
# ==========================================
# This function prints the rule to call 
# speed.py

def print_help():
    print("python3 speed.py <log file path>")
    print("if any log file path is introduced a \".\" path will be used")

#TODO: IMPLEMENT THE FUNCTION
def path_check(file_path):
    return

# ==========================================
# GET TEST VALUES
# ==========================================
# This function reads the current speedtest
# file and obtain the speed values.
# @param current_file_log --> file name
# @return test --> TestDone object with
# the test values added.

def get_test_values(current_file_log):
    #
    current_file = open(current_file_log, "r+")

    test = TestDone()

    line_hosted     = ""
    line_download   = ""
    line_upload     = ""

    for line in current_file:
        if("Hosted") in line:
            line_hosted     = line;
        if("Download") in line:
            line_download   = line
        if("Upload") in line:
            line_upload     = line

    line_hosted         = line_hosted.split(" ")
    line_download       = line_download.split(" ")
    line_upload         = line_upload.split(" ")

    test.ping           = line_hosted[len(line_hosted)-2]
    test.speed_download = line_download[len(line_download)-2]
    test.speed_upload   = line_upload[len(line_upload)-2]

    return test


# ==========================================
# ADD TO MAIN LOG
# ==========================================
# This function add the new test values to
# the general log file if it exists
# if the general log does'nt exist
# the function creates a new one
# @param genera_file log -> general file log
# name
# @param test -> test object to be added

def add_to_main_log(general_file_log, test):
    #Defining and preparing variables
    file_name = str(general_file_log)
    fields = ['Date','Time','Ping(ms)','Download speed(Mbit/s)', 'Upload speed(Mbit/s)']
    row = [test.date,test.time,test.ping,test.speed_download,test.speed_upload]
    general_log_writer = ""

    #Checking if the general file exists
    file_exists = exists(general_file_log)

    if(file_exists):
        #if it exists we append a new row
        with open(file_name, 'a') as csvfile:
            # creating a csv reader object
            general_log_writer = csv.writer(csvfile)
            print("File: "+file_name+" exists\n")
            general_log_writer.writerow(row)
    else:
        #if it does'nt exist we create a new one and add the values obtained in the test
        with open(file_name, 'w') as csvfile:
            # creating a csv reader object
            general_log_writer = csv.writer(csvfile)
            print("File: "+file_name+" doesn't exist")
            print("File: "+file_name+" created\n")
            general_log_writer.writerow(fields)
            general_log_writer.writerow(row)

    return