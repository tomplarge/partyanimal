from numpy import genfromtxt
import matplotlib.pyplot as plt

def get_data(path):
    data = genfromtxt(path, delimiter=',')
    data = data[:,1:]
    return data

def plot(data):
    plt.plot(data)
    plt.show()

def make_path(id_str):
    return "./data/dab1_"+id_str+"-1493500380.csv"
