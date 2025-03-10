
A=int(input('Введите делимое:'))
B=int(input('Введите делитель:'))
A1=A
B1=B

def f(p):
    return A-B*p

if B == 0:
    print('был введен 0, программа не может быть реализована')
elif B == 1:
    print('частное:', A)
    print('остаток: 0')
elif B == -1:
    print('частное:', A * (-1))
    print('остаток: 0')

else:
    A=abs(A)
    B=abs(B)
    L=0 # начало отрезка
    R=A # конец отрезка
    p=(R-L)//2
    while f(p)>=B or f(p)<0: 
        if f(p)>=B: 
            L=p
        if f(p)<0:
            R=p
        p=(R-L)//2+L
        
    if A1>0 and B1>0:
        print('частное:',p)
        print('остаток:',A-B*p)
    
    elif (A1>0 and B1<0):
        print('частное:',-1*p)
        print('остаток:',(A-B*p))

    elif (A1<0 and B1>0):
        print('частное:',-1*p)
        print('остаток:',-1*(A-B*p))

    else:
        print('частное:',p)
        print('остаток:',-1*(A-B*p))

