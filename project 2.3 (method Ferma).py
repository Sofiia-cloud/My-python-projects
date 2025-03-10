
a=int(input("Input a:"))

def ferma(a): # метод Ферма
  
    m=int(a**0.5)
    x=1
    while ((m+x)**2-a)**0.5!=int(((m+x)**2-a)**0.5):
        x+=1
    if a**0.5==int(a**0.5):
        p=q=int(a**0.5)
    else:
        A=m+x
        B=int(((m+x)**2-a)**0.5)
        q= A-B
        p=A+B
    
    return [q,p]

def resheto(a): # решето Эратосфена 
    lst = []
    for i in range(2, a + 1):
        lst.append(i)

    for j in lst:
        for y in range(2*j,a+1,j):
            if y in lst:
                lst.remove(y)

    return lst[1:] # 2 пропускаем, тк у нас нечетные числа


def factor(a): # раскладываем число на простые множители
    mnoj=ferma(a)
    ans=[]
    c_1=mnoj[0]
    c_2=mnoj[1]
    
    if c_1==resheto(c_1)[-1]:
        ans.append(c_1)
    if c_2==resheto(c_2)[-1]:
        ans.append(c_2)
    if c_1!=resheto(c_1)[-1]:
        ans+=(ferma(c_1)[0:2])
    if c_2!=resheto(c_2)[-1]:
        ans+=(ferma(c_2)[0:2])
    return ans


if a%2==0:
    print('Вы ввели четное число, поэтому программа не может быть реализована')
elif a in resheto(a):
    print(f'число {a} встречается {1} раз')
else:
    lst=sorted(factor(a))

    for i in set(lst):
        print(f'число {i} встречается {lst.count(i)} раз')


