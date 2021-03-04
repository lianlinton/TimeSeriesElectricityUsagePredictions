#summarize data for a specific day together

#import required libraries
import pandas as pd
import math

# load the file
electricityUsage = pd.read_csv('pge_2020_data1.csv', header=0, infer_datetime_format=True, parse_dates=['DATE'], index_col=['DATE'])
#print(electricityUsage.head())

#create an empty dictionary
sumDataDict = {'DATE': [0] , 'USAGE': [0] }

#plot electricity usage for each month
months = [x for x in range(1, 13)]

#iterate through each month
for m in range(len(months)):
    #conditions to avoid errors while searching for a particular date and month
    if (m == 1):
        #plot electricity usage for each day for February
        days = [x for x in range(1, 29)]
    elif (m == 8 or m ==3 or m == 5 or m ==10):
        #plot electricity usage for each day for September, April, June, November
        days = [x for x in range(1, 31)]
    else:
        #plot electricity usage for each day for any other rmonth
        days = [x for x in range(1, 32)]
    #print (days)
    #iterate through each month  
    for d in range(len(days)):
        if (m < 9):
            if (d < 9):
                #plot electricity usage for each day
                dayEach = '2020-0'+str(months[m])+'-0' + str(days[d])
            else:
                #plot electricity usage for each day
                dayEach = '2020-0'+str(months[m])+'-' + str(days[d])
        else:
            if (d < 9):
                #plot electricity usage for each day
                dayEach = '2020-'+str(months[m])+'-0' + str(days[d])
            else:
                #plot electricity usage for each day
                dayEach = '2020-'+str(months[m])+'-' + str(days[d])
        #calculates the sum of the data in the group
        dayEachData = math.fsum(electricityUsage[dayEach]['USAGE'])
        #clears the originally created 0 , 0 row
        if ((sumDataDict['DATE'][0] == 0)  and (sumDataDict['USAGE'][0] == 0)):
            sumDataDict['DATE'][0] = dayEach
            sumDataDict['USAGE'][0] = dayEachData
        else:
            #adds new sums to the dictionary
            sumDataDict['DATE'].append(dayEach)
            sumDataDict['USAGE'].append(dayEachData)

#converts dictionary to a dataframe
sumData = pd.DataFrame.from_dict(sumDataDict)

#converts it to a csv file
sumData.to_csv('pge_2020_daily_data1.csv')