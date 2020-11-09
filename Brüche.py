# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:27:58 2020

@author: Marco
"""

def add_frac(z1,n1,z2,n2):
    a=[z1*n2,n1*n2]
    b=[z2*n1,n2*n1]
    c=[a[0]+b[0],a[1]]
    return c

while True:
    try:
        z1=int(input("Geben Sie den ersten Zähler als ganze Zahl ein: "))
        break 
    except ValueError:
        print("Das ist keine ganze Zahl! Bitte nochmals versuchen!")
        
while True:
    try:
        n1=int(input("Geben Sie den ersten Nenner als ganze Zahl ein: "))
        break 
    except ValueError:
        print("Das ist keine ganze Zahl! Bitte nochmals versuchen!")

while True:
    try:
        z2=int(input("Geben Sie den zweiten Zähler als ganze Zahl ein: "))
        break 
    except ValueError:
        print("Das ist keine ganze Zahl! Bitte nochmals versuchen!")
        
while True:
    try:
        n2=int(input("Geben Sie den zweiten Nenner als ganze Zahl ein: "))
        break 
    except ValueError:
        print("Das ist keine ganze Zahl! Bitte nochmals versuchen!")   
        

        
c=add_frac(z1,n1,z2,n2)
print("Zähler", c[0])
print("Nenner", c[1])
