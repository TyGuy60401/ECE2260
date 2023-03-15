import numpy as np
delta_t_list = [60, 28, 17.6, 12.8, 10.4, 8.8, 7.2, 6.2, 5.7, 5, 4.5, 4.12, 3.18, 3.14, 3.24, 3, 2.8, 2.72, 2.56, 2.36]
delta_t_micro = []
frequency_list = np.arange(5000, 100001, 5000)
print(frequency_list)

for val in delta_t_list:
    delta_t_micro.append(val*1E-6)

for i in range(len(delta_t_list)):
    print(frequency_list[i], round(delta_t_micro[i] * frequency_list[i] * 360, 2), sep='\t')