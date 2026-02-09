n = int(input())
s = bin(n)[2:]
maximum = n
for i in range(1, len(s)):
    var = s[i:] + s[:i]
    number = int(var, 2)
    if number > maximum:
        maximum = number
print(maximum)