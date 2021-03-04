#plotting autocorrleation plots

#importing required libraries
from pandas import read_csv
from pandas import DataFrame
from statsmodels.tsa.arima.model import ARIMA
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot

#load the file
electricityUsage = read_csv('pge_2020_daily_data1.csv', header=0, infer_datetime_format=True, parse_dates=['DATE'], index_col=['DATE'])
electricityUsage.index = electricityUsage.index.to_period('M')

#plot the data with an electricity plot
autocorrelation_plot(electricityUsage)
print(electricityUsage.head())
electricityUsage.plot()
pyplot.show()

# Define the model with p,d,q paramaters
model = ARIMA(electricityUsage, order=(15,1,0))

#Model Preparation on the training data
model_fit = model.fit()

# summary of fit model
print(model_fit.summary())
# line plot of residuals
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()

# density plot of residuals
residuals.plot(kind='kde')
pyplot.show()

# summary statisticss of residuals
print(residuals.describe())





