import re
import os
import subprocess
# Get list of all servers avaiable at Speedtest.net
os.system("../speedtest.py --list > serverData.txt")
id_list = []
regCount = 10
fi = open("serverData.txt", "r")
fo = open("serverData.csv","w")
fo.write("ServerID,Location,Distance")
# Extract ServerID, Location and Distance from server list data
for line in fi:
	server_id = re.findall('(\d+)\)',line)
	location = re.findall('(\w+, \w+)',line)
	distance = re.findall('(\d+.\d+) km',line)
	if (len(server_id)==1 & len(location)==1 & len(distance)==1) :
		id_list.append(server_id[0])
		fo.write("%s,%s,%s\n" % (server_id[0], location[0], distance[0]) ) 
fi.close()
fo.close()
fo1 = open("results.csv","w")
# Get header from running speedtest-cli command
temp = subprocess.Popen(["../speedtest.py","--csv-header"],stdout=subprocess.PIPE ).communicate()[0]
fo1.write(temp)
fo1.write("\n")
print len(id_list)
# Run speedtest for each server 10 times and write output to csv file
for i in range(0,regCount):
	for test_id in id_list:
		data = subprocess.Popen(["../speedtest.py","--csv","--server",test_id],stdout=subprocess.PIPE ).communicate()[0]
		fo1.write(data)
fo1.close()
