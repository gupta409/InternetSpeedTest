import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.graphics as stgraph 
from statsmodels.stats.outliers_influence import summary_table
import seaborn as sb
import pandas
serverDistance = {'wen1-speedtest-1':4701,'zgb-speedtest-1':4839,'fra36-speedtest-1':4382,'bks-speedtest-1':4545,'vln038-speedtest-1':4674,'ams-speedtest-1':4180,'bck-speedtest-1':4158,'kst5-speedtest-1':4234,'nyc9-speedtest-1':1196}
def fixSpeed(x):
	if(x < 30):
		return x*1000000
	else:
		return x
def findDistance(x):
	return serverDistance[x]
data = pandas.read_csv('./sizeResults.csv', sep=',', na_values=".",parse_dates=[4])
headers = data.columns
downloadData = data[data["Type"]=="Download"]
uploadData = data[data["Type"]=="Upload"]
downloadSpeed = downloadData[headers[3]].apply(fixSpeed)
uploadSpeed= uploadData[headers[3]].apply(fixSpeed)
downloadSize = downloadData[headers[1]]
uploadSize = uploadData[headers[1]]
downloadTime = downloadData[headers[4]].dt.hour*60+downloadData[headers[4]].dt.second
uploadTime = uploadData[headers[4]].dt.hour*60+uploadData[headers[4]].dt.second
downloadDistance = downloadData[headers[0]].apply(findDistance)
uploadDistance = uploadData[headers[0]].apply(findDistance)
def linearAnalysis(xValues, yValues,xlabel,ylabel):
	#Ping Analysis
	df = pandas.DataFrame({ylabel:yValues,xlabel:xValues})
	yVal = df[ylabel]
	xVal = df[xlabel]
	X = sm.add_constant(xVal)
	model = sm.OLS(yVal,X).fit()
	print model.conf_int(alpha=0.10,cols=None)
	print model.summary()
	print model.predict(X).min()
	print model.predict(X).max()
	predict = model.predict(X)
#	sb.regplot(xVal,yVal,ci=90)
def multiLinAnalysis(a,b,c,label):
	df = pandas.DataFrame({'Size':a,'Distance':b,label:c})
	X = df[['Size','Distance']]
	y = df[label]
	X = sm.add_constant(X)
	model = sm.OLS(y,X).fit()
	print model.conf_int(alpha=0.10,cols=None)
	print model.summary()
	print model.predict(X).min()
	print model.predict(X).max()
	#sb.lmplot(x="Distance",y=label,hue="Size",data=df)
	sb.lmplot(x="Size",y=label,hue="Distance",data=df)
linearAnalysis(downloadDistance,downloadTime,'Distance','Time')
#linearAnalysis(uploadSize,uploadTime,'Size','Time')
#linearAnalysis(downloadSize,downloadSpeed,'Size','Speed')
#linearAnalysis(uploadSize,uploadSpeed,'Size','Speed')
#multiLinAnalysis(downloadSize,downloadDistance,downloadTime,"Time")
#multiLinAnalysis(uploadSize,uploadDistance,uploadTime,"Time")
#multiLinAnalysis(downloadSize,downloadDistance,downloadSpeed,"Speed")
#multiLinAnalysis(uploadSize,uploadDistance,uploadSpeed,"Speed")
plt.show()
