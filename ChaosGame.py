#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 14:42:24 2021

@author: nounou
"""


#Startpunkt (muss nicht random sein)
#Drei Punkte mit Vorschrift für random
#Punkt generieren
#Teile Punkte in x & y-Komponente auf 





import numpy as np
import matplotlib.pyplot as plt
import random as rd


A = [0,0]
B = [2,0]
C = [1,1]

xP = [0,2,1]
yP = [0,0,1]




StartPunkt = [0.5, 1]
Punkt = StartPunkt

Iterations = int(input("How many iterations ?"))


xGesamt = []
yGesamt = []

for i in range(Iterations):
    #j =  rd.randrange(0, 2, 1)
    j = rd.randint(0,2)

    xPunkt = xP[j]
    yPunkt = yP[j]
    xVorPunkt = Punkt[0]
    yVorPunkt = Punkt[1]
    xneu = (xPunkt + xVorPunkt)/2
    yneu = (yPunkt + yVorPunkt)/2
    Punkt = [xneu,yneu]
    xGesamt.append(xneu)
    yGesamt.append(yneu)
    #print("Punkt = ", Punkt)


plt.scatter(xGesamt, yGesamt, s = .01)
plt.xlim(0,2)
plt.ylim(0,2)
plt.show()

    
    




