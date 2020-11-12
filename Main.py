# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:27:33 2020

@author: Luis Carlos Absalón Rojas Torres
e-mail: luiscarlos.bsf@gmail.com

Parameters:
    min. well head connected: minWHC
    max. well head connected: maxWHC
    clearance: clearance
    maximum gathering line length: maxGLL
    
Main Class:
    System(fileName.csv,posXFloatingUnit=0,posYFloatingUnit=0,minWHC=0,maxWHC=10,clearance=0,maxGLL=inf))
"""

from PointXY import *
from WellHeads import *
from Manifold import *
from System import *
import matplotlib.pyplot as plt

#System(fileName.csv,posXFloatingUnit=0,posYFloatingUnit=0,minWHC=0,maxWHC=10,clearance=0,maxGLL=inf))
Rojas = System('Data.csv',2.5,0)



print(Rojas.distanceFromFUtoManifold(Rojas.MG))



