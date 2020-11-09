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

def multi_frac(z1,n1,z2,n2):
    d=[z1*z2]
    e=[n1*n2]
    f=[d[0],e[0]]
    return f

def sub_frac(z1,n1,z2,n2):
    g=[z1*n2,n1*n2]
    h=[z2*n1,n2*n1]
    i=[g[0]-h[0],g[1]]
    return i

def div_frac(z1,n1,z2,n2):
    j=[z1*n2]
    k=[z2*n1]
    l=[j[0],k[0]]
    return l