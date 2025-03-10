
def binary_search(list,key=0):
    low=0
    high=len(list)-1
    
    while low <= high:
        mid= (low + high)//2
        midVal= list[mid]
        
        if midVal==key: # если в массиве есть 0
            pol_chisla=len(list[mid:-1])
            otr_chisla=len(list[0:list.index(0)]) # конец среза - это первое вхождение 0 в списке
            
    
        if midVal>0 and list[mid-1]<0: # минимальное положительное число в массиве
            pol_chisla=len(list[mid:-1])+1
            otr_chisla=len(list[0:mid])  
        if midVal>key:
            high=mid-1
        else:
            low=mid+1

    if min(list)>0: # если в массиве только положительные числа
        return f'количество положительных чисел равно {len(list)}'
    if max(list)<0: # если в массиве только отрицательные числа
        return f'количество отрицательных чисел равно {len(list)}'
    
    if pol_chisla>otr_chisla:
        return f'количество положительных чисел равно {pol_chisla}'
    if pol_chisla<otr_chisla:
        return f'количество отрицательных чисел равно {otr_chisla}'
    else:
        return f'количество отрицательных чисел равно положительным'

a=[0,0,0]
print(binary_search(a))

