

'''
Time:        45     97     72     95
Distance:   305   1062   1110   1695
'''

races=[[45,305],[97,1062],[72,1110],[95,1695]]
races = [[45977295,305106211101695]]

num_of_ways_to_beat=[]
for race in races:
    local_result=0
    time = race[0]
    record=race[1]
    for i in range(time):
        distance= (time-i)*i
        if distance >record:
            local_result+=1
        if i %1000000==0: print(i)
    num_of_ways_to_beat.append(local_result)


total=1
for i in num_of_ways_to_beat:
    total*=i

print("P1:", total)



            



