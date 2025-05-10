## Rentabilidad ##
# Utilidades = P * U - GT
#Ejercicio 2

Precio1 = float(input("¿Cual es el precio de la suscripción normal [CLP]:"))
Usuariosp = int(input("¿Cual es el número de usuarios premium? [#]: "))
Usuariosn = int(input("¿Cual es el número de usuarios normales? [#]: "))
Gastosn = float(input("Indicar gastos totales para la suscripción de usuarios normales [CLP]: "))
Gastosp = float(input("Indicar gastos totales para la suscripción de usuarios premium [CLP]: "))

Utilidades = Precio1*(Usuariosn + 1.5*Usuariosp) - Gastosn - Gastosp
Utilidadesp = Precio1*1.5*Usuariosp - Gastosp
Utilidadesn = Precio1*Usuariosn - Gastosn

print = input(f"Las utilidades totales son:{Utilidades:.2f}[CLP]")