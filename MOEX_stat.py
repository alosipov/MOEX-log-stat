import math

newDict = {}
# читаем построчно лог и наполняем словарь событие:время
with open('C:\\Tasks\\mtesrl_20150626_MD0000600002_stats.txt', 'r') as f:    
    for line in f:
        if line != '\n':
            l = line.split('\t')            
            if len(l) == 16:                
                event_str = l[1]        
                avgtsmr_string = int(l[15].rstrip())
                if event_str in newDict:
                    newDict[event_str].append(int(avgtsmr_string))
                else:
                    newDict[event_str] = [int(avgtsmr_string)]

for v in newDict.values():
    v = v.sort()
percintele = [0.5, 0.90, 0.99, 0.999]
index = []
# выполняем необходимые подсчеты
for v in newDict.values():
    
    for p in percintele:
        p1 = len(v) * p
        p1_sep = math.modf(p1)
        if p1_sep[0] > 0:
            index.append(int(p1_sep[1]))
        elif p1_sep[0] == 0:
            index.append(int(p1_sep[1]) - 1)

i = 0

# выводим результирующую  строку и таблицу
for k, v in newDict.items():
    
    print(k, "min={}".format(v[0]), "50%={}".format(v[index[i]]), "90%={}".format(v[index[i+1]]),\
         "99%={}".format(v[index[i+2]]), "99.9%={}".format(v[index[i+3]]))
    i = i+4
    
    
    t_current = v[0] 
    next_index_to_process = 0 
    count_total = len(v) 
    count_weight = 0 
    count_percent = 0 
    
    print('________________________________________________')
    print('ExecTime', 'TransNo', 'Weight,%', 'Percent')
    
    while next_index_to_process < count_total:
        if v[next_index_to_process] <= t_current:
            count_weight = count_weight + 1
            next_index_to_process = next_index_to_process + 1
        else:
            exectime = t_current
            transNo = count_weight
            weight = round((count_weight/count_total * 100), 2)
            count_percent = count_percent + count_weight
            percent = round((count_percent/count_total * 100), 2)            
            if count_weight >0:
                print(str(exectime) + '\t', str(transNo) + '\t', str(weight) + '\t', str(percent) + '\t') 

            t_new = (int(t_current/5) + 1) * 5    
            t_current = t_new
            count_weight = 0
        
    exectime = t_current
    transNo = count_weight
    weight = round((count_weight/count_total * 100), 2)
    count_percent = count_percent + count_weight
    percent = round((count_percent/count_total * 100), 2) 
    if count_weight >0:
        print(str(exectime) + '\t', str(transNo) + '\t', str(weight) + '\t', str(percent) + '\t') 
        print("\n")
    
            
    
    
