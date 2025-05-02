print ("hola que vamos a calcular hoy")
operacion= float (input ("dijita 1 para suma o 2 para resta"))
if operacion == 1:
    num1 = float (input ("digita numero 1:"))
    num2 = float (input ("digita numero 2:"))
    suma = num1 + num2 
    print ("el resultado de la suma es: ", suma)
elif operacion == 2:
    num3 = float (input ("digita numero 1:"))
    num4 = float (input ("digita numero 2:"))
    resta = num3 - num4 
    print ("el resultado de la resta es: ", resta)
else: 
    print ("numero incorrecto")



