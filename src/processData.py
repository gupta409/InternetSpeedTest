import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import statsmodels.graphics as stgraph 
from statsmodels.stats.outliers_influence import summary_table
import seaborn as sb
import pandas

data = pandas.read_csv('./results.csv', sep=',', na_values=".")
headers = data.columns
#Distance
distance = data[headers[4]]
#Ping
ping = data[headers[5]]
#Download Data
download = data[headers[6]]
#Uplaod Data
upload = data[headers[7]]
def ciAnalysis(re,x,y):
	st, data, ss2 = summary_table(re, alpha=0.10)
	fittedvalues = data[:,2]
	predict_mean_se  = data[:,3]
	predict_mean_ci_low, predict_mean_ci_upp = data[:,4:6].T
	predict_ci_low, predict_ci_upp = data[:,6:8].T
	plt.plot(x, y, 'o')
	plt.plot(x, fittedvalues, '-', lw=2)
	plt.plot(x, predict_ci_low, 'r--', lw=2)
	plt.plot(x, predict_ci_upp, 'r--', lw=2)
	plt.plot(x, predict_mean_ci_low, 'r--', lw=2)
	plt.plot(x, predict_mean_ci_upp, 'r--', lw=2)
	plt.show()
def pingAnalysis(distance, ping):
	#Ping Analysis
	df = pandas.DataFrame({'distance':distance,'ping':ping})
	df = df[df['ping'] <=300]
	distance = df['distance']
	ping = df['ping']
	X = sm.add_constant(distance)
	model = sm.OLS(ping,X).fit()
	print model.conf_int(alpha=0.10,cols=None)
	print model.summary()
	print model.predict(X).min()
	print model.predict(X).max()
	#ciAnalysis(model,distance,ping)
	sb.regplot(distance,ping,ci=90)
	plt.show()
def downloadAnalysis(distance, download):
	#Download Analysis
	df = pandas.DataFrame({'distance':distance,'download':download})
	distance1 = df['distance']
	download = df['download']
	X = sm.add_constant(distance1)
	model1 = sm.OLS(download,X).fit()
	print model1.conf_int(alpha=0.10,cols=None)
	print model1.summary()
	print model1.predict(X).min()
	print model1.predict(X).max()
	sb.regplot(distance1,download,ci=90)
	plt.show()
def uploadAnaysis(distance, upload):
	#Upload Analysis
	df = pandas.DataFrame({'distance':distance,'upload':upload})
	distance2 = df['distance']
	upload = df['upload']
	X = sm.add_constant(distance2)
	model2 = sm.OLS(upload,X).fit()
	print model2.conf_int(alpha=0.10,cols=None)
	print model2.summary()
	print model2.predict(X).min()
	print model2.predict(X).max()
	sb.regplot(distance2,upload,ci=90)
	plt.show()
#pingAnalysis(distance, ping)
downloadAnalysis(distance, download)
#uploadAnaysis(distance, upload)

