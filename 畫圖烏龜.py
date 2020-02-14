#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:20:55 2020

@author: juliapao
"""

import turtle
Tur = turtle.Turtle()
Tur.color("blue")
Tur.shape("turtle")
a=0
for i in range(360):
    Tur.forward(a)
    Tur.right(10)
    a=a+0.1
turtle.done()  

