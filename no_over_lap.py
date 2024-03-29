import sys
import numpy as np
import time
start_time = time.time()
stoppoints = []
max_sensor_stoppoints = 0 # record the stoppoints with maximum sensors.
energy = int(sys.argv[1]) #TODO
Filename = sys.argv[2]
with open(Filename) as f:
    for line in f.readlines():
        sensors = line.split()
        weights = [int(x) for x in sensors]
        #weights.sort(reverse=True)
        stoppoints.append(weights)
        max_sensor_stoppoints = max(max_sensor_stoppoints,len(weights))
matrix = np.zeros((len(stoppoints),max_sensor_stoppoints))
for i in range(len(stoppoints)):
    matrix[i,:len(stoppoints[i])]=stoppoints[i]

non_zero_matrix = matrix > 0


total_collected_data = 0

hovering_time = [0]*len(stoppoints)

for i in range(energy):
    collected_datas = non_zero_matrix.sum(axis = 1)
    stoppoint = np.argmax(collected_datas)
    total_collected_data += collected_datas[stoppoint]
    matrix[stoppoint] = matrix[stoppoint]-1
    non_zero_matrix = matrix > 0
    hovering_time[stoppoint] = hovering_time[stoppoint] + 1

print("{},{},{}".format(Filename,total_collected_data,time.time() - start_time))