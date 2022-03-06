# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:44:55 2021

@author: user
"""

import numpy as np
import simpy
from plot_zplane import zplane
#import matplotlib.pyplot as plt
import scipy.signal as sc

def unos_polova():
    i=0;
    x=np.array([]);
    N=int(input("Unesite broj polova (//Ako imamo npr: 1+ z^-3 to je N=4): "));
    print("Unesite polove (broj po broj): ");
    while(i<N):
        if(i==0):
            print("z^",i,"="); 
        else:
            print("z^-",i,"="); 
        broj=float(input());
        x=(np.insert(x,i,broj))
        i=i+1;
    return x;

def unos_nula():
    i=0;
    x=np.array([]);
    N=int(input("Unesite broj nula(//Ako imamo npr: 1+z^-3 to je N=4): "));
    print("Unesite sekvencu (broj po broj): ");
    while(i<N):
        if(i==0):
            print("z^",i,"="); 
        else:
            print("z^-",i,"="); 
        broj=float(input());
        x=(np.insert(x,i,broj))
        i=i+1;
        
    return x;

def i_z_tr(polovi,nule):

    zplane(polovi,nule)
    print(sc.residuez(nule,polovi))

