from utils import *
from analyze import *
import numpy

data_dab = full_data(1493500380,1,True)
data_not_dab = full_data(1493500936,1,False)
data_dab_1 = full_data(1493500659,2,True)

id_str = 'accelerometer'
data_dab[id_str] = data_dab[id_str][100:]
data_dab_1[id_str] = data_dab_1[id_str][100:]
data_not_dab[id_str] = data_not_dab[id_str][100:]


diff_combined,component = dist(data_dab[id_str],data_not_dab[id_str])
same_combined,component = dist(data_dab[id_str],data_dab_1[id_str])
diff_combined_1,component = dist(data_dab_1[id_str],data_not_dab[id_str])

plot(diff_combined,same_combined,diff_combined_1)
