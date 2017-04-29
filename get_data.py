import pandas as pd


# takes in a csv file as a string and outputs an array
def get_data(input_file):

    data = pd.read_csv(input_file, sep=',',header=None)
    arr = data.valuesarray

    return arr
