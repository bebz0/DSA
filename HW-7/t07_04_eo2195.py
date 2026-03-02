import sys

def is_prime(number):
    if number % 2 == 0 and number > 2: 
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

class VocabDictionary:
    def __init__(self, capacity=11):
        while not is_prime(capacity):
            capacity += 1
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.used = [False] * self.capacity
        self.word_count = 0

    def _hash(self, word):
        h = 0
        for char in word:
            h = h * 31 + ord(char)
        return h % self.capacity

    def _expand(self):
        old_keys = self.keys
        old_used = self.used
        
        self.capacity = self.capacity * 2 + 1
        while not is_prime(self.capacity):
            self.capacity += 2
            
        self.keys = [None] * self.capacity
        self.used = [False] * self.capacity
        self.word_count = 0
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.add(old_keys[i])
                if old_used[i]:
                    self.mark_used(old_keys[i])

    def add(self, word):
        if self.word_count > 0.5 * self.capacity:
            self._expand()

        index = self._hash(word)
        while self.keys[index] is not None:
            if self.keys[index] == word:
                return
            index = (index + 1) % self.capacity

        self.word_count += 1
        self.keys[index] = word
        self.used[index] = False

    def mark_used(self, word):
        if self.word_count == 0:
            return False
            
        index = self._hash(word)
        while self.keys[index] is not None:
            if self.keys[index] == word:
                self.used[index] = True
                return True
            index = (index + 1) % self.capacity
            
        return False

    def is_all_used(self):
        for i in range(self.capacity):
            if self.keys[i] is not None and not self.used[i]:
                return False
        return True


if __name__ == '__main__':
    input_data = sys.stdin.read().splitlines()
    
    if input_data:
        first_line = input_data[0].split()
        n = int(first_line[0])
        m = int(first_line[1])
        
        starting_capacity = max(11, n * 2 + 1)
        vocab = VocabDictionary(starting_capacity)
        
        for i in range(1, n + 1):
            word = input_data[i].strip().lower()
            if word:
                vocab.add(word)
                
        raw_text = " ".join(input_data[n + 1 : n + 1 + m])
        
        cleaned_chars = []
        for char in raw_text:
            if 'a' <= char.lower() <= 'z':
                cleaned_chars.append(char.lower())
            else:
                cleaned_chars.append(' ')
                
        text_words = "".join(cleaned_chars).split()
        
        unknown_found = False
        for word in text_words:
            if not vocab.mark_used(word):
                unknown_found = True
                break
                
        if unknown_found:
            print("Some words from the text are unknown.")
        elif vocab.is_all_used():
            print("Everything is going to be OK.")
        else:
            print("The usage of the vocabulary is not perfect.")