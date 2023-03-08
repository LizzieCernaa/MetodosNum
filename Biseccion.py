import math

a = float(input('Introduzca el extremo a: '))
b = float(input ( 'Introduzca el extremmo b : '))
iteracion=float(input('Introduzca el numero de iteraciones : '))
tolerancia=float(input('Introduzca la tolerancia : '))

error=100 #Inicialización de la tolerancia, pero se le iguala a un número alto por si el usuario desea una tolerancia mayor a 1 porciento
iter=0 

#Mientras el valor absoluto del error sea mayor o igual a la tolerancia  ó  la iteración no llegue a su valor límite
while abs(error) >= tolerancia or iter>iteracion:
    #Se coloca al inicio para que la primera iteración sea 1, si se pone alfinal habrá una iteración de más
    iter+=1

    m=round((a+b)/2, 4) #Punto medio M
    fa = round((math.e**(3*a)-4), 4) #se sustituye el valor en la ecuación, y luego se redondea a 4 decimales
    fb = round((math.e**(3*b)-4), 4) 
    fm = round((math.e**(3*m)-4), 4) 
    error=round((((b-a)/2)*100), 4)  #Se calcula el error en porcentaje, y luego se redondea

    if fa*fm < 0:
        b=m
    else:
        a=m

    if iter<=1: #Para imprimir el header de la tabla solo una vez
        print("  ______________________________________________________________________________________________________________")
        print(" | Iter | a                       | b                       | m                       | error                   |")
        print(" |¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|")
       
    DaList=[[iter,fa,fb,m,error]] #Lista para imprimir la tabla
    for item in DaList:
        print(" |",item[0]," "*(3-len(str(item[0]))),
        "|",item[1]," "*(22-len(str(item[1]))),
        "|",item[2]," "*(22-len(str(item[2]))),
        "|",item[3]," "*(22-len(str(item[3]))),
          "|",item[4]," "*(22-len(str(item[4]))),"|")
   
   
print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯") #Es el final de la tabla
print('La aproximación de la raiz es : ', m)
print('Se alcanzó en la iteración : ', iter)
print('Con un error de : ', error,"%")
