#implementing an ARIMA model to predict electricity usage Records

#importing the libraries
from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt

#load the dataset
electricityUsage = read_csv('pge_2020_daily_data1.csv', header=0, infer_datetime_format=True, parse_dates=['DATE'], index_col=['DATE'])
electricityUsage.index = electricityUsage.index.to_period('M')

#split into train and test sets
#train: Jan - Oct
#test: Nov - Dec
electricityValue = electricityUsage.values
train, test = electricityValue[1:304], electricityValue[304:366]

#storing past datas in a list
pastData = [x for x in train]

#storing predictions in a list
predictions = list()

#walk-forward validation
#past data is used for more future predictions
for t in range(len(test)):
    #testing different values for p, d, q
    #model = ARIMA(pastData, order=(5,1,0))
    #model = ARIMA(pastData, order=(6,1,1))
    model = ARIMA(pastData, order=(15,1,0))
    #fit the model
    model_fit = model.fit()
    #forecast predictions based on the output
    output = model_fit.forecast()
    #store the prediction
    predict = output[0]
    #append it to the list of predictions
    predictions.append(predict)
    #store expected value
    expected = test[t]
    #append to the list of past data for future observations
    pastData.append(expected)
    #print comparisons
    print('predicted=%f, expected=%f' % (predict, expected))
    
#evaluate forecasts with RMSE
rmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
print (predictions)

#plot forecasts against actual outcomes
#blue: expected
#red: predictions
pyplot.plot(test)
pyplot.plot(predictions, color='red')
#provide a visual display
pyplot.show()

#pyplot.plot(predictions)
#pyplot.show()
