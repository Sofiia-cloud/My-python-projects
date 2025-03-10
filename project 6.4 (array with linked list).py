class Node: #Класс для представления узла связанного списка
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Linked_List: # Класс для представления связанного списка
    def __init__(self):
        self.head = None  

    def append(self, data): # Добавить узел в конец списка
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # Если список пуст, новый узел становится началом
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next  # Перейти к последнему узлу
        last_node.next = new_node  # Присоединить новый узел

    def sum(self):
        current_node = self.head
        itog = 0
        while current_node:
            itog += current_node.data  # Добавить значение текущего узла к сумме
            current_node = current_node.next  # Перейти к следующему узлу
        return itog


arr=Linked_List()           

n=int(input('Введите количестыо чисел:'))
for i in range(n):
    x=int(input("Введите число:"))
    arr.append(x)
   
print('Сумма чисел в связном списке:',arr.sum())

