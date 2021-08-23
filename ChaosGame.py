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


#x- and y-coordinates of three points that define our playground. [0, 0], [2, 0], [1, 1] respectively.

xP = [0,2,1]
yP = [0,0,1]



# Starting point

Point = [0.5, 1]


#Self explanatory

Iterations = int(input("How many iterations ?"))


#List of x- and y-coordinates of the calculated points

xTotal = []
yTotal = []


for i in range(Iterations):
    
    #chooses out target point at random
    j = rd.randint(0,2)

    xPoint = xP[j]
    yPoint = yP[j]
    xPre = Point[0]
    yPre = Point[1]
    xNew = (xPoint + xPre)/2
    yNew = (yPunkt + yPre)/2
    Point = [xNew,yNew]
    xTotal.append(xNew)
    yTotal.append(yNew)

#plots the the calculated pairs
plt.scatter(xTotal, yTotal, s = .01)
plt.xlim(0,2)
plt.ylim(0,2)
plt.show()

    
    




