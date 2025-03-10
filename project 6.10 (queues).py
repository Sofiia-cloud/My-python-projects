import queue

def numbers(file): # Функция для чтения файла и печати чисел в нужном порядке
    
    odnoznach = queue.Queue()
    dvuznach = queue.Queue()

    with open(file, encoding="UTF-8") as f: # Читаем файл и распределяем числа по очередям
        for line in f:
            number = int(line.strip())
            if 0 <= number < 10:  # Однозначные числа
                odnoznach.put(number)
            elif 10 <= number < 100:  # Двузначные числа
                dvuznach.put(number)

    while not odnoznach.empty():
        print(odnoznach.get())

   
    while not dvuznach.empty():
        print(dvuznach.get())


numbers(r"C:\Users\София\OneDrive\Desktop\python projects\pythonProject\file for pr 6.10.txt") 
