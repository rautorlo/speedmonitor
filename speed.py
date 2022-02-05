
import os
import time

from TestDone import TestDone
import utils

#Preparing test
test = TestDone()

#Preparing date
current_date = time.strftime('%Y-%m-%d')
current_date = current_date.replace("/","-")

#Preparing time
current_time = time.strftime('%X')
current_time = current_time.replace(":","-")

#Preparing log file name
file_name=str(current_date)+"_speedmonitor_"+str(current_time)+".log"

#Preparing OS command
speedcommand = "speedtest > "+str(file_name);

#Launching OS command
res = os.system(speedcommand)

if(res==0):
    #Now a log file should be crated.

    #We'll obtaing ping, download speed and upload speed
    t = utils.get_test_values(file_name)

    print("TEST DONE!\n")
    t.date = current_date
    t.time = current_time
    t.ObjectPrint()

    utils.add_to_main_log("speedmonitor.csv",t)
else:
    print("TEST FAILED!\n")


