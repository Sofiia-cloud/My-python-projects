n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=int(input('Введите элемент массива: '))
    lst.append(x)

def insertion_sort(lst):
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
print('Отсортированный массив:',insertion_sort(lst))