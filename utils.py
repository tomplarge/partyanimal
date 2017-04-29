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

def full_data(id_num,dataset_num,dab):
    id_str = ['accelerometer','emg','gyro','orientation','orientationEuler']
    data = {}
    for i in range(len(id_str)):
        path = "./data/"

        if dab:
            path += "dab"+str(dataset_num)+"_"
        else:
            path+="not_dab_"+str(id_num)+"_e"

        path+=id_str[i]+"-"+str(id_num)+'.csv'
        data[id_str[i]] = get_data(path)
    return data
