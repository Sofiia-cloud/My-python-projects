n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=int(input('Введите элемент массива: '))
    lst.append(x)

def selection_sort(lst):
    n=len(lst)
    
    for i in range(n):
        index_mi=i
        for j in range(i+1,n):
            if lst[j]<lst[index_mi]:
                index_mi=j
        lst[i],lst[index_mi] = lst[index_mi], lst[i]
        
    return lst

print('Отсортированный массив:',selection_sort(lst))