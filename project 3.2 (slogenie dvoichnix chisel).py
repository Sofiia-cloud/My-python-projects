first=input('Введите первое число: ')
sec=input('Введите второе число: ')

def slogenie(first,sec):
    ans=''
    first=[0]+[int(i) for i in first]
    sec=[0]+[int(i) for i in sec]
    if len(first)<len(sec):
        first=[0]*(len(sec)-len(first))+first # добавляем незначащие 0, чтобы длины всех чисел стали одинаковыми
    else:
        sec=[0]*(len(first)-len(sec))+sec
    lst=sec

    print(*first)
    print(*lst)
    print('--'*len(first))

    while lst.count(1)!=0:
        for x in range(len(lst)):
            if first[x]+lst[x]>1: # учет случая, когда получается 2 при сложении
                lst[x-1]=1
                lst[x]=0
                first[x]=0
            elif first[x]+lst[x]==1:
                lst[x]=0
                first[x]=1
            else: 
                lst[x]=0
                first[x]=0

        print(*first)
        print(*lst)
        print('--'*len(first))
        
    for n in first: # запись итого числа
        ans+=str(n)
    return int(ans)
print('сумма введенных чисел равна:',slogenie(first,sec))

