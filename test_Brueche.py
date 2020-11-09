# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:49:29 2020

@author: raine
"""

from Brueche import add_frac 
def test_add_frac(): 
    assert add_frac(2,3,4,5) == [22, 15]

from Brueche import multi_frac   
def test_multi_frac(): 
    assert multi_frac(2,3,4,5) == [8, 15]
