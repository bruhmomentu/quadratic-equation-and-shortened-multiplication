#add problems to prints
import numpy
import math
from math import  sqrt
choice = int(input("enter what you want to solve: \n [1] quadratic equation\n [2] shortened multiplication\n "))
if choice == 1:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    c=int(input("enter c: "))
    d=sqrt(b**b-4*a*c)
    x1= (- b + sqrt(d)) / (2 * a)
    x2= ( -b - sqrt(d))/(2*a)
    print(x1,"\n",x2)
elif choice == 2:
    type= int(input("enter type of shortened multiplication\n  [1](a+b)²\n  [2](a-b)²\n  [3](a-b)(a+b)\n"))
    if type==1:
        a=int(input("enter a: "))
        b=int(input("enter b: "))
        answr=a**2+2*a*b+b**2
        print("(",a,"+",b,")²=",answr)
    elif type == 2:
        a=int(input("enter a: "))
        b=int(input("enter b: "))
        answr=a**2-2*a*b+b**2
        print("(",a, "-", b, ")²=", answr)
    elif type == 3:
        a=int(input("enter a: "))
        b=int(input("enter b: "))
        answr= a**2-b**2
        print("(",a,"-",b,")"," ","(",a,"+",b,")=",answr)