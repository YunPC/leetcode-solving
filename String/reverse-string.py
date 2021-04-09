
# s = ['h', 'e', 'l', 'l', 'o']
s = ['H', 'a', 'n', 'n', 'a', 'h']
l = len(s)-1

for i in range(len(s)//2):
    s[i], s[l-i] = s[l-i], s[i]

print(s)
