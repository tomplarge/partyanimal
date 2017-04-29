from numpy import genfromtxt
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import MultiLine
import pandas as pd
import numpy as np
from bokeh.palettes import Spectral11
from bokeh.plotting import figure, show, output_file

def get_data(path):
    data = genfromtxt(path, delimiter=',')
    data = data[:,1:] #exlucde time field
    return data

def plot(data,data1,data2):
    plt.plot(data,'r')
    plt.plot(data1,'g')
    plt.plot(data2,'b')
    plt.show()

def plot_bokeh(data1,data2,field):

    output_file('temp.html')

    toy_df = pd.DataFrame(data=data[field], columns = ('a', 'b'), index = pd.DatetimeIndex(start='01-01-2015',periods=5, freq='d'))

    numlines=len(toy_df.columns)
    mypalette=Spectral11[0:numlines]

    p = figure(width=500, height=300, x_axis_type="datetime")
    p.multi_line(xs=[toy_df.index.values]*numlines,ys=[toy_df[name].values for name in toy_df],
                line_color=mypalette,
                line_width=5)
    show(p)

def make_path(id_str):
    return "./data/dab1_"+id_str+"-1493500380.csv"

def full_data(id_num,dataset_num,dab):
    id_str = ['accelerometer','emg','gyro','orientation','orientationEuler']
    data = {}
    for i in range(len(id_str)):
        path = "./data/"

        if dab:
            path += "dab"+str(dataset_num)+"_"
        else:
            path+="not_dab_"+str(dataset_num)

        path+=id_str[i]+"-"+str(id_num)+'.csv'
        data[id_str[i]] = get_data(path)

    return data
