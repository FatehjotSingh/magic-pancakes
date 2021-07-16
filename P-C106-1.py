import numpy as np
import plotly.express as py
import pandas as pd
import csv

def plot():
    fil= open('3.csv')
    reader=csv.DictReader(fil)   
    chart= py.scatter(reader,x='Coffee',y='sleep',size_max=50,title='Sleep-Coffee')
    chart.show()

def datasource():
    cf=[]
    sh=[]
    fil= open('csvs/3.csv')
    reader=csv.DictReader(fil)
    for i in reader:
        cf.append(float(i['Coffee']))
        sh.append(float(i['sleep']))
    return {'x':cf, 'y':sh}

def findcorr(source):
    correlation= np.corrcoef(source['x'],source['y'])
    print(correlation[0,1])

def setup():
    src= datasource()
    findcorr(src)
    plot()

setup();
