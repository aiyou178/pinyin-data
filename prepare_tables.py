import re
import json
character_pronounciation = re.compile(r'.+:\s*([^\s]*)\s*#\s+(.+)')
normalizer = re.compile(r'(.)')
without_initials = ['ou', 'eng', 'o', 'e', 'er', 'ei', 'ai', 'an', 'en', 'a', 'ao', 'ang']
initials = re.compile(r'(b|p|m|f|d|t|n|l|g|k|h|j|q|x|zh|ch|sh|r|z|c|s|y|w)')
startwith = re.compile(r'(b|p|m|f|d|t|n|l|g|k|h|j|q|x|zh|ch|sh|r|z|c|s|y|w|a|o|e)')
data = dict()
with open('ok.json', 'r') as f:
    pinyins = json.load(f)
pinyins[','] = ','
spellings = set()
with open('pinyin.txt') as f:
  for i in f:
    if match := character_pronounciation.match(i):
      pronounciation, character = match.groups()
      normalized = normalizer.sub(lambda m: pinyins.get(m.group()),
                                       pronounciation)
      data[character] = set(normalized.split(','))
      spellings |= data[character]
result = []
for k, v in data.items():
  for i in v:
    result.append(f'{k},{i}\n')
with open('pinyin_spelling.txt', 'w') as f:
  f.writelines(result)
result = []
for k, v in data.items():
  for i in {startwith.match(j).groups() for j in v}:
    if not i:
      raise Exception(k, v)
    result.append(f'{k},{i[0]}\n')
with open('pinyin_initials.txt', 'w') as f:
  f.writelines(result)
without_initials = [i for i in spellings if not initials.match(i)]
print(len(spellings), len(without_initials), without_initials)


