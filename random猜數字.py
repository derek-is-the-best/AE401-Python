#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:20:22 2020

@author: juliapao
"""

import random
a = random.randint(1,10)
while True:
    b = int(input("輸入一個數(1-10):"))
    if a==b:
        print("right")
        break
    else:
        print("wrong")
        