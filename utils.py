from numpy import genfromtxt
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from bokeh.models.glyphs import MultiLine
import pandas as pd
import numpy as np
from bokeh.palettes import Spectral11
from bokeh.plotting import figure, show, output_file
import scipy
import scipy.spatial
import os

def get_data(path):
    data = genfromtxt(path, delimiter=',')
    data = data[:,1:] #exlucde time field
    return data

def plot(data):
    colors = ['r','g','b','p','m']
    for i in range(data.shape[1]):
        plt.plot(data[:,i],colors[i])
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

def normalize(v):
    for i in range(v.shape[1]):
        v[:,i] /= np.max(v[:,i])
    return v

def dist(x,y,metric='euclidean'):
    #computes the absolute distance between two time sample multi-field data vectors
    #x: first vector (numpy array)
    #y: second vector (numpy array)
    #metric: distance metric to use (string)

    #indexing the vectors: x[time_idx][field]

    #indexing output:
    #combined[t] = distance between the n-dimensional points y[t] and x[t]
    #component[t,n] = absolute distance between the component values y[t,n] and x[t,n]

    time_points_x = x.shape[0]
    time_points_y = y.shape[0]
    time_points = np.minimum(time_points_x,time_points_y)

    if x.shape[1] != y.shape[1]:
        print "Data incorrectly formatted"

    combined_distance = np.zeros((time_points,))
    component_distance = np.zeros((time_points,x.shape[1]))

    for t in range(time_points):
        if metric=='euclidean':
            combined_distance[t] = scipy.spatial.distance.euclidean(y[t],x[t])


        elif metric == 'cityblock':
            combined_distance[t] = scipy.spatial.distance.cityblock(y[t],x[t])

        elif metric == 'cosine':
            combined_distance[t] = scipy.spatial.distance.cosine(y[t],x[t])

        for n in range(component_distance.shape[1]):
            component_distance[t,n] = np.abs(y[t,n]-x[t,n])

    return combined_distance,component_distance

def one_component_flat(oE_data):
    #only 3 components
    flat = [False,False,False]
    flat_ctr = 0
    thresh = 0.7
    for i in range(3):
        variance = np.abs(np.amax(oE_data[:,i]) - np.amin(oE_data[:,i]))
        #print variance
        if variance > thresh:
            flat[i] = False
        else:
            flat[i] = True
            flat_ctr += 1
    if flat_ctr == 0:
        return False
    else:
        return True


def dabornotdab():
    path = "./data/test.csv"
    ratings = [0,0,0,0,0,0]
    rating = 4
    ratings[0] = "I honestly don't know if you just sneezed or tried to dance."
    ratings[1] = "This isn't the fucking chicken dance."
    ratings[2] = "I can tell what you're trying to do, but if anyone asks we don't know each other, ok?"
    ratings[3] = "Well... not terrible. Practice that form a bit more and you'll be in good shape."
    ratings[4] = "You don't need a dabby you dabstar."
    ratings[5] = "Literally. Perfect."

    id_str = 'orientationEuler'
    #oE_data = input_data[id_str]
    oE_data = get_data(path)
    oE_data_norm = normalize(oE_data)
    oE_data = np.nan_to_num(oE_data)
    oE_data_norm = np.nan_to_num(oE_data_norm)

    maxmin_thresh = 1.5
    diff_thresh = 5

    if one_component_flat(oE_data) == False:
        #print "failed flat component analysis"
        rating -= 1

    data_dab = [0,0,0,0]
    dab_id_nums = [1493500380,1493500659,1493510372,1493510494]

    data_dab[0] = full_data(dab_id_nums[0],1,True)
    data_dab[1] = full_data(dab_id_nums[1],2,True)
    data_dab[2] = full_data(dab_id_nums[2],3,True)
    data_dab[3] = full_data(dab_id_nums[3],4,True)

    data_dab[0] = normalize(data_dab[0][id_str][105:])
    data_dab[1] = normalize(data_dab[1][id_str][85:])
    data_dab[2] = normalize(data_dab[2][id_str][110:])
    data_dab[3] = normalize(data_dab[3][id_str][150:])

    differences = [0,0,0,0]

    for i in range(4):
        differences[i],component = dist(data_dab[i],oE_data_norm)
        if np.amax(differences[i]) > diff_thresh:
            #print "failed 5 threshold analysis"
            rating -= 1
            break

    for i in range(4):
        differences[i],component = dist(data_dab[i],oE_data_norm)
        if np.amin(differences[i]) > diff_thresh/2:
            #print "failed minimum threshold analysis"
            rating -= 1
            break

    for i in range(4):
        if np.amax(differences[i]) - np.amin(differences[i]) > maxmin_thresh:
            #print "failed max-min analysis"
            rating -= 1
            break

    for i in range(4):
        if np.amax(differences[i]) < 0.5:
            rating = 5

    say_string = "say "+"\"" + ratings[rating]+"\""
    #print say_string
    os.system(say_string)
