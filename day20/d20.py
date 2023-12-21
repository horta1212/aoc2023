# output agent, pulse_type, sending_agent
broadcaster =[ ['mn',0,'button'] , ['jn',0,'button'], ['hd',0,'button'], ['lq',0,'button']]

#label: [state, outputs...]
flops = {
'nz':[False,'jm', 'ms'],
'xk':[False,'cs', 'ks'],
'rh':[False,'ks'],
'ml':[False,'mf', 'ks'],
'mf':[False,'ks', 'km'],
'bk':[False,'zz', 'ks'],
'zf':[False,'dn'],
'qf':[False,'kf'],
'zv':[False,'mz', 'ms'],
'hd':[False,'dn', 'mm'],
'nv':[False,'pn', 'dn'],
'vz':[False,'pz', 'tc'],
'jl':[False,'ps'],
'lq':[False,'ms', 'fm'],
'fl':[False,'ms'],
'zz':[False,'ks', 'vd'],
'td':[False,'bj', 'tc'],
'vd':[False,'ks', 'ml'],
'cp':[False,'fl', 'ms'],
'jn':[False,'ks', 'xk'],
'xg':[False,'tc'],
'xs':[False,'zk'],
'kf':[False,'dz', 'dn'],
'qx':[False,'ks', 'rh'],
'kb':[False,'ms', 'tl'],
'mm':[False,'nv'],
'mn':[False,'tc', 'xs'],
'cs':[False,'gb'],
'jm':[False,'ms', 'cp'],
'bj':[False,'tc', 'xx'],
'pn':[False,'dn', 'jk'],
'fm':[False,'zv'],
'jk':[False,'nr'],
'pz':[False,'td', 'tc'],
'xx':[False,'tc', 'xg'],
'gb':[False,'bk', 'ks'],
'dz':[False,'zb', 'dn'],
'vl':[False,'jl', 'tc'],
'gx':[False,'ms', 'kb'],
'zb':[False,'dn', 'zf'],
'tl':[False,'pp', 'ms'],
'pp':[False,'nz', 'ms'],
'km':[False,'ks', 'qx'],
'ps':[False,'tc', 'vz'],
'mz':[False,'ms', 'gx'],
'hf':[False,'qf'],
'nr':[False,'hf'],
'zk':[False,'vl'],
}

conj = {
'ms':{'out':['lq', 'fm', 'sz'], 'in':{}},
'tc':{'out':['mn', 'xf', 'jl', 'xs', 'zk'], 'in':{}},
'gc':{'out':['zr'], 'in':{}},
'ks':{'out':['jn', 'cs', 'cm'], 'in':{}},
'dn':{'out':['jk', 'qf', 'gc', 'hf', 'hd', 'nr', 'mm'], 'in':{}},
'sz':{'out':['zr'], 'in':{}},
'cm':{'out':['zr'], 'in':{}},
'zr':{'out':['rx'], 'in':{}},
'xf':{'out':['zr'], 'in':{}},
}

'''
broadcaster = [['a',0,'button']]
flops = {'a':[False, 'inv','con'],
         'b':[False, 'con']
         }
conj = {'inv':{'out':['b'], 'in':{}},
        'con':{'out':['output'],'in':{}},
        }
'''

low_pulses = 0
high_pulses = 0

for flop_label, flop_outputs in flops.items():
    for output in flop_outputs:
        if output in conj.keys():
            conj[output]['in'][flop_label]=False

print(conj)

stop_all = False
for button in range(1,10001):
    if stop_all:
        break
    #print()
    pulse_list = broadcaster
    low_pulses+=1
    while len(pulse_list) != 0:
        #print(pulse_list)
        next_pulse_list = []
        for agent_action in pulse_list:
            agent = agent_action[0]
            pulse_type = agent_action[1]
            sender = agent_action[2]
            
            if pulse_type:
                high_pulses +=1
            else:
                low_pulses +=1

            #if agent in ['dn','ns','ks','tc'] and pulse_type == True:
            #    print('button_press:', button)
            #    print(agent_action)

            #if agent == 'zr':
            #    print(agent_action)
            if agent in ['gc','sz','cm','xf'] and pulse_type == False:
                print('button_press:', button)
                print(agent_action)
            
            if agent in flops.keys():
                if pulse_type == False:
                    flops[agent][0] = not(flops[agent][0])
                    for out_agent in flops[agent][1:]:
                        next_pulse_list.append([out_agent, flops[agent][0],agent])
                
            elif agent in conj.keys():
                conj[agent]['in'][sender]=pulse_type
                out_pulse = not set([x for x in conj[agent]['in'].values()]) == set([True])
                for out_agent in conj[agent]['out']:
                    next_pulse_list.append([out_agent, out_pulse, agent])

            else: 
                if pulse_type == False:
                    print('ERROR', agent_action)
                    print('agent',agent)
                    print('button_press:', button)
                    stop_all=True
        
        pulse_list = next_pulse_list
    if button % 10000==0:
        print('button_press:', button)

print('high_pulses', high_pulses)
print('low_pulses', low_pulses)
print('P1:', high_pulses * low_pulses)
#high_pulses 37986
#low_pulses 16664
#P1: 632998704
# Too low

