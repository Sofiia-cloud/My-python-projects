
with open(r"C:\Users\София\OneDrive\Desktop\python projects\pythonProject\file for pr 6.9.txt", encoding="UTF-8") as file:  
    for line in file:  
        stack = []  
        for char in line.strip():  # Убираем пробелы в начале и конце строки
            stack.append(char)  # Добавляем каждый символ в стек

reversed_line = ''
for i in stack[::-1]:
    reversed_line += i  # Берем последний добавленный символ
print(reversed_line)  