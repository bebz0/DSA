"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
Реалізація за допомогою хеш-таблиці з методом ланцюжків.
"""
import math

class Node:
    def __init__(self, key):
        self.key = key          # Ім'я автора
        self.value = set()      # Множина книг цього автора
        self.next = None        # Вказівник на наступний вузол у ланцюжку

size = 11
slots = []
count = 0


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global size, slots, count
    size = 11
    count = 0
    slots = [None for _ in range(size)]


def _hash(key):
    global size
    h = 0
    for char in key:
        h = (h * 31 + ord(char)) % size
    return h


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def rehash():
    global size, slots, count
    old_slots = slots
    
    size = size * 2 + 1
    while not is_prime(size):
        size += 2
        
    slots = [None for _ in range(size)]
    count = 0
    
    for node in old_slots:
        curr = node
        while curr is not None:
            h = _hash(curr.key)
            
            new_node = Node(curr.key)
            new_node.value = curr.value
            
            new_node.next = slots[h]
            slots[h] = new_node
            
            count += 1
            curr = curr.next


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count
    
    if count >= size * 0.7:
        rehash()
        
    h = _hash(author)
    node = slots[h]
    
    while node is not None:
        if node.key == author:
            node.value.add(title)
            return
        node = node.next
        
    new_node = Node(author)
    new_node.value.add(title)
    new_node.next = slots[h]
    slots[h] = new_node
    count += 1


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    if size == 0:
        return False
        
    h = _hash(author)
    node = slots[h]
    
    while node is not None:
        if node.key == author:
            return title in node.value
        node = node.next
        
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global count
    if size == 0:
        return
        
    h = _hash(author)
    node = slots[h]
    prev = None
    
    while node is not None:
        if node.key == author:
            if title in node.value:
                node.value.remove(title)
                
                if len(node.value) == 0:
                    if prev is None:
                        slots[h] = node.next
                    else:
                        prev.next = node.next
                    count -= 1
            return
            
        prev = node
        node = node.next


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    if size == 0:
        return []
        
    h = _hash(author)
    node = slots[h]
    
    while node is not None:
        if node.key == author:
            ans = list(node.value)
            ans.sort()
            return ans
        node = node.next
        
    return []