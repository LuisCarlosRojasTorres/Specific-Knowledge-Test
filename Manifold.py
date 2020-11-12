# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:23:53 2020

@author: Luis Carlos Absalón Rojas Torres
e-mail: luiscarlos.bsf@gmail.com

Parameters:
    min. well head connected: minWHC
    max. well head connected: maxWHC
    clearance: clearance
    maximum gathering line length: maxGLL

"""
from math import inf
from PointXY import *
import matplotlib.pyplot as plt

class Manifold:
    '''Class takes a list of wellhead with the same function'''
    def __init__(self,listOfPoints,clearance=0,maxGLL=inf):
        self.listOfPoints = listOfPoints
        self.clearance = clearance
        self.maxGLL = maxGLL
        self.position = self.getCG()
        #self.plot()
        #Calculate the length of flowlines
        self.getInitialLengthOfGathLines()
        #Calculates the optimum location to minimize the length of flowlines
        self.optimize()
        self.plot()
        
    def getInitialLengthOfGathLines(self):
        '''Determines the Length of the Flowlines for a manifold located at the CENTROID'''
        self.lengthOfGathLines = 0
        
        for i in self.listOfPoints:
            #print('distancia: '+str(self.position.distance(i)))
            if(self.position.distance(i) < self.clearance or self.position.distance(i) > self.maxGLL):
                self.lengthOfGathLines = inf
                return  self.lengthOfGathLines
            
            self.lengthOfGathLines += self.position.distance(i)
        #print('From Centroid: '+ str(self.lengthOfFlowLines))
        return self.lengthOfGathLines
    
    def getLengthOfGathLines(self,dummyPoint):
        '''Determines the Length of the Flowlines for a manifold located at a dummyPoint'''
        dummyFlowLines = 0
        
        for i in self.listOfPoints:
            #print('distancia: '+str(dummyPoint.distance(i)))
            if(dummyPoint.distance(i) < self.clearance or dummyPoint.distance(i) > self.maxGLL):
                return inf
            dummyFlowLines += dummyPoint.distance(i)
        #print('Total length: '+ str(dummyFlowLines))
        return dummyFlowLines
    
    
    def optimize(self,meshSizeX=50,meshSizeY=50):
        '''Determine the best position for the manifold'''
        (minX,maxX,minY,maxY) = self.getLimits()
        arrayX = np.linspace(minX, maxX,meshSizeX)
        arrayY = np.linspace(minY, maxY,meshSizeY)
        
        for i in arrayX:
            #print('New tentative')
            #print(' i : '+str(i))
            for j in arrayY:
                #print(' j:')
                dummyPoint = PointXY(i,j,self.position.function)
                #print(dummyPoint)
                if (self.lengthOfGathLines > self.getLengthOfGathLines(dummyPoint)):
                    #print('NEW POSITION FOUND')
                    #print('old:' + str(self.lengthOfFlowLines)+ ' new: '+ str(self.getLengthOfGathLines(dummyPoint)))
                    self.position = dummyPoint
                    self.lengthOfGathLines = self.getLengthOfGathLines(dummyPoint)
        #print('NEW POSITION FOUND')
        #print('New total length:' + str(self.lengthOfFlowLines))
        
        
                
    def getLimits(self):
        '''Determines the region to look for the optimum location of the manifold'''            
        minX = self.listOfPoints[0].posX
        maxX = self.listOfPoints[0].posX
        minY = self.listOfPoints[0].posY
        maxY = self.listOfPoints[0].posY
        
        for i in self.listOfPoints:
            if minX > i.posX :
                minX = i.posX
            if minY > i.posY :
                minY = i.posY
            if maxX < i.posX :
                maxX = i.posX
            if maxY < i.posY :
                maxY = i.posY
        return (minX-self.clearance,maxX+self.clearance,minY-self.clearance,maxY+self.clearance)
            
    def plot(self):
        if self.position.function == 'Production':
            plt.scatter(self.position.posX, self.position.posY,c='green',marker='s')
        elif self.position.function == 'Water Injection':    
            plt.scatter(self.position.posX, self.position.posY,c='red',marker='s')
        elif self.position.function == 'Gas Injection':    
            plt.scatter(self.position.posX, self.position.posY,c='blue',marker='s')
        else:
            plt.scatter(self.position.posX, self.position.posY,c='black',marker='s')
        
    def getCG(self):
        '''Determines the Centroid of N points'''
        cg = PointXY(0,0,self.listOfPoints[0].function)
        
        for i in self.listOfPoints:
            cg.posX += i.posX
            cg.posY += i.posY
        cg.posX/=len(self.listOfPoints)
        cg.posY/=len(self.listOfPoints)
        return cg
        
              
            
        
        