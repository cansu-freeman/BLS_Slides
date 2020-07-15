from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# For reference: https://mortada.net/python-api-for-fred.html
# FRED API Key (must have FRED acct): https://research.stlouisfed.org/useraccount/apikeys

fred = Fred(api_key='ENTER YOUR OWN FRED API HERE')

### pulling Initial Claims data then creating a dataframe
df = fred.get_series('ICSA', observation_start = '2020-03-07', observation_end = '2020-07-14')
df = pd.DataFrame(data = df).reset_index()      #turns series data into dataframe
df.columns = ['date', 'ICSA']
df['ICSA_millions'] = df['ICSA']/1000000
#print(df)

### creating graph 
fig, ax = plt.subplots(figsize = (11, 5.5))
ax.bar(df['date'], df['ICSA_millions'], color = 'olivedrab', width = 3, zorder = 3) # for some reason, zorder = 3 helps bars show up in front of grid

# making axes pretty
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('whitesmoke')
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.grid(axis = 'y', color = 'gainsboro', zorder = 0) # zorder = 0 helps grid stay behind bars

# this changes the x-axis to show only abbreviated months
ax.set_xticks(df['date'])
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b-%d"))
ax.xaxis.set_minor_formatter(mdates.DateFormatter("%b-%d"))
plt.xticks(rotation=60) 

# labeling points
for x,y in zip(df['date'], df['ICSA_millions']):
    label = "{0:.2f}".format(y) # 2 decimal points
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

# this formats the graph
plt.ylabel('MILLIONS', fontdict= {'stretch':'condensed', 'variant': 'small-caps'})
plt.ylim(0, 8)
plt.title('National: Initial Claims for Unemployment (Seasonally Adjusted)')
plt.margins(.01)
plt.savefig('/Users/XXXXX/Desktop/ICSA.png', bbox_inches='tight')
