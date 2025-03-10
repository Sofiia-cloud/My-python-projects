n=int(input('Введите размер массива:'))
arr=[]
k1=k2=0
for i in range(n):
    x=int(input('Введите элемент массива:'))
    arr.append(x)

for i in range(n-2):
    if arr[i]==0 and arr[i+1]==0 and arr[i+2]==0:
        k2+=1

for i in range(n-1):
    if arr[i]==0 and arr[i+1]==0:
        k1+=1

if k1!=0:
    print('Да, есть 2 идущих подряд нуля')
else:
    print('Нет, нет 2 идущих подряд нулей')

if k2!=0:
    print('Да, есть 3 идущих подряд нуля')
else:
    print('Нет, нет 3 идущих подряд нулей')