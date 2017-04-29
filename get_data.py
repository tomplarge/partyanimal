from pandas import read_csv


# takes in a csv file as a string and outputs an array
def get_data("data/dab1_accelerometer-1493500380.csv"):

    data = pd.read_csv(input_file, sep=',',header=None)
    arr = data.valuesarray

    print arr
    return arr
