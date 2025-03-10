import math as m

def f(x):
    return m.sqrt(1-0.4*x**2)-m.asin(x)

def root(a,b):
    x=0
    if (abs(b-a)/2)<0.0001:
        r=(b+a)/2
    else:
        x=(a+b)/2
        if f(a)*f(x)>0:
            return root(x,b)
        return root(a,x)
    return r
a=int(input('Введите левую границу отрезка: '))
b=int(input('Введите правую границу отрезка: '))
print('Корень равен', root(a,b))