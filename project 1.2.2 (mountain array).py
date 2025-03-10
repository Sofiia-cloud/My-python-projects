
def mountain_array(arr):
    low=0
    high=len(arr)-1

    if len(arr)<3: # длина горного массива должна быть как минимум 3 
        return f'не является горным массивом'
    while (high-low)>1:
        mid= (low + high)//2
        midVal= arr[mid]
        
        if arr[mid+1]<midVal and midVal>arr[mid-1]: # проверяем, является ли серединный элемент тройки наибольшим из них
            return f'индекс первого пика равен {mid}'

        if arr[mid-1]<midVal<arr[mid+1]:
            low=mid
        else:
            high=mid
    return f'не является горным массивом'
    
a=[4,3,2,1]
print(mountain_array(a))
