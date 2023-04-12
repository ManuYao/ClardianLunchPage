from asyncio.log import logger
from datetime import datetime
from tkinter import E, W
import webbrowser 
import time 
import os.path
import os

#Zone test |/[]\|

#Ouvre les pages Web
def Weblunch():
    webbrowser.open('https://docs.google.com/spreadsheets/d/1E5bKiLOb16oLeULvyNGY014Box8QewO9C0qszUqgRbs/edit?pli=1#gid=1293143753')
    webbrowser.open('https://calendar.google.com/calendar/u/0/r?tab=rc')
    time.sleep(2)
    webbrowser.open('https://extranet.bmi-system.com/index.php?option=com_badger_custom_pages&Itemid=1&command=SHOW_PAGE&id=2')
    time.sleep(2)
    webbrowser.open('https://mail.google.com/mail/u/0/?pli=1#inbox')
    time.sleep(2)
    webbrowser.open('https://bmi-system.ilucca.net/timmi#/submission/62/2022-01-31')
    time.sleep(2)
    webbrowser.open('https://chat.bmi-system.com/direct/KZjjrRgZoJfQucGbyodm3XGjjtTbetfzFS')
    time.sleep(2)
    webbrowser.open('http://redmine.clardian.com/login?back_url=http%3A%2F%2Fredmine.clardian.com%2F')
    return True

#Ouvre les apps 
def AppLunch():

    print("Lancement des services en cours...")
    time.sleep(4)
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\KeePass 2.lnk')
    time.sleep(2)
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox\Oracle VM VirtualBox.lnk')
    time.sleep(4)
    os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk')
    time.sleep(6)
    tend = os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MobaXterm\MobaXterm.lnk')
    time.sleep(8)
    return True

#Affiche L'heure actuel
    now = datetime.now()
    time_ = now.strftime("%H:%M:|---|%D")
    time_str = "9:30"

#Fichier de log
def Logfile():
    fileLog = open('C:\\Users\\eyao\\Documents\\Travail\\DEV\\Script_Python\\log\\logAlpha.txt', "a") 
    fileLog.write('\n Le travail à débuter >  ' + time_ + "  < la fin de journée est à ... N/A") 
    #Ajouter un calcule à fin de voir l'heur de sortie
    fileLog.write('\n|')
    fileLog.close()

#Lance le processus
def LuchPross():
     Weblunch()
     AppLunch()
     Logfile()
     print("F I N BETA")


os.startfile(r"C:\Users\eyao\Documents\Travail\DEV\Script_Python\log\logAlpha.txt")

print('--------------------------------')
print('temp actuel DEBUG! = ' + time_)
print('--------------------------------')
print('\n')

if time_ < time_str: 
    print('Lancement des service en cours 20s... ')
    print('------------------------------')
    print('Il est actuellement ', time_ ,"Tu est à l'heur")
    #print("Tu fini donc à ", JustTime) ...
    LuchPross()
else:
    print('Lancement des service en cours ... ')
    print('Il est actuellement ', time_ ,"Tu n'est pas à l'heur")
    LuchPross()