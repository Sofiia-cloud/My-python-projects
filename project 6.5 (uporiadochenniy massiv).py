n=int(input('Введите размер массива:'))
arr=[]
k=0
for i in range(n):
    x=float(input('Введите элемент массива:'))
    arr.append(x)

for i in range(n-1):
    if arr[i]<arr[i+1]:
        k=1
if k!=0:
    print('Не является упорядоченным по убыванию')
else:
    print('Является упорядоченным по убыванию')
