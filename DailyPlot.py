#daily line plots
#import required libraries
from pandas import read_csv
from matplotlib import pyplot
# load file
electricityUsage = read_csv('pge_2020_data1.csv', header=0, infer_datetime_format=True, parse_dates=['DATE'], index_col=['DATE'])
#print(electricityUsage.head())

#plot the power for each day
days = [j for j in range(1, 31)]
pyplot.figure()

for i in range(len(days)):
    #create subplots for each day
    dayEachPlot = pyplot.subplot(len(days), 1, i+1)
    #print (ax)
    #group the values
    if (i <9):
        dayEach = '2020-09-0' + str(days[i])
    else:
        dayEach = '2020-09-' + str(days[i])
    #print(dayEach)
    #print(electricityUsage)
    #get all data for the day
    dayEachData = electricityUsage[dayEach]
    #print(dayEachData)
    #plot the electicity usage for the day
    pyplot.plot(dayEachData['USAGE'])
    #pyplot.plot(electricityUsage['USAGE'])
    #add a title to the plot
    pyplot.title(dayEach, y=0, loc='left')
#show plot
pyplot.show()