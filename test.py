# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 01:24:18 2020

@author: Luis Carlos Absalón Rojas Torres
e-mail: luiscarlos.bsf@gmail.com
Parameters:
    min. well head connected: minWHC
    max. well head connected: maxWHC
    clearance: clearance
    maximum gathering line length: maxGLL
"""
import random,math
import numpy as np
from WellHeads import *

listaDeWells = WellHeads('DataKmeans.csv')
listaDeWells.plot()
plt.grid()


   
def betterKmeans(listOfPointXY,numberOfManifolds,minWHC=0,maxWHC=10,ite=5):
    ''' Return the list of Points for numberOfManifold
    '''
    minNumManifolds = math.floor(len(listOfPointXY)/maxWHC)
    maxNumManifolds = int(len(listOfPointXY)/minWHC)
    
    #First step: calculate the range for the number of Manifolds 
    if( numberOfManifolds < minNumManifolds or numberOfManifolds > maxNumManifolds):
        print('Impossible solution: Please insert a number of Manifolds between '+ \
              str(minNumManifolds)+' and '+str(maxNumManifolds))
        return None
    
    #These list will allocate the posible locations of the manifolds
    manifoldLocations = list()    
    listOfPointsForEachManifold = list()
    
    #The initial locations of the manifolds will be at the same position of 
    #"numberOfManifolds" points from listOfPointXY randomly choosed
    print('Locs Iniciales: ')
    randomNumbers = list()
    #This while avoids to choose the same Point
    while(len(randomNumbers) < numberOfManifolds):
        shoot = random.randint(0,len(listOfPointXY)-1)
        #print('Sorteo: '+str(shoot))
        if(shoot not in randomNumbers):
            randomNumbers.append(shoot)
            #print(listOfPointXY[shoot])
            manifoldLocations.append(listOfPointXY[shoot])
            listOfPointsForEachManifold.append(list())
        
    #The iterations begin        
    for i in range(ite):
        print('Iteracion: '+str(i))
        for point in listOfPointXY:
            dmin = math.inf
            index=0
            
            for j in range(len(manifoldLocations)):
                if(point.distance(manifoldLocations[j]) < dmin):
                    dmin = point.distance(manifoldLocations[j])
                    index = j
                    
            listOfPointsForEachManifold[index].append(point)
            
        
        for j in range(len(listOfPointsForEachManifold)):
            manifoldLocations[j] = getPointCG(listOfPointsForEachManifold[j])
            if(i<ite-1):
                listOfPointsForEachManifold[j].clear()
            #manifoldLocations[j].plot()
            
            print(manifoldLocations[j])
    for manifoldPoint in manifoldLocations:
        manifoldPoint.plot()
    
    return listOfPointsForEachManifold
    

def getPointCG(listOfPoints):
    '''Determines the Centroid of N points'''
    cg = PointXY(0,0,listOfPoints[0].function)
        
    for i in listOfPoints:
        cg.posX += i.posX
        cg.posY += i.posY
    cg.posX/=len(listOfPoints)
    cg.posY/=len(listOfPoints)
    return cg    

lista = betterKmeans(listaDeWells.listProduction,3,3,5)    