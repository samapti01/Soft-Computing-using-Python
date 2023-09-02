# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:41:53 2023

@author: user
"""

# Example to Demonstrate
# Intersection of Two Fuzzy Sets
A = dict()
B = dict()
Y = dict()
 
A = {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
B = {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
 
print('The First Fuzzy Set is :', A)
print('The Second Fuzzy Set is :', B)
 
 
for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]
 
    if A_value < B_value:
        Y[A_key] = A_value
    else:
        Y[B_key] = B_value
print('Fuzzy Set Intersection is :', Y)