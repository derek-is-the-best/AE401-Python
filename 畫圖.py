#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:20:43 2020

@author: juliapao
"""

import turtle
Tur = turtle.Turtle()
Tur.color("yellow")
Tur.shape("turtle")
a=0
import time
while a<=11:
    Tur.forward(100)
    Tur.right(15)
    time.sleep(1)
    a=a+1
turtle.done()   
    
    
    
    