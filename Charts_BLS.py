import pandas as pd
import numpy as np
import bls
import plotly.express as px


def makeChart(series, startYear, endYear, changeValue, yaxisAltName):
    BLSid = "c90dfae15adb45e68b3cbf64f5304e9a"
    df = bls.get_series(series, startYear, endYear, BLSid)
    df = df.reset_index()
    df.columns = ['Date', yaxisAltName]
    df['Date'] = df['Date'].astype(str)
    df[str(changeValue)+' Month Change'] = df[yaxisAltName] - df[yaxisAltName].shift(changeValue)

    def createFigure(df):
        if changeValue == 0:
            fig = px.bar(df, x = 'Date', y = yaxisAltName)
        else:
            chart_df = df[['Date', str(changeValue)+' Month Change']].dropna()
            chart_df['Date'] = df['Date'].astype(str)
            fig = px.bar(chart_df, x = 'Date', y = str(changeValue)+' Month Change')
        fig.show()
    createFigure(df)

## Slide 3: US Payroll Jobs - YoY, 2000 to Present
makeChart('CES0000000001', 1999, 2020, 12, 'Jobs')

## Slide 4: US Payroll Jobs - MoM, 2000 to Present
makeChart('CES0000000001', 2000, 2020, 1, 'Jobs')

## Slide 5: US Payroll Jobs - MoM & Total, 2013 to Present
makeChart('CES0000000001', 2012, 2020, 1, 'Jobs')

## Slide 8: US Unemployment Rate, 2010 to Present
makeChart('LNS14000000', 2010, 2020, 0, 'Unemployment Rate')

## Slide 13: US Labor Productivity, 2000 to Present
makeChart('PRS85006093', 2000, 2020, 0, 'Productivity')

##NOT WORKING 15, 16
## Slide 15: US Annual Consumer Prices - YoY, 2001 to Present
makeChart('CUUS0000SA0', 2001, 2020, 12, 'Consumer Prices')

## Slide 16: US Monthly Consumer Prices - MoM, 2001 to Present
makeChart('CUUS0000SA0', 2001, 2020, 0, 'Consumer Prices')

## Slide 25: WMA Annual Job Change - YoY, 1991 to Present
makeChart('SMU11479000000000001', 1990, 2020, 12, 'Job Change')

## Slide 26: WMA Annual Job Change - MoM & Total, 2012 to Present
makeChart('SMU11479000000000001', 2012, 2020, 1, 'Job Change')

## Slide 28: DC Annual Job Change - MoM, 1991 to Present
makeChart('SMU11000000000000001', 1991, 2020, 1, 'Job Change')

## Slide 29: DC Annual Job Change - MoM & Total, 2012 to Present
makeChart('SMU11000000000000001', 2012, 2020, 1, 'Job Change')

## Slide 32: NoVa Annual Job Change - MoM, 1991 to Present
makeChart('SMU51947830000000001', 1990, 2020, 1, 'Job Change')







# ''' Slide 33: NoVa Annual Job Change - MoY & Total, 2012 to Present'''
# JC33 = bls.get_series('SMU51947830000000001', 1999, 2020, BLSid)

# ''' ========================================================== '''
# ''' Slide 37: WMA PB&S Job Change - MoY, 2013 to Present'''
# PBSJC37 = bls.get_series('SMU11479006000000001', 1999, 2020, BLSid)

# ''' ========================================================== '''
# ''' Slide 39: Federal Government Job Change - MoY & Total, 2010 to Present'''
# FedJC39 = bls.get_series('SMU11479009091000001', 1999, 2020, BLSid)