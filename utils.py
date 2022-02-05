import csv
from TestDone import TestDone

# ==========================================
# ADD TO MAIN LOG
# ==========================================


def add_to_main_log(general_file_log, test):
    file_name = str(general_file_log)
    fields = ["Date","Time","Ping(ms)","Download speed(Mbit/s)", "Upload speed(Mbit/s)"]
    row = [test.date,test.time,test.ping,test.speed_download,test.speed_upload]
    general_log_reader = ""
    general_log_writer = ""

    try:
        with open(file_name, 'r') as csvfile:
            # creating a csv reader object
            general_log_reader = csv.reader(csvfile)
            print("File: "+file_name+" doesn't exist")
    except:
        with open(file_name, 'w') as csvfile:
            # creating a csv reader object
            general_log_writer = csv.writer(csvfile)
            print("File: "+file_name+" exists")

    general_log_writer.writerow(fields)
    general_log_writer.writerow(row)

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

    line_hosted = ""
    line_download = ""
    line_upload = ""

    for line in current_file:
        if("Hosted") in line:
            line_hosted = line;
        if("Download") in line:
            line_download = line
        if("Upload") in line:
            line_upload = line

    line_hosted = line_hosted.split(" ")
    line_download = line_download.split(" ")
    line_upload = line_upload.split(" ")

    test.ping           = line_hosted[len(line_hosted)-2]
    test.speed_download = line_download[len(line_download)-2]
    test.speed_upload   = line_upload[len(line_upload)-2]

    return test
