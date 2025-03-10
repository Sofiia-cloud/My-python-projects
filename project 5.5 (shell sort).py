n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=int(input('Введите элемент массива: '))
    lst.append(x)

def shell_sort(lst):
    n=len(lst)
    d=n//2 # длина промежутков между элементами
    while d>0:
        for i in range(d,n):
            cur=lst[i]
            index=i
            while index >= d and lst[index-d]>cur:
                lst[index]=lst[index-d]
                index-=d
            lst[index]=cur
        d-=1
    return lst
print('Отсортированный массив:',shell_sort(lst))