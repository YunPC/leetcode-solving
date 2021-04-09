# s = "A man, a plan, a canal: Panama"
s = "race a car"
s = s.lower()

start = []
end = []
for c in s:
    if c.isalpha() or c.isdigit():
        start.append(c)

for i in range(len(s)-1, -1, -1):
    if s[i].isalpha() or s[i].isdigit():
        end.append(s[i])

print(str(start) == str(end))
