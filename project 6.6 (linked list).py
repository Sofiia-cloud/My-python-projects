class Node: # Класс для представления узла связанного списка
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List: # Класс для представления связного списка
    def __init__(self):
        self.head = None

    
    def is_empty(self): # Проверка на пустоту
        return self.head is None

    
    def add_start(self, data): # Добавление элемента в начало списка
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def add_end(self, data): # Добавление элемента в конец списка
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    
    def add_n(self, n, data): # Добавление элемента после n-го элемента
        if n < 0:
            print("Ошибка ввода номера элемента")
            return
        new_node = Node(data)
        current_node = self.head
        for i in range(n):
            if current_node is None:
                print("Ошибка ввода номера элемента")
                return
            current_node = current_node.next
        if current_node is None:
            print("Ошибка ввода номера элемента")
            return
        new_node.next = current_node.next
        current_node.next = new_node

    
    def count_elements(self): # Получение количества элементов в списке
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    
    def except_first(self): # Получение списка всех элементов, кроме первого
        if self.head is None:
            return []
        result = []
        current_node = self.head.next  # Начинаем со второго элемента
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result


commanda=int(input("Введите номер операции: 0 - завершение программы, 1 - проверка списка на пустоту, 2 - добавление элемента в начало списка, 3 - добавление элемента в конец списка, 4 - добавление элемента после n-го элемента, 5 - проверка количества элементов в списке, 6 - вывод всех элементов списка, кроме 1-ого:"))
linked_list = Linked_List()
while commanda!=0:
    if commanda==1:
         print("Список пуст?", linked_list.is_empty())  
    if commanda==2:
        n=int(input("Введите элемент:"))
        linked_list.add_start(n)
    elif commanda==3:
        n=int(input("Введите элемент:"))
        linked_list.add_end(n)
    elif commanda==4:
        n=int(input("Введите элемент:"))
        ind=int(input("Введите номер позиции элемента, после которого нужно поставить новый:"))
        linked_list.add_n(ind-1, n)  # Вставляем 4 после второго элемента (индекс 1)
    elif commanda==5:
        print("Количество элементов в списке:", linked_list.count_elements())
    elif commanda==6:
         print("Элементы списка, кроме первого:", linked_list.except_first())  
    
    commanda=int(input("Введите номер операции: 0 - завершение программы, 1 - проверка списка на пустоту, 2 - добавление элемента в начало списка, 3 - добавление элемента в конец списка, 4 - добавление элемента после n-го элемента, 5 - проверка количества элементов в списке, 6 - вывод всех элементов списка, кроме 1-ого:"))



   
     
   