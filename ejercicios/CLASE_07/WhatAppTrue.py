# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:26:27 2021

@author: Juan Carlos
"""
import pyautogui as pg
import time
import webbrowser as web
phone_no="+593xxxxxxx"
parsedMessage=" Demo de Python con WhastApp "
web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
time.sleep(8)
for i in range(10):
    pg.write('La BlueIT no se detiene curso de Python')
    pg.press('enter')
    print('Mensaje #'+str(i+1)+' enviado')
    pass
pg.alert('Envio de mensajes finalizada')
