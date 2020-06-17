
with open('sophiesblog', 'r') as myfile:
  data = myfile.read().replace('/n', '')
lines = data.split(" ")
ans = []
print(lines)
for line in lines:
  ans.append(int(line, 2))
print(ans)
print([chr(x) for x in ans])
