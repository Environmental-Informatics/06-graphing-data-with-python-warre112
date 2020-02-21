#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les Warren
ABE 651- Lab #6 Graphing Data with Python
Created on Fri Feb 21 13:20:37 2020
Provides function to with user command to load data file, plot using mathplotlib, and save it to a pdf file

"""


import numpy #imports numpy package
from matplotlib import pyplot as plt #imports pyplot from matplotlib and defines it as "plt"


def file(x, y): #function to run three plots as specified before. Input requires two variables
    #x= input file name
    #y= output file name
      
    data= numpy.genfromtxt(x, names=True) #creates variable "data" and loads data from specified file in commmand line, names= header line is name ofeach array (column) 
    
    plt.figure() #plot multiple figures
    plt.subplot(311) #plot #1. 311= three rows, one column, first figure 
    plt.plot(data['Year'], data['Mean'], 'black', label= "Mean") #plot (y variable, x variable, color of line, label)
    plt.plot(data['Year'], data['Min'], 'blue', label= "Minimum") #plot (y variable, x variable, color of line, label)
    plt.plot(data['Year'], data['Max'], 'red', label= "Maximum") #plot (y variable, x variable, color of line, label)
    plt.legend() #command for legend to appear using labels 
    plt.xlabel("Year") #plots x axis label
    plt.ylabel("Streamflow (cfs)") #plots y axis label
    plt.show() #shows plot

    plt.subplot(312) #plot #2 312= three rows, one column, second plot (row)
    plt.plot(data['Year'], data['Tqmean']*100, "v") #plot(y,x, symbology)
    plt.xlabel("Year") #plots x axis label
    plt.ylabel("Tqmean (%)") #plots y axis label
    plt.show #shows plot

    plt.subplot(313) #plot #3 312= three rows, one column, third plot (row)
    plt.bar(data['Year'], data['RBindex']) #bar plot (x,y)
    plt.xlabel("Year") #plots x axis label
    plt.ylabel("R-B Index (ratio)") #plots y axis label
    plt.show #shows plot
    
    plt.savefig(y) #saves figure to specifed file name

file('Wildcat_Creek_at_Lafayette.Annual_Metrics.txt', 'Wildcat_Results.pdf') #runs function
file('Tippecanoe_River_at_Ora.Annual_Metrics.txt', 'Tippecanoe_Results.pdf') #runs function


    



