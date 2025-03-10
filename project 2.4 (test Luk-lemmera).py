
p=int(input('Введите номер числа Мерсенна:'))
def luk_lemmer(p):
    s=4
    k=1
    M=2**p-1
    while k!=p-1:
        s=((s**2)-2)%M
        k+=1
    if s==0:
        return f"{M} данное число Мерсенна простое"
    else:
        return f'{M} данное число Мерсенна составное'
print(luk_lemmer(p))
