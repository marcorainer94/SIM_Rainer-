# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:27:58 2020

@author: Marco
"""
#z1 and z1 for the numerator / n1 and n2 for the denominator
#gives the Addition of the two fractions
def add_frac(z1,n1,z2,n2):
    a=[z1*n2,n1*n2]
    b=[z2*n1,n2*n1]
    c=[a[0]+b[0],a[1]]  #a[1] to get the correct denominator
    return c            #returns two numbers / numerator and denominator 

#gives the Multiplication of the two fractions
def multi_frac(z1,n1,z2,n2):
    d=[z1*z2]
    e=[n1*n2]
    f=[d[0],e[0]]
    return f

#gives the Substraction of the two fractions
def sub_frac(z1,n1,z2,n2):
    g=[z1*n2,n1*n2]
    h=[z2*n1,n2*n1]
    i=[g[0]-h[0],g[1]]
    return i

#gives the Division of the two fractions
def div_frac(z1,n1,z2,n2):
    j=[z1*n2]
    k=[z2*n1]
    l=[j[0],k[0]]
    return l