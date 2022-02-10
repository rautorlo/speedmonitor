import sys
import os
import time

import utils

#Reading from CLI
file_path = ""

if(len(sys.argv)==2):
    file_path = str(sys.argv[1])
else: 
    file_path = ""

if(len(sys.argv)>2):
    print("Invalid arguments")
    utils.print_help()
    exit()


#Preparing date
current_date = time.strftime('%Y-%m-%d')
current_date = current_date.replace("/","-")

#Preparing time
current_time = time.strftime('%X')
current_time = current_time.replace(":","-")

#Preparing log file name
file_name=str(current_date)+"_speedmonitor_"+str(current_time)+".log"

#Preparing OS command
speedcommand = "/usr/bin/speedtest-cli > "+file_path+str(file_name);

#Launching OS command
res = os.system(speedcommand)

if(res==0):
    # We'll obtaing ping, download speed and upload speed 
    # and we'll save the values in TestDone object
    t = utils.get_test_values(""+file_path+str(file_name))

    #Saving values in TestDone object
    t.date = current_date
    t.time = current_time
    t.ObjectPrint()
    print("TEST DONE!")

    #Joining the last test values in speedmonitor.csv
    utils.add_to_main_log(""+file_path+current_date+"_speedmonitor.csv",t)
else:
    print("TEST FAILED!\n")



