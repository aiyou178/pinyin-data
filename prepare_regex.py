import re

data = []
with open('pinyin.txt') as f:
  for index, i in enumerate(f):
    if index < 2:
      continue
    unicode, character = re.match(r'U\+(.+):.*#\s+(.+)', i).groups()
    data.append((unicode, character))
data_int = sorted((ord(j), j) for i, j in data)
pattern = ['['] + [data[0][1]]
for i in range(1, len(data) - 1):
  pre = data_int[i][0] - data_int[i - 1][0] == 1
  post = data_int[i + 1][0] - data_int[i][0] == 1
  if pre and post:
    if pattern[-1] != '-':
      pattern.append('-')
    continue
  if not pre and not post:
    pattern.append(data_int[i][1])
  elif pre and not post:
    pattern.append(data_int[i][1])
  else:
    pattern.append(data_int[i][1])
pattern.append(data_int[-1][1])
pattern.append(']+')
regex = ''.join(pattern)
print(len(regex), regex[:10], regex[-10:])
with open('regex.txt', 'w') as f:
  f.write(regex)
