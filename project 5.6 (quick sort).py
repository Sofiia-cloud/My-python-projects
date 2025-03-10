n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=int(input('Введите элемент массива: '))
    lst.append(x)

def quick_sort(lst):
    n=len(lst)
    if n<=1:
        return lst
    else:
        less=[]
        more=[]
        elem=lst[n//2]
        for i in lst:
            if i<elem:
                less.append(i)
            elif i>elem:
                more.append(i)
    return quick_sort(less)+[elem]*lst.count(elem)+quick_sort(more)
 
print('Отсортированный массив:',quick_sort(lst))