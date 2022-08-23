# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
list100 = np.linspace(1,100,100,dtype=int)
sum100=sum(list100)
print('sum of the first 100 integers is:{}'.format(sum100))

otherSum=0
for i in range(101):
    otherSum +=  i
   
    
print('otherSum ={}'.format(otherSum))