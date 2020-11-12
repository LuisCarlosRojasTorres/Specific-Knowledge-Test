# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:14:15 2020

@author: Luis Carlos Absalón Rojas Torres
e-mail: luiscarlos.bsf@gmail.com
"""
from PointXY import *
import matplotlib.pyplot as plt

class WellHeads:
    '''This class creates three list each one for a different function
            listProduction     = Production WellHeads
            listWaterInjection = Water Injection WellHeads
            listGasInjection   = Gas Injectopm WellHeads
    '''
    def __init__(self,fileName):
        self.listProduction = list()
        self.listWaterInjection = list()
        self.listGasInjection = list()
        
        self.setWellHead(getData(fileName))
        self.printAll()
        self.plot()
        
    
    def addWellHead(self,pointXY):
        '''Adds a wellhead to its respective list'''
        if(pointXY.function == 'Production'):
            self.listProduction.append(pointXY)
        
        elif (pointXY.function == 'Water Injection'):
            self.listWaterInjection.append(pointXY)
        
        elif (pointXY.function == 'Gas Injection'):
            self.listGasInjection.append(pointXY)
        else:
            print(" ERROR no coincidence!!!" + pointXY.function)
     
    def setWellHead(self,listOfPoints):
        '''
        Adiciona los pozos segun du funcion a la lista de WellHeads
        listOfPoints es una lista de objetos PointXY 
        '''
        for i in listOfPoints:
            self.addWellHead(i)
    
    def getList(self,function):
        '''
        Return one of the list of wellheads to construct the manifolds
        '''
        if (function == 'Production'):
            return self.listProduction
        if (function == 'Water Injection'):
            return self.listWaterInjection
        if (function == 'Gas Injection'):
            return self.listGasInjection
            
    #Visualization
    def getXY(self,function):
        '''
        Creates the list of X and Y to plot in SCATTER mode
        '''
        listX = list()
        listY = list()
        
        if(function == 'Production'):
            for i in self.listProduction:
                listX.append(i.posX)
                listY.append(i.posY)
        elif(function == 'Water Injection'):
            for i in self.listWaterInjection:
                listX.append(i.posX)
                listY.append(i.posY)
        elif(function == 'Gas Injection'):
            for i in self.listGasInjection:
                listX.append(i.posX)
                listY.append(i.posY)
        return (listX,listY)
    
    def plot(self):
        
        plt.scatter(self.getXY('Production')[0], self.getXY('Production')[1],c='green',marker='o')
        plt.scatter(self.getXY('Water Injection')[0], self.getXY('Water Injection')[1],c='red',marker='o')
        plt.scatter(self.getXY('Gas Injection')[0], self.getXY('Gas Injection')[1],c='blue',marker='o')
        plt.grid()
        
    def printAll(self):
        print('All wellheads uploaded:')
        print('-----------------------')
        for i in self.listProduction:
            print(i)
        print()
        for i in self.listWaterInjection:
            print(i)
        print()
        for i in self.listGasInjection:
            print(i)
       
            
        
        
    
    