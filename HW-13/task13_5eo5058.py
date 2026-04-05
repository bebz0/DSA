import sys
def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    stack = []
    brackets_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in input_data:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                print("no")
                return
            top_element = stack.pop()            
            if top_element != brackets_map[char]:
                print("no")
                return
    if len(stack) == 0:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    solve()