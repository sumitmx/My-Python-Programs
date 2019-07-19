# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 18:25:01 2019

@author: Sumit
"""

n=int(input('Enter the number: '))
list1=[]

while (n%10!=0):
    list1.append(n%10)
    n=int(n/10)
    

print("The reverse of the number is : ")

for i in range(len(list1)):
        print(list1[i],end ="")