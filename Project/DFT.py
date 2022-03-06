# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 16:20:33 2021

@author: user
"""

import scipy as sc
import matplotlib.pyplot as plt
import numpy as np

def unos():
    i=0;
    x=np.array([]);
    N=int(input("Unesite dužinu sekvence: "));
    print("Unesite sekvencu (broj po broj): ");
    while(i<N):
        print("x(",i,")="); 
        broj=float(input());
        x=(np.insert(x,i,broj))
        i=i+1;
    return x;

def dft(x):
    n=sc.arange(0,len(x),1)
    plt.figure(1)
    plt.stem(n,x);
    plt.xlabel("n");
    plt.title("ULAZNA SEKVENCA")
    plt.grid();
    
    N=len(x);
    X_f=sc.fft(x);
    
    n1=sc.linspace(0,sc.pi*2,N+1);
    n1=n1[:-1];

    plt.figure(2);
    plt.stem(n1,X_f);
    plt.title("DFT UNESENE SEKVENCE")
    print("DFT= ",X_f);
    plt.xlabel("k")
    plt.grid();
    
def idft(x):
    n=sc.arange(0,len(x),1)
    plt.figure(1)
    plt.stem(n,x);
    plt.xlabel("k");
    plt.title("UNESENA SEKVENCA")
    plt.grid();

    N=len(x);
    X_f=sc.ifft(x);

    n1=sc.linspace(0,sc.pi*2,N+1);
    n1=n1[:-1];
    
    plt.figure(2);
    plt.stem(n1,X_f);
    plt.title("IDFT UNESENE SEKVENCE ")
    print("IDFT= ",X_f);
    plt.xlabel("n")
    plt.grid();