import numpy as np
import time
import sys
import socket
import pandas as pd
from sys import argv

'''
pandas is a Data Analysis Library, helps to parse our csv file
'''


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_ip = '172.18.1.1'
udp_port = 8088

#the current column/building we are reading from data
try:
	bld_id = int(sys.argv[1])
	#print("building id: " + str(bld_id))

except IndexError:
	#if cmd line is "python messenger.py" instead of 
	#		"python messenger.py <bld_id>"
	print("Please specify a building id")
	exit(1)


data_col = pd.read_csv("./data.csv",header=None, usecols=[bld_id,])


# NOTE: when dealing with real-time data, this will have to be parsed
# differently (while True)
for idx,msg in data_col.iterrows():
	print(msg.item())
	sock.sendto(str(msg.item()), (udp_ip,udp_port))
	#print(str(msg))
	time.sleep(.05)



