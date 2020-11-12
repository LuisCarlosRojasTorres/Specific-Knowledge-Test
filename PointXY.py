# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:23:17 2020

@author: Luis Carlos Absalón Rojas Torres
e-mail: luiscarlos.bsf@gmail.com
"""
import numpy as np
import csv
import matplotlib.pyplot as plt
class PointXY:
             
    def __init__(self,posX,posY,function):
        self.posX = posX
        self.posY = posY
        self.function = function 
        
    def distance(self,givenPoint):
        '''Calculates the distance between from this point to a givenPoint'''
        #if(self.function == givenPoint.function):
        distX = (self.posX-givenPoint.posX)
        distY = (self.posY-givenPoint.posY)
        return (distX**2+distY**2)**0.5
        #else:
        #    return 0.0
    
    
    #Visualization
    def plot(self):
        plt.scatter(self.posX, self.posY,c='black',marker='*')
    
    def __str__(self):
        return '>> ('+str(self.posX)+' , '+str(self.posY)+')  Function: ' + self.function 
    
def distance(pointA, pointB):
    '''Calculates the distance between two points: PointA and PointB'''
    #if(pointA.function == pointB.function):
    distX = (pointA.posX-pointB.posX)
    distY = (pointA.posY-pointB.posY)
    return (distX**2+distY**2)**0.5
    #else:
    #    return 0.0


def getData(fileName):
    '''Upload all the data from a CSV file'''
    lista = list()
    with open(fileName,'r',newline = '') as archivo:
        filas = csv.reader(archivo)
        for fila in filas:
            P = PointXY(float(fila[0]),float(fila[1]),fila[2])
            lista.append(P)
    
    return lista


    