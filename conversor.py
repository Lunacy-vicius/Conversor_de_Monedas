menu = """
Bienvenido al convrsor de monedas 🌟

1 - Pesos Mexicanos
2 - Pesos colombianos
3 - Pesos argentinos
4 - Bit coin

Elige una opción
"""
opcion = int(input(menu))

if opcion == 1:
    pesos = input ("Cuantos pesos mexicanos tienes")
    pesos = float(pesos)
    valor_dolar = 19.93
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
elif opcion == 2:
    pesos = input ("Cuantos pesos colombianos tienes")
    pesos = float(pesos)
    valor_dolar = 3,521
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
elif opcion == 3:
    pesos = input ("Cuantas copas tenes vos")
    pesos = float(pesos)
    valor_dolar = 88.47
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
elif opcion == 4:
    pesos = input ("Cuantos bit coins tienes")
    pesos = float(pesos)
    valor_dolar = 0.000020
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
else:
    print('Ingresa un valor correcto')


