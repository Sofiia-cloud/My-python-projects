import datetime
import random
n=int(input('Введите количество элементов в массиве:'))
lst=[]

for x in range(n):
    x=random.randint(-1000,1000)
    #x=int(input('Введите элемент массива: '))
    lst.append(x)

ss = dd = ff = uu = tt = rr = lst

'''start1 = datetime.datetime.now()
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
bubble_sort(ss)
finish1= datetime.datetime.now()'''


start2 = datetime.datetime.now()
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
shaker_sort(dd)
finish2=datetime.datetime.now()


start3 = datetime.datetime.now()
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
insertion_sort(ff)
finish3=datetime.datetime.now()

start4 = datetime.datetime.now()
def selection_sort(lst):
    start4 = datetime.datetime.now()
    n=len(lst)
    mi=lst[0]
    
    for i in range(n):
        index_mi=i
        for j in range(i+1,n):
            if lst[j]<lst[index_mi]:
                index_mi=j
        lst[i],lst[index_mi] = lst[index_mi], lst[i]
    
    return lst
selection_sort(uu)
finish4=datetime.datetime.now()

start5 = datetime.datetime.now()
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
shell_sort(tt)
finish5=datetime.datetime.now()

start6 = datetime.datetime.now()
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
quick_sort(rr)
finish6=datetime.datetime.now()


#print('Время выполнения сортировки пузырьком:',finish1-start1)
print('Время выполнения шейкерной сортировки:',finish2-start2)
print('Время выполнения сортировки вставками:',finish3-start3)
print('Время выполнения сортировки выбором:',finish4-start4)
print('Время выполнения сортировки Шелла:',finish5-start5)
print('Время выполнения быстрой сортировки:',finish6-start6)