n=int(input('Количество дисков: '))
x=1
y=3

def hanoi_tower(n,x,y): # n - кол-во дисков, x - первый стержень, y -последний стержень
    if n<=0:
        return 0
    prom = 6 - x - y # промежуточный стержень
    hanoi_tower(n-1,x,prom)
    print('перенести диск',n,'со стержня',x,'на стержень',y)
    hanoi_tower(n-1, prom, y)

print(hanoi_tower(n,x,y))