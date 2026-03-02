import sys

def is_prime(number):
    if number % 2 == 0 and number > 2: 
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

class PhonebookSet:
    def __init__(self, capacity=11):
        while not is_prime(capacity):
            capacity += 1
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.unique_count = 0

    def _get_index(self, number):
        return number % self.capacity

    def _expand(self):
        self.capacity = self.capacity * 2 + 1
        while not is_prime(self.capacity):
            self.capacity += 2
        
        old_table = self.table
        self.table = [None] * self.capacity
        self.unique_count = 0
        
        for item in old_table:
            if item is not None:
                self.add(item)

    def add(self, number):
        if self.unique_count > 0.5 * self.capacity:
            self._expand()

        index = self._get_index(number)
        
        while self.table[index] is not None:
            if self.table[index] == number:
                return
            index = (index + 1) % self.capacity

        self.unique_count += 1
        self.table[index] = number


if __name__ == '__main__':
    raw_data = sys.stdin.read().split()
    
    if raw_data:
        total_calls = int(raw_data[0])
        
        starting_capacity = max(11, total_calls * 2 + 1)
        phonebook = PhonebookSet(starting_capacity)
        
        for i in range(1, total_calls + 1):
            phonebook.add(int(raw_data[i]))
            
        print(phonebook.unique_count)