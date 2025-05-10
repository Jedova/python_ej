## Desafío - Introducción a Python ##
# Actividad 1: Velocidad de escape
# Ve = (2*g*r)^0.5

import math as m

#Definición del radio

radio = float(input("ingresar radio en kilometros [km]: "))

r = radio*1000

#Definición de la gravedad

gravedad = input("La constante utilizada es 9.8 [m/s²]. ¿Está de acuerdo? (SI/NO). Nota: considerar que los valores deben ser ingresados en [m/s²]: ").strip().upper()
if gravedad == "NO":
    g = float(input("Ingrese el valor de la constante g en [m/s²]: "))
else:
    g = 9.8

##Calculo de la velocidad

Velocidad = m.sqrt(2*r*g)
print(f"la velocidad de Escape es:{Velocidad:.2f}[m/s]")