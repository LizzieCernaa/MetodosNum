import sympy
from sympy import *

ite=0
error=1

x=sympy.symbols('x')


ecuacion=input("Ingrese la función: ")
#f(X)=x**3+3*x**4+x+1
xi=float(input("Ingrese aproximación inicial: "))
tol=float(input("Ingrese la tolerancia: "))
itera=int(input("Ingrese la cantidad de Iteraciones: "))

derivada=diff(ecuacion, x)

while error>tol or ite>itera:
	y=round(sympy.sympify(ecuacion).subs(x,xi),4) #la función normal
	print("\n",y,end="	")
	yprima=round(sympy.sympify(derivada).subs(x,xi),4)#la función derivada
	print(yprima,end=" ")
	xii=xi-(y/yprima)
	print(xii, end=" ")
	error=round(abs((xii-xi)/xii),4)
	print(error, end="")
	xi=xii
	ite+=1

print("\nLa raíz encontrada es ", xii)
print("Fue convergente en la iteración: ",ite)
print("Con un error de: ", error)
