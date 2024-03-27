from os import getcwd
import czas
import time
import importlib
#Zad1
print("Helou World")
help(print)

#Zad2

current_path = getcwd()
print(current_path)
print(czas.aktualny_czas)
time.sleep(20)
print(czas.aktualny_czas)
importlib.reload(czas)
print(czas.aktualny_czas)

#Zad3
