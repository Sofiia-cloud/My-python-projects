import datetime 
import random
n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=random.randint(-1000,1000)
    lst.append(x)
lst1=lst2=lst

start1=datetime.datetime.now()
def insertion_sort_1(lst):
    n=len(lst)
    for i in range(1,n):
        temp=lst[i]
        pos=i-1
        while pos>=0:
            if lst[pos]>temp:
                lst[pos+1]=lst[pos]
                pos-=1
            else:
                break
        lst[pos+1]=temp
    return lst
insertion_sort_1(lst1)
finish1=datetime.datetime.now()

start2=datetime.datetime.now()
def binary_search(list,key, st, end):
    while st <= end:
        mid= (st + end)//2 # середина массива
        midVal= list[mid] 
        if midVal>key:
            st=mid+1 # начинаем поиск в левой части массива
        else:
            end=mid-1 # начинаем поиск в правой части массива
    return st

def insertion_sort_2(lst):
    n=len(lst)
    for i in range(0,n):
        temp=lst[i]
        pos=binary_search(lst, temp, 0, i)
        for j in range(i,pos,-1):
            
            lst[j]=lst[j-1]

        lst[pos]=temp
    return lst[::-1]
insertion_sort_2(lst2)
finish2=datetime.datetime.now()


print('Сортировка вставками (время):',finish1-start1)
print('Сортировка вставками с использованием бинарного поиска (время):',finish2-start2)