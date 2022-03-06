# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:23:01 2021

@author: user
"""
import matplotlib.pyplot as plt
import numpy as np
import DFT
import Z
import pomijeranje
choose=6;

while(choose<1 or choose>5):
    print("Pozdrav!!!\n 1. DFT  \n 2. IDFT \n 3. Inv. Z transformacija \n 4. Pomijeranje sekvence (n+-broj, prikaz) \n 5. Exit")
    choose=int(input("Izaberite funkciju: "));    
    if(choose == 1):
        sekvenca=DFT.unos()
        DFT.dft(sekvenca);
    elif (choose == 2):
        sekvenca=DFT.unos()
        DFT.idft(sekvenca)
    elif (choose == 3):
        p=Z.unos_polova()
        n=Z.unos_nula()
        Z.i_z_tr(p,n)
    elif (choose ==4):
        pomijeranje.unos()
    elif(choose ==5):
        print("Dovidjenja");
        break;
    else:
        print("Pogrešan unos \n");



