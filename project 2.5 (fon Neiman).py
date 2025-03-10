
import random as r
a=r.randint(10000,100000)
ans=[]
while len(ans)<10:
    sqrt_a=a**2
    if int(str(a**2)[2:7])>=10000:
        chislo=int(str(a**2)[2:7])
    else:
        chislo=int(str(a**2)[2:8])
    ans.append(chislo)
    a=chislo
print('Последовательности из 10 пятизначных чисел фон Неймана:',*ans)

