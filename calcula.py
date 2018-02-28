#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:34:58 2018

@author: m0nt3cr1s70
"""
import operaciones 


#control = True
while True: 
    a = int(input('Valor a: '))
    b = int(input('Valor b: '))
    if input('Deseas sumas(s) o miltiplicar(m)') == 's':
        print('Suma es: ',operaciones.suma(a,b))
    else: 
        print('El producto es: ',operaciones.multiplica(a,b))
    if input('Deseas salir s/n') == 's':
        break
    