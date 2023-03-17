import numpy as np
delta_t_list = [60, 28, 17.6, 12.8, 10.4, 8.8, 7.2, 6.2, 5.7, 5, 4.5, 4.12, 3.18, 3.14, 3.24, 3, 2.8, 2.72, 2.56, 2.36]
delta_t_list = [-220, -116, -58, -25, -8.6, -.68, 2.48, 3.48, 2.76, 2.04]
delta_t_micro = []
frequency_list = [1000.0, 1700.0, 2800.0, 4600.0, 7700.0, 12900.0, 21500.0, 35900.0, 59900.0, 100000.0]
print(frequency_list)

for val in delta_t_list:
    delta_t_micro.append(val*1E-6)

for i in range(len(delta_t_list)):
    print(frequency_list[i], round(delta_t_micro[i] * frequency_list[i] * 360, 2), sep='\t')
for i in range(len(delta_t_list)):
    print(round(delta_t_micro[i] * frequency_list[i] * 360, 2), sep='\t')