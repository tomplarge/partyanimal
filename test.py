from utils import *
from analyze import *
import numpy

dab_id_nums = [1493500380,1493500659,1493510372,1493510494]
non_dab_id_nums = [1493500936,1493510560]

data_not_dab_1 = full_data(non_dab_id_nums[0],1,False)
data_not_dab_2 = full_data(non_dab_id_nums[1],2,False)
data_dab_1 = full_data(dab_id_nums[0],1,True)
data_dab_2 = full_data(dab_id_nums[1],2,True)
data_dab_3 = full_data(dab_id_nums[2],3,True)
data_dab_4 = full_data(dab_id_nums[3],4,True)

id_str = 'orientation'
#
plt.plot(data_dab_3[id_str],'g')
plt.plot(data_not_dab_2[id_str],'r')
plt.show()


data_dab_1[id_str] = data_dab_1[id_str][105:]
data_dab_2[id_str] = data_dab_2[id_str][85:]
data_dab_3[id_str] = data_dab_3[id_str][110:]
data_dab_4[id_str] = data_dab_4[id_str][150:]
data_not_dab_1[id_str] = data_not_dab_1[id_str][85:]
data_not_dab_2[id_str] = data_not_dab_2[id_str][100:]

same_combined1,component = dist(data_dab_1[id_str],data_dab_2[id_str])
same_combined2,component = dist(data_dab_1[id_str],data_dab_3[id_str])
same_combined3,component = dist(data_dab_1[id_str],data_dab_4[id_str])
same_combined4,component = dist(data_dab_2[id_str],data_dab_3[id_str])
same_combined5,component = dist(data_dab_2[id_str],data_dab_4[id_str])
same_combined6,component = dist(data_dab_3[id_str],data_dab_4[id_str])
diff_combined1,component = dist(data_dab_1[id_str],data_not_dab_1[id_str])
diff_combined2,component = dist(data_dab_1[id_str],data_not_dab_2[id_str])
diff_combined3,component = dist(data_dab_2[id_str],data_not_dab_1[id_str])
diff_combined4,component = dist(data_dab_2[id_str],data_not_dab_2[id_str])
diff_combined5,component = dist(data_dab_3[id_str],data_not_dab_1[id_str])
diff_combined6,component = dist(data_dab_3[id_str],data_not_dab_2[id_str])
diff_combined7,component = dist(data_dab_4[id_str],data_not_dab_1[id_str])
diff_combined8,component = dist(data_dab_4[id_str],data_not_dab_2[id_str])

plt.plot(same_combined1,'g')
plt.plot(same_combined2,'g')
plt.plot(same_combined3,'g')
plt.plot(same_combined4,'g')
plt.plot(same_combined5,'g')
plt.plot(same_combined6,'g')
plt.plot(diff_combined1,'r')
plt.plot(diff_combined2,'r')
plt.plot(diff_combined3,'r')
plt.plot(diff_combined4,'r')
plt.plot(diff_combined5,'r')
plt.plot(diff_combined6,'r')
plt.plot(diff_combined7,'r')
plt.plot(diff_combined8,'r')
plt.show()
