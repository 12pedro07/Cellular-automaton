import numpy as np
import random
import time

size = 151
v = []
for cont in range(size):
    if cont == round(size/2):
        v.append('#')
    else:
        v.append(' ')

rule = input("chose the rule [0 to 255] (I recomend 82): ")
rule = int(rule)
while rule > 255 or rule < 0:
    rule = input("chose the rule [0 to 255]: ")
    rule = int(rule)
rule = ('{0:08b}'.format(rule))
print('\n --------> Binary rule chosen: ' + str(rule) + '\n')

def list2string(v):
    string = ''
    for m in range(size):
            if m == size-1:
                string = string + str(v[m])
                string = string + '\n'
            else:
                string = string + v[m]
    return string

def analysis(l,m,r):
    # print("l : "+ l + "\n")
    # print("m : "+ m + "\n")
    # print("r : "+ r + "\n")
    if ((l == ' ') and (m == ' ') and (r == ' ')): return rule[7]
    if ((l == ' ') and (m == ' ') and (r == '#')): return rule[6]
    if ((l == ' ') and (m == '#') and (r == ' ')): return rule[5]
    if ((l == ' ') and (m == '#') and (r == '#')): return rule[4]
    if ((l == '#') and (m == ' ') and (r == ' ')): return rule[3]
    if ((l == '#') and (m == ' ') and (r == '#')): return rule[2]
    if ((l == '#') and (m == '#') and (r == ' ')): return rule[1]
    if ((l == '#') and (m == '#') and (r == '#')): return rule[0]
    else: return 3

while True:
    printoso = list2string(v)
    print(printoso)
    nxt = []
    for i in range(len(v)):
        if ((i == 0) or (i == len(v)-1)):
            aux = ' '
        else:
            # print('sending' + v[i-1] + 'and' + v[i] + 'and' + v[i+1] + 'to analysis')
            aux = analysis(v[i-1],v[i],v[i+1])
            # print ('aux = '+str(aux))
            # print ('rule[0] = '+ str(rule[0]))
            # print(v[i]==' ')
            # print(v[i-1], v[i], v[i+1])
            if aux == str(0):
                aux = ' '
            elif aux == str(1):
                aux = '#'
            # else: aux = ' ---> loucuras da amanda <---
        nxt.append(aux)
    # print('\n'#3)
    v = nxt
    time.sleep(0.4)
