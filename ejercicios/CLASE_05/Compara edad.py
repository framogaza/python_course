# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:48:36 2021

@author: Rafael
"""

nombre= input("Nombre?: ")
apellido=input("Apellido?:")
ubicacion=input('Ubicación?:')
edad=input('Edad?:')

if edad > 0 and edad <=13:
    print (nombre, "eres un niño")
elif edad >13 and edad <= 18:
    print(nombre, "eres adolescente")

else:
    print(nombre, 'eres adulto')    

