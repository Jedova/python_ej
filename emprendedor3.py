## Rentabilidad ##
# Utilidades = P * U - GT
#Ejercicio 3

# Solicitar datos
Precio3 = float(input("¿Cuál es el precio de la suscripción [CLP]? "))
Usuariosn = int(input("¿Cuál es el número de usuarios normales [#]? "))
Gastos = float(input("Indicar gastos totales para la suscripción [CLP]: "))

# Validar que las utilidades anteriores no sean cero
while True:
    Utilidadesa = float(input("Incluir las utilidades del año anterior [CLP]: "))
    if Utilidadesa != 0:
        break
    print("Valor no aceptable para cálculo matemático (debe ser distinto de 0). Intente nuevamente.")

# Calcular utilidades actuales y ratio
Utilidadesac = Precio3 * Usuariosn - Gastos

Ratio = Utilidadesac/Utilidadesa

print(f"Las utilidades actuales son: {Utilidadesac:.2f} [CLP]")
print(f"El ratio entre utilidades es: {Ratio:.2f}")
