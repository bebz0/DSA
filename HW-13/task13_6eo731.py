import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    pref_exp = input_data[0]
    dct = {
        '+': 1, 
        '-': 1, 
        '*': 2, 
        '/': 2
    }
    
    stack = []    
    for char in reversed(pref_exp):
        if char.isalpha():
            stack.append((char, None))
        else:
            left_exp, left_op = stack.pop()
            right_exp, right_op = stack.pop()
            
            left_needs = False
            if left_op is not None and dct[char] > dct[left_op]:
                left_needs = True
                
            right_n = False
            if right_op is not None:
                if dct[char] > dct[right_op]:
                    right_n = True
                elif dct[char] == dct[right_op] and char in ('-', '/'):
                    right_n = True
                    
            left_str = f"({left_exp})" if left_needs else left_exp
            right_str = f"({right_exp})" if right_n else right_exp
            
            new_expr = left_str + char + right_str
            
            stack.append((new_expr, char))
            
    print(stack[0][0])

if __name__ == '__main__':
    solve()