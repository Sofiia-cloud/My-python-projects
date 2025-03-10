def resheto(a): # алгоритм решета Эратосфена
    lst = []
    for i in range(2, a + 1):
        lst.append(i)

    for j in lst:
        for y in range(2*j,a+1,j):
            if y in lst:
                lst.remove(y)

    return lst

a=int(input('Input a:'))
ans=[]
for i in resheto(a):
    k=0
    while a%i==0:
        a//=i
        k+=1 # находим степень числа
    ans.append([i,k])

for j in ans:
    if 0 not in j:
        print('число', j[0],'встречается',j[1], 'раз')

