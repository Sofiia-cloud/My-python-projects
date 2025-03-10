class Node: #Класс для представления узла связанного списка
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable: #Класс для представления хэш-таблицы
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key): #Хэш-функция для получения индекса элемента
        return hash(key) % self.size

    def insert(self, key, value): #Вставка ключа и значения в хэш-таблицу
        index = self._hash(key)
        new_node = Node(key, value)

        # Если на этом индексе ничего нет, просто добавляем новый узел.
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Если уже есть элементы, добавляем новый узел в начало списка.
            current = self.table[index]
            while current:
                if current.key == key:
                    # Если ключ уже существует, добавляем значение в список.
                    if isinstance(current.value, list):
                        current.value.append(value)
                    else:
                        current.value = [current.value, value]
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def get(self, key): #Получение значений по ключу
        index = self._hash(key)
        current = self.table[index]

        values = []
        while current:
            if current.key == key:
                if isinstance(current.value, list):
                    values.extend(current.value)
                else:
                    values.append(current.value)
            current = current.next

        return values if values else None  # Если ключ не найден

    def remove(self, key, value=None): #Удаление элемента по ключу. Если у ключа есть иные значения – удалять только значения
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if value is None:
                    # Удаляем весь узел.
                    if prev is None:
                        self.table[index] = current.next
                    else:
                        prev.next = current.next
                else:
                    # Удаляем только указанное значение.
                    if isinstance(current.value, list):
                        if value in current.value:
                            current.value.remove(value)
                            # Если после удаления список пустой, удаляем узел.
                            if not current.value:
                                if prev is None:
                                    self.table[index] = current.next
                                else:
                                    prev.next = current.next
                    elif current.value == value:
                        if prev is None:
                            self.table[index] = current.next
                        else:
                            prev.next = current.next
                return True
            prev = current
            current = current.next

        return False  # Если ключ не найден.



# Пример использования хэш-таблицы как телефонной книги
commanda=int(input('Введите номер операции, которую вы хотите совершить: 1 - добавление записи в телефонную книгу; 2 - поиск номера телефона по фамилии; 3 - удаление номера телефона; 4 - удаление всей записи; 0 - завершение программы:'))
phone_book = HashTable()
while commanda!=0:
    
    if commanda==1: #добавление записи в телефонную книгу
        name=input('Input a name:')
        number = input('Input a phone number:')
        phone_book.insert(name, number)
    elif commanda==2: #поиск номера телефона по фамилии
        name=input('Input a name:')
        print(phone_book.get(name)) 
    elif commanda==3: #удаление номера телефона
        name=input('Input a name:')
        number = input('Input a phone number:')
        print(phone_book.remove(name, number))
    elif commanda==4: #удаление всей записи
        name=input('Input a name:')
        phone_book.remove(name)
        print(phone_book.get(name))
    else:
        print('Ошибка ввода')
    commanda=int(input('Введите номер операции, которую вы хотите совершить: 1 - добавление записи в телефонную книгу; 2 - поиск номера телефона по фамилии; 3 - удаление номера телефона; 4 - удаление всей записи; 0 - завершение программы:'))

'''phone_book = HashTable()
# Добавление записей
phone_book.insert("Иванов", "123-456")
phone_book.insert("Петров", "987-654")
phone_book.insert("Сидоров", "555-000")
phone_book.insert("Иванов", "111-222")  # Добавляем еще один номер для Иванова

# Поиск номеров по фамилии
print(phone_book.get("Иванов"))  
print(phone_book.get("Петров"))  
print(phone_book.get("Сидоров")) 
print(phone_book.get("Неизвестный"))  

# Удаление номера телефона
phone_book.remove("Иванов", "123-456")  # Удаляем только один номер
print(phone_book.get("Иванов"))  

# Удаление всей записи
phone_book.remove("Петров")  # Удаляем Петрова полностью
print(phone_book.get("Петров"))  


'''