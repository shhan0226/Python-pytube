# -*- coding: utf-8 -*-




f = open('/data/sq_mini_data/result_pec_run', 'r')


sum_ = 0
max_ = 0
min_ = 100
count = 0

lines = f.readlines()
for line in lines:
    if "main: Total Power:" in line:
       count += 1
       string=list(line.strip().split(' ')) 
       result = float(string[3][:-1])
       #print(result,  ", " , count)
       sum_ += result
       if max_ < result: max_ = result
       if min_ > result: min_ = result



print(max_)
print(min_)
print(sum_ / count)

f.close()
