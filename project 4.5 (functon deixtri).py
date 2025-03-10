import sys
sys.setrecursionlimit(5000)

def deixtra(n):
    if n==1:
        return 1
    elif n%2==0:
        return deixtra(n//2)
    else:
        return deixtra((n - 1)//2 + 1)+deixtra((n - 1)//2)


n=int(input('Введите число:'))

print('Значение функции Дейкстры равно', deixtra(n))