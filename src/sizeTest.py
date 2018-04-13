import os
import subprocess
preDomain = "ftp://"
baseDomain = ".tele2.net/"
serverList = ["wen1-speedtest-1","zgb-speedtest-1","bks-speedtest-1","vln038-speedtest-1","ams-speedtest-1","bck-speedtest-1","nyc9-speedtest-1","kst5-speedtest-1"]
sizeList = ["1KB","512KB","1MB","2MB","3MB","5MB","10MB","50MB","100MB","200MB","500MB","1GB","10GB","100GB","1000GB"]
fileType = ".zip"
uploadDirectory = "upload/"
fo = open("sizeResults.cvs","w")
foPing = open("pingResults.txt","w")
'''
Steps followed while running all tests
	1. Ping server 
	2. Curl for download
	3. Extract download speed
	4. Curl for upload
	5. Extract upload speed
	6. Write to file both speeds
'''
#Function to write to file
def curlOutToFile(server_name, size, up_down, curlOut):
	if up_down is "Download":
		speed = curlOut.split("\n")[2].split()[-6]
		time = curlOut.split("\n")[2].split()[-3]
	else:
		speed = curlOut.split("\n")[2].split()[-5]
		time = curlOut.split("\n")[2].split()[-3]
	speed = speed.replace("k","000")
	speed = speed.replace("M","000")	
	size = size.replace("KB","000")
	size = size.replace("MB","000000")
	size = size.replace("GB","000000000")
	print (server_name+","+size+","+up_down+","+speed+","+time)
	fo.write(server_name+","+size+","+up_down+","+speed+","+time+"\n")
#Function to curl files from url
def curlData(server_name):
	rawUrl = server_name + baseDomain
	for size in sizeList[:-3]:
		url = preDomain + rawUrl + size + fileType
		#curlCmd = "curl -o /dev/null "+url
		curlCmd = "curl -o ./temp "+url
		upUrl = preDomain + rawUrl + uploadDirectory 
		upcurlCmd = "curl -T ./temp "+upUrl
		try:
			curlOut =  subprocess.Popen(curlCmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
			upcurlOut =  subprocess.Popen(upcurlCmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
			curlOutToFile(server_name,size,"Download",curlOut)
			curlOutToFile(server_name,size,"Upload",upcurlOut)
		except:
			pass
		#Delete zip file downloaded
		cmd = "rm -rf ./temp"+size+fileType
		subprocess.Popen(cmd,shell=True)
for server_name in serverList:
	rawUrl = server_name + baseDomain 
	url = preDomain + server_name + baseDomain
	pingCmd = "ping -w 1 " + rawUrl[:-1]
	pingResults = subprocess.Popen(pingCmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
	print pingResults
	foPing.write(pingResults)
	#Testing if ping fails based on '0 received' and 'unknown host' in result of ping command
	if(pingResults.find("0 received") < 0 and pingResults.find("unknown host") < 0):
		try:
			curlData(server_name)
		except:
			pass
fo.close()
foPing.close()
