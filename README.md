# InternetSpeedTest

This repository consists of a few python scripts to automate the process of testing your internet connection and generating a linear regression model for the same. Models ping, download speed, upload speed vs distance, size.
Makes use of [Speedtest-cli](https://github.com/sivel/speedtest-cli) by [sivel](https://github.com/sivel/) as backbone for generating model for ping, downlaod speed, upload sped vs distance. This model generated is very rich and detailed.
While makes use of [TELE2](http://speedtest.tele2.net/) for making multi variable linear model incorporating ping,downlaod speed, upload speed vs distance, file size. This model is not as rich as the previous one since it is dependent highly on [TELE2](http://speedtest.tele2.net/) as a service which doesn't provide a very good spread on distance

## Repository Contents
* [src](https://github.com/gupta409/InternetSpeedTest/blob/master/src)
  * [speedTestMultiServer.py](https://github.com/gupta409/InternetSpeedTest/blob/master/src/sizeTest.py): This script will run commands with the speedtest-cli. It extracts list of servers on speedtest.net and then hits each of the servers to perform tests. The results are then saved in results.csv
  * [processData.py](https://github.com/gupta409/InternetSpeedTest/blob/master/src/processData.py): This script extracts data from results.csv and generates a linear regression model from the data. By default model is made for downloadSpeed vs distance, file can be changed to model other aspects. 
  * [sizeTest.py](https://github.com/gupta409/InternetSpeedTest/blob/master/src/sizeTest.py): This runs tests on TELE2 and generates sizeResults.csv which contains server_name, size, upload/download operation performed, speed and time taken.
  * [processSizes.py](https://github.com/gupta409/InternetSpeedTest/blob/master/src/processSizes.py): This script takes sizeResults.csv as input and processes the data to make a multivariable linear model.
  
## Dependencies
* Requires Python 2.7
* Requires following python packages
  * subprocess
  * os
  * pyplot
  * numpy
  * statsmodel
  * seaborn
  * pandas

## Use
1. Clone [speedtest-cli](https://github.com/sivel/speedtest-cli)
2. Move src folder inside speedtest-cli/
3. Run in following order
  1. speedtestMultiServer.py
  2. processData.py (options can be changed by uncommenting lines for different results)
  3. sizeTest.py
  4. processSizes.py (options can be changed by uncommenting lines for different results)
  





