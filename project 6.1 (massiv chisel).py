n=int(input('Введите количество элементов:'))
arr=[]
usl1=usl2=usl3=usl4=usl5=usl6=0

def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return fact(x-1)*x


for i in range(n):
    x=int(input("Введите элемент массива:"))
    arr.append(x)

for i in range(len(arr)):
    if arr[i]%2!=0:
        usl1+=1
    
    if arr[i]>=0 and int(arr[i]**0.5)==arr[i]**0.5 and arr[i]%2==0:
        usl2+=1
    
    if arr[i]%3==0 and arr[i]%5!=0:
        usl3+=1
    
    if 2**i<arr[i]<fact(i):
        usl4+=1
    
    if i%2==0 and arr[i]%2!=0:
        usl6+=1

for i in range(1,len(arr)-1):
    if arr[i]<((arr[i-1]+arr[i+1])/2):
        usl5+=1

print('Условие 1:',usl1)
print('Условие 2:',usl2)
print('Условие 3:',usl3)
print('Условие 4:',usl4)
print('Условие 5:',usl5)
print('Условие 6:',usl6)


