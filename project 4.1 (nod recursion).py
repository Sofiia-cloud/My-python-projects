a=int(input('Input the first number:'))
b=int(input('Input the second number:'))

def nod1(a,b):
    if a==0 and b==0:
        return 'НОД не может быть найден'
    elif a==0:
        return b
    elif b==0:
        return a
    while a!=b:
        if a>b:
            return nod1(a-b,b)
        else:
            return nod1(a,b-a)
    return a
print('НОД введенных чисел:', nod1(a,b))