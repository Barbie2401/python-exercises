def conversor (tipo_pesos, valor_dolar):
    pesos= input("¿Cuantos pesos " +"tipo_pesos"+" tienes?: ")
    pesos =float (pesos)
    dolares = valor_dolar*pesos
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Tienes $" + dolares + " dolares")

menu= """
Bienvenido al conversor de monedas 😁💲💲

1- Pesos Chilenos
2- Pesos Colombianos
3- Pesos Argentinos
4- Pesos Mexicanos

Elige una opción:  """

opcion = int (input(menu))

if opcion == 1:
    conversor("Chilenos", 0.0012)
    
elif opcion == 2:
    conversor("Colombianos", 0.00025)
   
elif opcion==3:
    conversor("Argentinos", 0.0096)

elif opcion==4:
    conversor("Mexicanos", 0.048)

else:
    print("Ingresa una opción correcta por favor")




    


# pesos= input("¿Cuantos pesos Chilenos tienes?: ")
# pesos =float (pesos)
# valor_dolar = 0.0012
# dolares = valor_dolar*pesos
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print ("Tienes $" + dolares + " dolares")

# dolares=input ("¿Cuantos dolares tienes? ")
# dolares= float (dolares)
# valor_peso = 801.78
# pesos= valor_peso*dolares
# pesos=round(pesos,2)
# pesos =str(pesos)
# print ("Tienes $ " + pesos + " pesos")
