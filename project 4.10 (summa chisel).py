lst=[]
chislo=int(input('Введите число-сумму: '))
n=int(input('Введите количество чисел в массиве:'))

for i in range(n):
    x=int(input("Введите число:"))
    lst.append(x)

def hash_table(lst,chislo):
    res={}
    ans=set()
    for i in range(len(lst)):
        res[lst[i]]=i
    #sorted_dict = dict(sorted(res.items()))
    for j in range(len(lst)):
        if (chislo-lst[j] in res) and (res[chislo-lst[j]]!=j):
            ans.add(j)
            ans.add(res[chislo-lst[j]])
    return ans
print(hash_table(lst,chislo))

