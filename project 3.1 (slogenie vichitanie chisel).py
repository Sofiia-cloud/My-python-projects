first=input('Введите первое число: ')
sec=input('Введите второе число: ')

def slogenie(first,sec):
    ans=''
    first=[int(i) for i in first][::-1]
    sec=[int(i) for i in sec][::-1]
    if len(first)<len(sec):
        lst=[0]*(len(sec)+1) # берем длину макс числа и увеличиваем ее на 1, в случае увеличения числа разрядов итого числа (макс увеличение=1)
        first=first+[0]*(len(lst)-len(first)) # добавляем незначащие 0, чтобы длины всех чисел стали одинаковыми
    else:
        lst=[0]*(len(first)+1)
        sec=sec+[0]*(len(lst)-len(sec))
    
    for x in range(len(lst)-1):
        if first[x]+sec[x]+lst[x]>9: # учет случая, когда получается 10 при сложении
            lst[x+1]+=1
        lst[x]=(first[x]+sec[x]+lst[x])%10
       
    for n in lst[::-1]: # запись итого числа
        ans+=str(n)
    return int(ans)
print('сумма введенных чисел равна:',slogenie(first,sec))

def vichitanie(first,sec):
    f=int(first)
    s=int(sec)
    first=[int(i) for i in first][::-1]
    sec=[int(i) for i in sec][::-1]
    ans=''
    if f<s: # определяем большее число
        lst=[0]*len(sec) # берем длину макс числа 
        first=first+[0]*(len(lst)-len(first)) # добавляем незначащие 0, чтобы длины всех чисел стали одинаковыми
        first,sec=sec,first # меняем местами числа, чтобы из  большего  вычитать  меньшее
    else:
        lst=[0]*len(first)
        sec=sec+[0]*(len(lst)-len(sec))
    
    for x in range(len(lst)):
        if first[x]-sec[x]+lst[x]<0: # учет случая, когда вычитается большее число разрядов из меньшего
            lst[x+1]-=1
            lst[x]=10+first[x]-sec[x]+lst[x] # "занимаем" 10 для вычитания
        else:
            lst[x]=first[x]-sec[x]+lst[x]

    for n in lst[::-1]: # запись итого числа
        ans+=str(n)
    return int(ans)
print('разность введенных чисел равна:', vichitanie(first,sec))

