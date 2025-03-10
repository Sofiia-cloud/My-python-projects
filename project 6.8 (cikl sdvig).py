k=int(input('Введите количество элементов:'))
lst=[]
ans=[0]*k
n=int(input('Введите N:'))
side=input('Введите направление сдвига:')
for i in range(k):
    x=int(input("Введите элемент массива:"))
    lst.append(x)

if side=='влево':
    for i in range(k): # left
        ans[i-n]=lst[i]
else:
    for i in range(k): # right
        ans[(i+n)%k]=lst[i]

print('Изначальный список:',lst)
print('Список со сдвигом:',ans)