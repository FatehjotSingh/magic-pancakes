import numpy as np
import plotly.express as py
import pandas as pd
import csv

def plot():
    fil= open('4.csv')
    reader=csv.DictReader(fil)   
    chart= py.scatter(reader,x='Days',y='Marks',size_max=50,title='Attendance-Percentage ratio')
    chart.show()

def datasource():
    marks=[]
    days=[]
    fil= open('csvs/4.csv')
    reader=csv.DictReader(fil)
    for i in reader:
        marks.append(float(i['Marks']))
        days.append(float(i['Days']))
    return {'x':days, 'y':marks}

def findcorr(source):
    correlation= np.corrcoef(source['x'],source['y'])
    print(correlation[0,1])

def setup():
    src= datasource()
    findcorr(src)
    plot()

setup();
