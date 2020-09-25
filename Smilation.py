# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
R = random.randint(0,1)   #0 or 1

Pare = 0   #
S = 0   #
W = 0   #Win
L = 0   #Lose
N = 100   #Number of try
H = 0   #Starting number

#Simulation
for H in N:
    print(H+1,"回目", "",Pare[S])
    R = random.randint(0,1)
    if T==1:   #Win case
        W=W+1
        P=Pare[S]*Lever*B
        S=S+1   #Win > +1
        if S==C:
            S=1
    else:
        L=L+1
        P=Pare[S]*-Lever*B
        if S>=1:
            S=1   #Lose Stage1
            
    U=U+P
    print("出目",T,"勝ち数",W,"負け数",L,"決済",P,"合計収支",U)
    print("")