# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#https://vegas-online.jp/paray-martin/

import random
Pare = [1,2,4,8,16,32,64,128,256,512,1024,2048]   #Pare Main
S = 0      #現在のパーレーステージ 0 から
Deme = list(range(0))    #Deme list history
R = random.randint(0,1)   #出目 0 or 1
W = 0      #Win
L = 0      #Lose
N = range(1000)    #Number of maximum try
H = 0      #Starting number
T = 0      #前の出目
Lever = 100  #Leverage 掛け金
B = 1      #倍率
C = 0      #
U = 0      #合計収支　総合
P = 0      #収支計算用

#シュミレーション
for H in N:
    R = random.randint(0,1)
    Deme.append(R)   #Deme history
    print("ベッド数",Pare[S])    
    if R==1:    #Win case
        P=Pare[S]*Lever*B   #収支計算
        W=W+1   #勝ち数+１
    else:   #Lose case
        P=Pare[S]*-Lever*B   #収支計算
        L=L+1   #負け数追加
    
    #ステージ計算
    if H==0:   #H=0 初回のみ 
        S=S+1   #勝っても負けてもステージ２へ
    else:   #初回以外は
        if Deme[H-1]==Deme[H]:   #前回の出目が同じなら
            S=S+1   #追加で次のステージへ
        else:
            S=0     #負けから勝ったら１へ戻る       
    
    U=U+P   #合計収支計算
    print(H+1,"回目","出目",R,"収支",P,"収支合計",U)
 