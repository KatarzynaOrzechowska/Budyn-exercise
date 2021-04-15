# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 23:30:41 2021

@author: Darth
"""

import random
import math


pocket = ['100', '120', '150', '180', '220', '270', '330', '390', '470', '560', '680', '820', '1000', 
          '1200', '1500', '1800', '2200', '2700', '3300', '4700', '5600', '6800', '8200']
converter = 0
x =[]
i = True
while i == True:
    for z in random.choices(pocket):
        converter +=1
        x.append(int(z))
        if converter == 16:
            i = False
            break
        
    
#20log(licznik/(licznik+mianownik))
