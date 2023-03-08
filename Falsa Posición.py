import math

a = float(input('Introduzca el extremo a: '))
b = float(input ( 'Introduzca el extremmo b : '))
iteracion=float(input('Introduzca el numero de iteraciones : '))
tolerancia=float(input('Introduzca la tolerancia : '))

error=1000
iter=0

while a>=b:
    print("Error, a debe ser menor que b")
    a = float(input('Introduzca el extremo a: '))
    b = float(input ( 'Introduzca el extremmo b : '))
    iteracion=float(input('Introduzca el numero de iteraciones : '))
    tolerancia=float(input('Introduzca la tolerancia : '))

while abs(error) > tolerancia or iter>iteracion:

        fa=round(((8/10)-(3/10)*a)/a,4)
        fb=round(((8/10)-(3/10)*b)/b,4)
        xi=round(((a*fb)-(b*fa))/(fb-fa),4)
        
        fxi=round(((8/10)-(3/10)*xi)/xi,4)

        if(iter>=1):
            
            error=round((abs(xi-xiAnterior)/xi),4)
        
        xiAnterior=xi

        if((fa*fb)<0):
            b=xi
        else:
            a=xi

         
        iter+=1

print("xi =", xi)
print("error: ",round(error*100,4),"%")
print("iteración",iter)

input()

