import datetime
first=input('Введите первое число: ')
sec=input('Введите второе число: ')
def karatsuba(first,sec): # метод Карацубы
    global time
    start1 = datetime.datetime.now()
    first=int(first)
    sec=int(sec)
    if len(str(first))==1 or len(str(sec))==1:
        return first*sec
    else:
        k=max(len(str(first)),len(str(sec)))//2 
       
        a=first//10**k # разбиваем первое число на два меньших
        b= first%10**k

        c= sec//10**k # разбиваем второе число на 2 меньших
        d=sec%10**k

        # считаем произведения чисел по алгоритму:
        x=karatsuba(b,d)
        y=karatsuba(a,c)
        z=karatsuba (a+b, c+d)

    ans=y*10**(2*k) + (z-y-x)*10**k + x # складываем промежуточные результаты (произведения чисел)
    finish1=datetime.datetime.now()
    time=finish1-start1
    
    return ans 
print('Произведение введенных чисел (метод Карацубы):',karatsuba(first,sec))


def umnogenie(first,sec):
    global time2
    start2=datetime.datetime.now()
    ans=''
    first=[int(i) for i in first][::-1]
    sec=[int(i) for i in sec][::-1]
    lst=[0]*(len(first)+len(sec)) # длина итого числа будет не больше чем общее кол-во цифр перемножаемых чисел 

    for x in range(len(first)):
        for y in range(len(sec)):
            lst[x+y]+=first[x]*sec[y] # выполняем попеременное умножение каждой пары цифр
    
    num=0 # число, которое должны прибавить к последующему разряду
    for i in range(len(lst)):
        lst[i]+=num # увеличение разряда на десяток, который запомнили при предыдущем сложении
        num=lst[i]//10 # будет больше 0, если сумма цифр больше 9 (то, что обычно запоминаем при сложении в столбик)
        lst[i]=lst[i]%10 # оставляем только последнюю цифру суммы, если эта сумма цифр больше 9

    for n in lst[::-1]: # запись итого числа
        ans+=str(n)
    finish2=datetime.datetime.now()
    time2=finish2-start2
    return int(ans)

print('Произведение введенных чисел (столбик):',umnogenie(first, sec))
print('Время выполнения при умножении столбиком',time2)
print('Время выполнения методом Карацубы:',time)

