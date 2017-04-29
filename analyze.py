import numpy as np
import scipy
import scipy.spatial

def dist(x,y,n,metric):
    #computes the absolute distance between two time sample multi-field data vectors
    #x: first vector (numpy array)
    #y: second vector (numpy array)
    #n: number of fields in each one (int)
    #metric: distance metric to use (string)

    #indexing the vectors: x[time_point][field]

    time_points_x = x.shape[0]
    time_points_y = y.shape[0]
    time_points = np.minimum(time_points_x,time_points_y)

    combined_distance = np.zeros((time_points))
    component_distance = np.zeros((time_points,n))

    for i in range(time_points):
        combined_distance[i] = scipy.spatial.distance.cdist(y[i],x[i],metric)
        component_distance[i] = np.abs(y[i]-x[i])

    return combined_distance,component_distance

x = np.zeros((5,3))
y = np.zeros((5,3))

for i in range(5):
    for j in range(3):
        x[i,j] = i+j
        y[i,j] = i-j

combined,component = dist(x,y,3,'euclidean')

print "combined:",combined,"\n"
print "component:",component,"\n"
