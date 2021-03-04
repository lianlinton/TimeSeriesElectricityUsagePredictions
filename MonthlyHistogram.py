#monthly histogram plots

#import required libraries
from pandas import read_csv
from matplotlib import pyplot

#load the file
electricityUsage = read_csv('pge_2020_data1.csv', header=0, infer_datetime_format=True, parse_dates=['DATE'], index_col=['DATE'])
#print(electricityUsage.head())

#plot the power for each month
months = [x for x in range(1, 13)]
pyplot.figure()

for i in range(len(months)):
    #create subplots for each month
    monthEachPlot = pyplot.subplot(len(months), 1, i+1)
    #group the values of the month
    if (i <9):
        monthEach = '2020-0' + str(months[i])
    else:
        monthEach = '2020-' + str(months[i])
    #print(monthEach)
    #get all data for the month
    monthEachData = electricityUsage[monthEach]
    #plot the electricity usage for the month
    monthEachData['USAGE'].hist(bins=100)
    #zooming on the distribution in the histogram 
    monthEachPlot.set_xlim(0, 2)
    #add a title to the plot
    pyplot.title(monthEach, y=0, loc='right')
    
#show plot    
pyplot.show()