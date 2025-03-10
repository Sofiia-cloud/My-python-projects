
def nod(a, b): # алгоритм для поиска нода методом вычитания
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = abs(int(input('Input a:')))
b = abs(int(input('Input b:')))
c = abs(int(input('Input c:')))
d = abs(int(input('Input d:')))

lst = sorted([a,b,c,d])

if lst.count(0) == 0:
    print('Нод равен',nod(a, nod(b, nod(c, d))))
elif lst.count(0) == 1:
    a = lst[1]
    b = lst[2]
    c = lst[3]
    print('Нод равен',nod(a, nod(b, c)))
elif lst.count(0) == 2:
    a = lst[3]
    b = lst[4]
    print('Нод равен',nod(a, b))
elif lst.count(0) == 3:
    print('Нод равен',lst[4])
else:
    print('нод не может быть определен')

