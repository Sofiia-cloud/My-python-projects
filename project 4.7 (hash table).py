class Node: #Класс для представления узла связанного списка
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable: #Класс для представления хэш-таблицы
    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key%7

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

    
the_hash_table=HashTable()           
lst=[]
for i in range(7):
    x=int(input("Введите число:"))
    the_hash_table.insert(x%7,x)
    
for i in range(7):    
    print(i, ':', the_hash_table.get(i))
    

