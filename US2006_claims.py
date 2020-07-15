from fredapi import Fred
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches


# For reference: https://mortada.net/python-api-for-fred.html
# FRED API Key (must have FRED acct): https://research.stlouisfed.org/useraccount/apikeys

fred = Fred(api_key='ENTER YOUR OWN FRED API HERE')

### pulling Initial Claims data then creating a dataframe
df = fred.get_series('ICSA', observation_start = '2006-01-07', observation_end = '2020-07-14')
df = pd.DataFrame(data = df).reset_index()      #turns series data into dataframe
df.columns = ['date', 'ICSA']
df['ICSA_millions'] = df['ICSA']/1000000
#print(df)

### creating graph 
fig, ax = plt.subplots(figsize = (11, 5.5))
ax.plot(df['date'], df['ICSA_millions'], color = 'olivedrab', zorder = 3) # for some reason, zorder = 3 helps bars show up in front of grid

# making axes pretty
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('whitesmoke')
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid(axis = 'y', color = 'gainsboro', zorder = 0) # zorder = 0 helps grid stay behind bars

# this changes the x-axis to show only abbreviated months
locator = mdates.YearLocator(1, month = 1, day =1)
fmt = mdates.DateFormatter('%Y')
X = plt.gca().xaxis
X.set_major_locator(locator)
X.set_major_formatter(fmt)

# creating filler
y1 = df['ICSA_millions']
y0 = 0
ax.fill_between(df['date'], y1, y0, where =y1>y0, facecolor='forestgreen', alpha=0.5)

# this adds the rectangle for 2008 crisis
square_df = df.iloc[100:].reset_index(drop = True) #drops first 100 dates to get us Dec 2007
square_df = square_df.iloc[:83].reset_index(drop = True) #keeps only 83 weeks of the recession until June 2009
x = square_df['date']
y2 = 8
ax.fill_between(x, y2, y0, where=y2>y0, color = 'silver', alpha=0.2)
ax.annotate('2007-2008', (mdates.date2num(x[10]), 4.9), color = 'black', size ='small', alpha=.7)
ax.annotate('Financial Crisis', (mdates.date2num(x[1]), 4.5), color = 'black', size='small', alpha=.7)
fig.autofmt_xdate()

# this formats the rest of graph
plt.ylabel('MILLIONS', fontdict= {'stretch':'condensed', 'variant': 'small-caps'})
plt.ylim(0, 8)
plt.title('National: Initial Claims for Unemployment since 2006 (Seasonally Adjusted)')
plt.margins(.01)
#plt.show()
plt.savefig('/Users/cansu/Desktop/ICSA2006.png', bbox_inches='tight')