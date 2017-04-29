import numpy as np
import scipy
import scipy.spatial

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
            
            for n in range(component_distance.shape[1]):
                component_distance[t,n] = np.abs(y[t,n]-x[t,n])

    return combined_distance,component_distance

x = np.zeros((5,3))
y = np.zeros((5,3))

for i in range(5):
    for j in range(3):
        x[i,j] = i+j
        y[i,j] = i-j
print x,"\n",y
combined,component = dist(x,y)
#combined = dist(x,y,'euclidean')
print "combined:",combined,"\n"
print "component:",component,"\n"
