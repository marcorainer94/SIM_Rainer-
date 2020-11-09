# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:27:58 2020

@author: Marco
"""

def add_frac(z1,n1,z2,n2):
    a=[z1*n2,n1*n2]
    b=[z2*n1,n2*n1]
    c=[a[0]+b[0],a[1]]
    return a,b,c




