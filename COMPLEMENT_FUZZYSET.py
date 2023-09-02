# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:43:02 2023

@author: user
"""

# Example to Demonstrate the
# Difference Between Two Fuzzy Sets
A = dict()
Y = dict()
 
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
 
print('The Fuzzy Set is :', A)
 
 
for A_key in A:
   Y[A_key]= 1-A[A_key]
         
print('Fuzzy Set Complement is :', Y)