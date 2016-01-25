#SoftwareCarpentry final example

df = pd.read_csv('software/TrainingMaterial/python-ecology/bouldercreek_09_2013.txt', delimiter='\t', skiprows=25, header=[0,1], parse_dates=[2], infer_datetime_format=True)

df.columns.values
type(df.columns.values[0])

#Extract date and time to reformat columns, pandas parses strings to date-time automatically
temp = pd.DatetimeIndex(df[('datetime', '20d')])

#create two new columns for Date and Time
df['Date'] = temp.date
df['Time'] = temp.time
#delete a column from a dataframe
del df[('datetime', '20d')]

#rename columns with something more handy
df.columns = ['agency', 'site_no', 'tz_cd', 'Discharge', '04_00060_cd', 'Date', 'Time']
df_clean = df.loc[:, ['Date', 'Time', 'Discharge']]

#Plots
#How many unique dates are there
df_clean['Date'].nunique()
df_clean['Date'].unique()

#Plot the discharge for Sep9-15
startDay = pd.datetime(2013, 9, 9)
endDay = pd.datetime(2013, 9, 15)
#inspect 
startDay.date
endDay.date
#find all dates after startDay
df_clean['Date'] > startDay.date()
#find all dates before endDay
df_clean['Date'] < endDay.date()

mask = (df_clean['Date'] > startDay.date()) & (df_clean['Date'] < endDay.date())
#how many valid dates are there in mask
mask.sum() #sums up all values "True"
#subselect the data
df_clean[mask]["Discharge"]
#subselect and plot the data
df_clean[mask]["Discharge"].plot()
df_clean[mask]["Discharge"].plot("bar")

#Plot the discharge vs time for one day
day = pd.datetime(2013, 9, 9)
mask = df_clean['Date'] == day.date()
df_clean[mask]
df_clean[mask][['Time', 'Discharge']].plot()
#How does the plot change with the kind option, why does 'hist' look so differently?
df_clean[mask][['Time', 'Discharge']].plot(kind = 'line')
df_clean[mask][['Time', 'Discharge']].plot(kind = 'bar')
df_clean[mask][['Time', 'Discharge']].plot(kind = 'hist')
df_clean[mask][['Discharge']].plot(kind = 'hist')

#Generate such plots for every day. Tip: write a function and use a for-loop

#Plot the minimum and maximum discharge per day
minDischargePerDay = df_clean.groupby('Date')['Discharge'].min()
maxDischargePerDay = df_clean.groupby('Date')['Discharge'].max()
newFrame = pd.concat([minDischargePerDay, maxDischargePerDay], axis=1)
newFrame.plot(subplots=True)





