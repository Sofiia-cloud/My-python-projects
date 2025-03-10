def binary_search(list,key):
    low=0 # нижняя граница 
    high=len(list)-1 # верхняя граница
    
    while low <= high:
        mid= (low + high)//2 # середина массива
        midVal= list[mid] 
        if midVal== key: 
            return f'Элемент находится на {mid} позиции.'
        if midVal>key:
            high=mid-1 # начинаем поиск в левой части массива
        else:
            low=mid+1 # начинаем поиск в правой части массива

    if key<list[mid]: # сравниваем новый элемент с ближайшим по значению числом
        list.insert(mid, key)
        return f'Позиция вставки элемента равна {mid}. Новый список: {list}'
    else:
        list.insert(mid+1, key)
        return f'Позиция вставки элемента равна {mid+1}. Новый список: {list}'
        
a=[1,2,3,5,5,6,8]
print(binary_search(a,4))