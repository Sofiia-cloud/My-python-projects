n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=int(input('Введите элемент массива: '))
    lst.append(x)

def shaker_sort(lst):
    check=True
    while check==True:
        check=False
    
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                check=True
        if check==False:
            break
    
        check=False
        n=len(lst)
        st=0
        n-=1
        for y in range(n,st,-1):
            if lst[y]<lst[y-1]:
                lst[y],lst[y-1]=lst[y-1],lst[y]
                check=True 
        st+=1
        if check==False:
            break
        
    return(lst)
print('Отсортированный массив:',shaker_sort(lst))