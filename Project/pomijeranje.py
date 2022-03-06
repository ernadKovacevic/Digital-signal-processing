# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:34:43 2021

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt

def unos():
    
    p=int(input("unos pocetka x ose: "));
    k=int(input("unos kraja x ose: "));
    n=np.arange(p,k+1,1);
    i=0;
    temp=p
    x=np.array([]);
    N=len(n);
    while(i<N):
    
        print("x(",temp,")="); 
        broj=float(input());
        x=(np.insert(x,i,broj))
        temp=temp+1;
        i=i+1;
    
    move=int(input("Koliko zelite pomjeriti sekvencu: "))
    
    plt.figure(1);
    plt.stem(n,x);
    plt.title("Unesena sekvenca")
    plt.xlabel("n");
    plt.grid();
    
    if(move<0):
        plt.figure(2);
        plt.stem(n-move,x);
        plt.title("Pomjerena sekvenca")
        plt.xlabel("n");
        plt.grid()
    else:
        plt.figure(2);
        plt.stem(n-move,x);
        plt.title("Pomjerena sekvenca")
        plt.xlabel("n");
        plt.grid()
        
        
        
    """
   i=0;
    while(i<abs(move)):
        if(move<0):
            n_=np.arange(p,k+1-move,1)
            x=np.insert(x,0,0);
        else:
            n_=np.arange(p-move,k+1,1)
            x=np.insert(x,len(x),0);
        i=i+1;   
    
    plt.figure(2);
    plt.stem(n_,x);
    plt.title("Pomjerena sekvenca")
    plt.xlabel("n");
    plt.grid();
        
    """
    

