while (True) :
    menu= """
    ---------------------------------------------------------------------------------
    Bienvenidos a la calculadora de PLATZI:
    
    aquí podras realizar las siguientes operaciones: +,-,*,/: 
    Presiona el numero correspondiente a la operación matematica que deseas realizar:
    
    1) Sumar (+)
    2) Restar (-)
    3) Multiplicar (*)
    4) Dividir (/)
    5) Salir de calculadora
    
    La opción que elijo es:"""

    opcion =int(input(menu))

    num_1 = float (input("\nColoque el primer número: \n"))
    num_2 = float (input("\nColoque el segundo número: \n"))

    
    if opcion ==1:
         print("""\n 
        ---------------------------------------------------------------
        El resultado de la suma es:""", num_1+num_2)    

    elif opcion  == 2:
        print(""" 
        ---------------------------------------------------------------
        El resultado de la resta es: """, num_1-num_2)
         

    elif opcion == 3 :
        print(""" 
        ---------------------------------------------------------------
        El resultado de la multiplicación es: """, num_1*num_2)

    
    elif opcion == 4 :
        print (""" 
        ---------------------------------------------------------------
        El resultado de la división es """, num_1/num_2)
 

    elif opcion ==5:
        print ("""\n \n \n 
        ---------------------------------------------------------------
        Usted a decidido salir de la calculadora.
        
        Que tenga un buen día 
        
        Adiós\n \n """)
        break

    else:
        print("""\n 
        ---------------------------------------------------------------
                  Comando desconocido, vuelve a intentarlo por favor""")

