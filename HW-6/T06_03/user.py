"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""
import math

size = 11
keys = []
values = []
count = 0

EMPTY = "EMPTY"
DELETED = "DELETED"


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global size, keys, values, count
    size = 11
    count = 0
    keys = [EMPTY] * size
    values = [EMPTY] * size


def _hash(key):
    global size
    h = 0
    for char in key:
        h = (h * 37 + ord(char)) % size # h=37
    return h


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def rehash():
    global size, keys, values, count
    
    old_size = size
    old_keys = keys
    old_values = values
    
    size = size * 2 + 1
    while not is_prime(size):
        size += 2
    
    keys = [EMPTY] * size
    values = [EMPTY] * size
    count = 0
    
    for i in range(old_size):
        if old_keys[i] not in (EMPTY, DELETED):
            author = old_keys[i]
            author_books = old_values[i]
            
            idx = _hash(author)
            while keys[idx] is not EMPTY:
                idx = (idx + 1) % size
            
            keys[idx] = author
            values[idx] = author_books
            count += 1


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count
    
    if count >= size * 0.7: # 70%  
        rehash()
    
    idx = _hash(author)
    first_del = -1
    
    while keys[idx] is not EMPTY:
        if keys[idx] == author:
            values[idx].add(title)
            return
        
        if keys[idx] == DELETED and first_del == -1:
            first_del = idx
            
        idx = (idx + 1) % size
    
    if first_del != -1:
        idx = first_del
    
    keys[idx] = author
    values[idx] = {title}
    count += 1


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    if size == 0:
        return False
    
    idx = _hash(author)
    while keys[idx] is not EMPTY:
        if keys[idx] == author:
            return title in values[idx]
        idx = (idx + 1) % size
        
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    global count
    
    if size == 0:
        return

    idx = _hash(author)
    while keys[idx] is not EMPTY:
        if keys[idx] == author:
            if title in values[idx]:
                values[idx].remove(title)
                if len(values[idx]) == 0:
                    keys[idx] = DELETED
                    values[idx] = DELETED
                    count -= 1
            return
        idx = (idx + 1) % size


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    if size == 0:
        return []

    idx = _hash(author)
    while keys[idx] is not EMPTY:
        if keys[idx] == author:
            ans = list(values[idx])
            ans.sort()
            return ans
        idx = (idx + 1) % size
        
    return []