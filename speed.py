
import os
import time
import sys

#def: __init__()

durrent_date = time.strftime('%x')
durrent_date = durrent_date.replace("/","-")
current_time = time.strftime('%X')
current_time = current_time.replace(":","-")


file_name=str(durrent_date)+"_speedmonitor_"+str(current_time)+".log"

speedcommand = "speedtest > "+str(file_name);

res = os.system(speedcommand)
#the method returns the exit status
