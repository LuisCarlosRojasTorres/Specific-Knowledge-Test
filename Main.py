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

#Because i didnt have enough time i could not automatizate the calculations of number of manifold

nummberOfManifoldForProductionWH = 2
nummberOfManifoldForWaterInjectionWH = 2
nummberOfManifoldForGasInjectionWH = 2



#System(fileName.csv,posXFloatingUnit=0,posYFloatingUnit=0,minWHC=0,maxWHC=10,clearance=0,maxGLL=inf))
Rojas = System('Data.csv',2.5,0)

#All the well heads are divided into three list for each function
listOfProductionWellHeads = Rojas.listOfWellHeads.getList('Production')
listOfWaterInjectionWellHeads = Rojas.listOfWellHeads.getList('Water Injection')
listOfGasInjectionWellHeads = Rojas.listOfWellHeads.getList('Gas Injection')


#Determines the listOfPoints for every manifold
listOfProductionManifoldPoints = Rojas.betterKmeans(listOfProductionWellHeads,nummberOfManifoldForProductionWH)
listOfWaterInjectionManifoldPoints = Rojas.betterKmeans(listOfWaterInjectionWellHeads,nummberOfManifoldForWaterInjectionWH)
listOfGasInjectionManifoldPoints = Rojas.betterKmeans(listOfGasInjectionWellHeads,nummberOfManifoldForGasInjectionWH)    
 
#Since we have the well heads for every manifold it is posible to INITIALIZE each manifold
listOfProductionManifold=list()
for i in listOfProductionManifoldPoints:
    listOfProductionManifold.append(Manifold(i))

listOfWaterInjectionManifold=list()
for i in listOfWaterInjectionManifoldPoints:
    listOfWaterInjectionManifold.append(Manifold(i))

listOfGasInjectionManifold=list()
for i in listOfGasInjectionManifoldPoints:
    listOfGasInjectionManifold.append(Manifold(i))


#Calculate the total sum of gathering lines:
totalGatheringLength = 0

for i in listOfProductionManifold:
    totalGatheringLength += i.lengthOfGathLines
for i in listOfWaterInjectionManifold:
    totalGatheringLength += i.lengthOfGathLines
for i in listOfGasInjectionManifold:
    totalGatheringLength += i.lengthOfGathLines
    


#Calculates the total sum of flow Lines:

totalFlowLength = 0
print()
print("Production Manifold: ")
for i in listOfProductionManifold:
    print(i.position)
    totalFlowLength += Rojas.distanceFromFUtoManifold(i)
print()
print("Water Injection Manifold: ")
for i in listOfWaterInjectionManifold:
    
    print(i.position)
    totalFlowLength += Rojas.distanceFromFUtoManifold(i)
print()
print("Gas Injection Manifold: ")
for i in listOfGasInjectionManifold:
    print(i.position)
    totalFlowLength += Rojas.distanceFromFUtoManifold(i)
print()
print('Total of gathering lines: '+str(totalGatheringLength))
print('Total of flow lines: ' + str(totalFlowLength))
