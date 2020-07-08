import pandas as pd
import numpy as np
import bls
import plotly.express as px

# Basic Bar Chart Function
def makeBarChart(series, startYear, endYear, changeValue, yaxisAltName, title):
    BLSid = "INSERT YOUR OWN PUBLIC DATA API ACCT NUMBER"
    df = bls.get_series(series, startYear, endYear, BLSid)
    df = df.reset_index()
    df.columns = ['Date', yaxisAltName]
    df['Date'] = df['Date'].astype(str)
    df[str(changeValue)+' Month Change'] = df[yaxisAltName] - df[yaxisAltName].shift(changeValue)

    def createBarFigure(df):
        if changeValue == 0:
            fig = px.bar(df, x = 'Date', y = yaxisAltName)
        else:
            chart_df = df[['Date', str(changeValue)+' Month Change']].dropna()
            chart_df['Date'] = df['Date'].astype(str)
            fig = px.bar(chart_df, x = 'Date', y = str(changeValue)+' Month Change')
        fig.show()
    createFigure(df)
    
# Basic Line Chart Function
def makeLineChart(series, startYear, endYear, changeValue, yaxisAltName, title):
    BLSid = 'INSERT YOUR OWN PUBLIC DATA API ACCT NUMBER'
    df = bls.get_series(series, startYear, endYear, BLSid)
    df = df.reset_index()
    df.columns = ['Date', yaxisAltName]
    df['Date'] = df['Date'].astype(str)
    df[str(changeValue)+' Month Change'] = df[yaxisAltName] - df[yaxisAltName].shift(changeValue)

    def createLineFigure(df):
        if changeValue == 0:
            fig = px.line(df, x = 'Date', y = yaxisAltName, title = title)
        else:
            chart_df = df[['Date', str(changeValue)+' Month Change']].dropna()
            chart_df['Date'] = df['Date'].astype(str)
            fig = px.line(chart_df, x = 'Date', y = str(changeValue)+' Month Change', title = title)
        fig.show()
    createLineFigure(df)
    
    
    
# Horizontal Bar Chart Function (very specific right now, work-in-progress to make it more general)
# personally not 100% happy with this code, but it's the start.
# I know it will have issues gettinig one month difference in January 
def makeHorzBarChart(series1, series2, series3, series4, series5, series6, series7, series8, series9, series10, series11, series12,
                    year, month, changeValue, title):

    BLSid = 'INSERT YOUR OWN PUBLIC DATA API ACCT NUMBER'
    
    #Creating DF
    if changeValue == 1:
        s1_1 = bls.get_series(series1, year, year, BLSid)[str(year)+'-'+str(month)]
        s1_2 = bls.get_series(series1, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s1 = s1_1 - s1_2

        s2_1 = bls.get_series(series2, year, year, BLSid)[str(year)+'-'+str(month)]
        s2_2 = bls.get_series(series2, year, year, BLSid)[str(year)+'-'+str(month- 1)]
        s2 = s2_1 - s2_2

        s3_1 = bls.get_series(series3, year, year, BLSid)[str(year)+'-'+str(month)]
        s3_2 = bls.get_series(series3, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s3 = s3_1 - s3_2

        s4_1 = bls.get_series(series4, year, year, BLSid)[str(year)+'-'+str(month)]
        s4_2 = bls.get_series(series4, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s4 = s4_1 - s4_2

        s5_1 = bls.get_series(series5, year, year, BLSid)[str(year)+'-'+str(month)]
        s5_2 = bls.get_series(series5, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s5 = s5_1 - s5_2

        s6_1 = bls.get_series(series6, year, year, BLSid)[str(year)+'-'+str(month)]
        s6_2 = bls.get_series(series6, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s6 = s6_1 - s6_2

        s7_1 = bls.get_series(series7, year, year, BLSid)[str(year)+'-'+str(month)]
        s7_2 = bls.get_series(series7, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s7 = s7_1 - s7_2

        s8_1 = bls.get_series(series8, year, year, BLSid)[str(year)+'-'+str(month)]
        s8_2 = bls.get_series(series8, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s8 = s8_1 - s8_2

        s9_1 = bls.get_series(series9, year, year, BLSid)[str(year)+'-'+str(month)]
        s9_2 = bls.get_series(series9, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s9 = s9_1 -s9_2

        s10_1 = bls.get_series(series10, year, year, BLSid)[str(year)+'-'+str(month)]
        s10_2 = bls.get_series(series10, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s10 = s10_1 - s10_2

        s11_1 = bls.get_series(series11, year, year, BLSid)[str(year)+'-'+str(month)]
        s11_2 = bls.get_series(series11, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s11 = s11_1 - s11_2

        s12_1 = bls.get_series(series12, year, year, BLSid)[str(year)+'-'+str(month)]
        s12_2 = bls.get_series(series12, year, year, BLSid)[str(year)+'-'+str(month - 1)]
        s12 = s12_1 - s12_2

        
    else:
        s1_1 = bls.get_series(series1, year, year, BLSid)[str(year)+'-'+str(month)]
        s1_2 = bls.get_series(series1, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s1 = s1_1 - s1_2

        s2_1 = bls.get_series(series2, year, year, BLSid)[str(year)+'-'+str(month)]
        s2_2 = bls.get_series(series2, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s2 = s2_1 - s2_2

        s3_1 = bls.get_series(series3, year, year, BLSid)[str(year)+'-'+str(month)]
        s3_2 = bls.get_series(series3, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s3 = s3_1 - s3_2

        s4_1 = bls.get_series(series4, year, year, BLSid)[str(year)+'-'+str(month)]
        s4_2 = bls.get_series(series4, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s4 = s4_1 - s4_2

        s5_1 = bls.get_series(series5, year, year, BLSid)[str(year)+'-'+str(month)]
        s5_2 = bls.get_series(series5, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s5 = s5_1 - s5_2

        s6_1 = bls.get_series(series6, year, year, BLSid)[str(year)+'-'+str(month)]
        s6_2 = bls.get_series(series6, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s6 = s6_1 - s6_2

        s7_1 = bls.get_series(series7, year, year, BLSid)[str(year)+'-'+str(month)]
        s7_2 = bls.get_series(series7, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s7 = s7_1 - s7_2

        s8_1 = bls.get_series(series8, year, year, BLSid)[str(year)+'-'+str(month)]
        s8_2 = bls.get_series(series8, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s8 = s8_1 - s8_2

        s9_1 = bls.get_series(series9, year, year, BLSid)[str(year)+'-'+str(month)]
        s9_2 = bls.get_series(series9, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s9 = s9_1 -s9_2

        s10_1 = bls.get_series(series10, year, year, BLSid)[str(year)+'-'+str(month)]
        s10_2 = bls.get_series(series10, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s10 = s10_1 - s10_2

        s11_1 = bls.get_series(series11, year, year, BLSid)[str(year)+'-'+str(month)]
        s11_2 = bls.get_series(series11, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s11 = s11_1 - s11_2

        s12_1 = bls.get_series(series12, year, year, BLSid)[str(year)+'-'+str(month)]
        s12_2 = bls.get_series(series12, year-1, year-1, BLSid)[str(year-1)+'-'+str(month)]
        s12 = s12_1 - s12_2


    df = {'Series': [series1, series2, series3, series4, series5, series6, series7, series8, series9, series10, series11, series12],
        'MoYChange': [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]}

    fig = px.bar(df, x = 'MoYChange', y = 'Series', orientation = 'h', title = title)
    fig.show()
    


# Slide 3: US Payroll Jobs - YoY, 2000 to Present
makeBarChart('CES0000000001', 1999, 2020, 12, 'Jobs', title = "US Payroll Jobs - YoY, 2000 to Present")

# Slide 4: US Payroll Jobs - MoM, 2000 to Present
makeBarChart('CES0000000001', 2000, 2020, 1, 'Jobs', title = 'US Payroll Jobs - MoM, 2000 to Present')

# Slide 5: US Payroll Jobs - MoM & Total, 2013 to Present
makeBarChart('CES0000000001', 2012, 2020, 1, 'Jobs', title = 'US Payroll Jobs - MoM & Total, 2013 to Present')

# Slide 6: US Payroll Job Change by Sector -  12 Month Net Change
makeHorzBarChart('CES9091000001',
'CES6500000001',
'CES6000000001',
'CES7000000001',
'CES4200000001',
'CES3000000001',
'CES5500000001',
'CES2000000001',
'CES4142000001',
'CES8000000001',
'CES4300000001',
'CES5000000001', 2020, 6, 12, "US Payroll Job Change by Sector -  12 Month Net Change (June 2020")

# Slide 6: US Payroll Job Change by Sector -  1 Month Net Change
makeHorzBarChart('CES9091000001',
'CES6500000001',
'CES6000000001',
'CES7000000001',
'CES4200000001',
'CES3000000001',
'CES5500000001',
'CES2000000001',
'CES4142000001',
'CES8000000001',
'CES4300000001',
'CES5000000001', 2020, 6, 1, "US Payroll Job Change by Sector -  1 Month Net Change (June 2020")


# Slide 8: US Unemployment Rate, 2010 to Present
makeLineChart('LNS14000000', 2010, 2020, 0, 'Unemployment Rate', title = 'US Unemployment Rate, 2010 to Present')

# Slide 13: US Labor Productivity, 2000 to Present
makeBarChart('PRS85006093', 2000, 2020, 0, 'Productivity', title = 'US Labor Productivity, 2000 to Present')


#NOT WORKING 15, 16 because of "HALF1" and "HALF2" time period points. 
# May have to do these seperate without function.
# Or change the function to ignore anything other than normal months
# Slide 15: US Annual Consumer Prices - YoY, 2001 to Present
makeBarChart('CUUS0000SA0', 2000, 2020, 12, 'Consumer Price Change', title = 'US Annual Consumer Prices - YoY, 2001 to Present')

# Slide 16: US Monthly Consumer Prices - MoM, 2001 to Present
makeBarChart('CUUS0000SA0', 2001, 2020, 0, 'Consumer Prices', title = 'US Monthly Consumer Prices - MoM, 2001 to Present')


# Slide 25: WMA Annual Job Change - YoY, 1991 to Present
makeBarChart('SMU11479000000000001', 1990, 2020, 12, 'Job Change', title = 'Washington MSA Annual Job Change - YoY, 1991 to Present')

# Slide 26: WMA Annual Job Change - MoM & Total, 2012 to Present
makeBarChart('SMU11479000000000001', 2012, 2020, 1, 'Job Change', title = 'Washington MSA Annual Job Change - MoM & Total, 2012 to Present')

# Slide 28: DC Annual Job Change - MoM, 2012 to Present
makeBarChart('SMU11000000000000001', 2011, 2020, 1, 'Job Change', title = 'Washington DC Annual Job Change - MoM, 2012 to Present')

# Slide 29: DC Annual Job Change - MoY & Total, 1991 to Present
makeBarChart('SMU11000000000000001', 1998, 2020, 12, 'Job Change', title = 'Washington DC Annual Job Change - MoY & Total, 1991 to Present')

# Slide 32: NoVa Annual Job Change - MoY, 1991 to Present
makeBarChart('SMU51947830000000001', 1990, 2020, 12, 'Job Change', title = 'NoVa Annual Job Change - MoY, 1991 to Present')

# Slide 33: NoVa Annual Job Change - MoY & Total, 2012 to Present
makeBarChart('SMU51947830000000001', 2012, 2020, 12, 'Job Change', title = 'MoY & Total, 2012 to Present')


# Slide 37: WMA PB&S Job Change - MoY, 2013 to Present
makeBarChart('SMU11479006000000001', 2012, 2020, 12, 'Job Change', title = 'WMA PB&S Job Change - MoY, 2013 to Present')

# Slide 39: Federal Government Job Change - MoY & Total, 2010 to Present
makeBarChart('SMU11479009091000001', 2009, 2020, 12, 'Job Change', title = 'Federal Government Job Change - MoY & Total, 2010 to Present')





