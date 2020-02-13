#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:11:20 2020

@author: juliapao
"""

import turtle
Tur = turtle.Turtle()
Turt = turtle.Turtle()
Turt.color("pink")
Tur.color("yellow")
Tur.shape("turtle")
import time
for i in range(12):
    Tur.forward(30)
    Tur.right(30)
    Turt.backward(30)
    Turt.left(30)
    time.sleep(1)
turtle.done()   