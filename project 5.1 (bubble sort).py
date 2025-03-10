n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=int(input('Введите элемент массива: '))
    lst.append(x)

def bubble_sort(lst):
    check=True
    while check==True:
        check=False
        for j in range(len(lst)-1):
            for i in range(len(lst)-1):
                if lst[i]>lst[i+1]:
                    lst[i],lst[i+1]=lst[i+1],lst[i]
                    check=True
        if check==False:
            break

    return(lst)
print('Отсортированный массив:',bubble_sort(lst))