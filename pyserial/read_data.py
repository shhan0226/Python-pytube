# -*- coding: utf-8 -*-




f = open('/data/power_data/sqminiH_bmc', 'r')


sum_ = 0
max_ = 0
min_ = 100
count = 0

lines = f.readlines()
for line in lines:
    if "get_Target_Watt: Target: +5V SB" in line:
       count += 1
       list_str=list(line.strip().split(' ')) 
       result = float(list_str[9][:-1])
       print(result,  ", " , count)
       sum_ += result
       if max_ < result: max_ = result
       if min_ > result: min_ = result
    else:
       count +=1
       list_str =list(line[26:31])
       list_str.insert(2, '.')
       list_str = ''.join(list_str)
       result = float(list_str)
       print(result,  ", " , count)
       sum_ += result
       if max_ < result: max_ = result
       if min_ > result: min_ = result


print("평균 " , sum_ / count)
print("최대 " , max_)
print("최소 " , min_)

f.close()
