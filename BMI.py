#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:06:42 2020

@author: juliapao
"""

身高=float(input("height:"))
體重=float(input("weight:"))
BMI=(體重//身高**2)
print("BMI是",BMI)
if BMI<18.5:
    print("過輕")
elif 18.5<=BMI and BMI<24:
    print("正常")
else:
    print("過重")
        
