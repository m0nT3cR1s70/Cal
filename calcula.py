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
    r = input('Deseas sumas(s), miltiplicar(m) o dividir(d)')
    if r == 's':
        print('Suma es: ',operaciones.suma(a,b))
    elif r == 'm':
        print('El producto es: ',operaciones.multiplica(a,b))
    else:
        print('La division es: ',operaciones.divide(a,b))
    if input('Deseas salir s/n') == 's':
        break
    