"""
if multiple pronunciations are available, the first one is used
syllable divider is removed
tone numbers are removed
"""
import re

with open('regex.txt', 'r') as f:
  character_regex = f.read().strip()

CHARACTERS = re.compile(r'^' + character_regex + r'$')
AVAILABLE_PINYINS = {
    'a',
    'ai',
    'an',
    'ang',
    'ao',
    'ba',
    'bai',
    'ban',
    'bang',
    'bao',
    'bei',
    'ben',
    'beng',
    'bi',
    'bian',
    'biao',
    'bie',
    'bin',
    'bing',
    'bo',
    'bu',
    'ca',
    'cai',
    'can',
    'cang',
    'cao',
    'ce',
    'cen',
    'ceng',
    'cha',
    'chai',
    'chan',
    'chang',
    'chao',
    'che',
    'chen',
    'cheng',
    'chi',
    'chong',
    'chou',
    'chu',
    'chuai',
    'chuan',
    'chuang',
    'chui',
    'chun',
    'chuo',
    'ci',
    'cong',
    'cou',
    'cu',
    'cuan',
    'cui',
    'cun',
    'cuo',
    'da',
    'dai',
    'dan',
    'dang',
    'dao',
    'de',
    'dei',
    'den',
    'deng',
    'di',
    'dian',
    'diao',
    'die',
    'ding',
    'diu',
    'dong',
    'dou',
    'du',
    'duan',
    'dui',
    'dun',
    'duo',
    'e',
    'ei',
    'en',
    'eng',
    'er',
    'fa',
    'fan',
    'fang',
    'fei',
    'fen',
    'feng',
    'fo',
    'fou',
    'fu',
    'ga',
    'gai',
    'gan',
    'gang',
    'gao',
    'ge',
    'gei',
    'gen',
    'geng',
    'gong',
    'gou',
    'gu',
    'gua',
    'guai',
    'guan',
    'guang',
    'gui',
    'gun',
    'guo',
    'ha',
    'hai',
    'han',
    'hang',
    'hao',
    'he',
    'hei',
    'hen',
    'heng',
    'hong',
    'hou',
    'hu',
    'hua',
    'huai',
    'huan',
    'huang',
    'hui',
    'hun',
    'huo',
    'i',
    #'ing',
    #'iu',
    'ji',
    'jia',
    'jian',
    'jiang',
    'jiao',
    'jie',
    'jin',
    'jing',
    'jiong',
    'jiu',
    'ju',
    'juan',
    'jue',
    'jun',
    'ka',
    'kai',
    'kan',
    'kang',
    'kao',
    'ke',
    'kei',
    'ken',
    'keng',
    'kong',
    'kou',
    'ku',
    'kua',
    'kuai',
    'kuan',
    'kuang',
    'kui',
    'kun',
    'kuo',
    'la',
    'lai',
    'lan',
    'lang',
    'lao',
    'le',
    'lei',
    'leng',
    'li',
    'lia',
    'lian',
    'liang',
    'liao',
    'lie',
    'lin',
    'ling',
    'liu',
    'long',
    'lou',
    'lu',
    'luan',
    'lun',
    'luo',
    'lv',
    'lve',
    'ma',
    'mai',
    'man',
    'mang',
    'mao',
    'me',
    'mei',
    'men',
    'meng',
    'mi',
    'mian',
    'miao',
    'mie',
    'min',
    'ming',
    'miu',
    'mo',
    'mou',
    'mu',
    'na',
    'nai',
    'nan',
    'nang',
    'nao',
    'ne',
    'nei',
    'nen',
    'neng',
    'ng',
    'ni',
    'nian',
    'niang',
    'niao',
    'nie',
    'nin',
    'ning',
    'niu',
    'nong',
    'nu',
    'nuan',
    'nun',
    'nuo',
    'nv',
    'nve',
    'o',
    'ou',
    'pa',
    'pai',
    'pan',
    'pang',
    'pao',
    'pei',
    'pen',
    'peng',
    'pi',
    'pian',
    'piao',
    'pie',
    'pin',
    'ping',
    'po',
    'pou',
    'pu',
    'qi',
    'qia',
    'qian',
    'qiang',
    'qiao',
    'qie',
    'qin',
    'qing',
    'qiong',
    'qiu',
    'qu',
    'quan',
    'que',
    'qun',
    #'r',
    'ran',
    'rang',
    'rao',
    're',
    'ren',
    'reng',
    'ri',
    'rong',
    'rou',
    'ru',
    'ruan',
    'rui',
    'run',
    'ruo',
    'sa',
    'sai',
    'san',
    'sang',
    'sao',
    'se',
    'sen',
    'seng',
    'sha',
    'shai',
    'shan',
    'shang',
    'shao',
    'she',
    'shei',
    'shen',
    'sheng',
    'shi',
    'shou',
    'shu',
    'shua',
    'shuai',
    'shuan',
    'shuang',
    'shui',
    'shun',
    'shuo',
    'si',
    'song',
    'sou',
    'su',
    'suan',
    'sui',
    'sun',
    'suo',
    'ta',
    'tai',
    'tan',
    'tang',
    'tao',
    'te',
    'teng',
    'ti',
    'tian',
    'tiao',
    'tie',
    'ting',
    'tong',
    'tou',
    'tu',
    'tuan',
    'tui',
    'tun',
    'tuo',
    'u',
    'ui',
    'un',
    'ur',
    #'v',
    'wa',
    'wai',
    'wan',
    'wang',
    'wei',
    'wen',
    'weng',
    'wo',
    'wu',
    'xi',
    'xia',
    'xian',
    'xiang',
    'xiao',
    'xie',
    'xin',
    'xing',
    'xiong',
    'xiu',
    'xu',
    'xuan',
    'xue',
    'xun',
    'ya',
    'yan',
    'yang',
    'yao',
    'ye',
    'yi',
    'yin',
    'ying',
    'yo',
    'yong',
    'you',
    'yu',
    'yuan',
    'yue',
    'yun',
    'za',
    'zai',
    'zan',
    'zang',
    'zao',
    'ze',
    'zei',
    'zen',
    'zeng',
    'zha',
    'zhai',
    'zhan',
    'zhang',
    'zhao',
    'zhe',
    'zhen',
    'zheng',
    'zhi',
    'zhong',
    'zhou',
    'zhu',
    'zhua',
    'zhuai',
    'zhuan',
    'zhuang',
    'zhui',
    'zhun',
    'zhuo',
    'zi',
    'zong',
    'zou',
    'zu',
    'zuan',
    'zui',
    'zun',
    'zuo',
    # added
    'dia',
    'lo',
    'tei',
    'nou',
    'biang',
}
NUMBER_REGEX = re.compile(r'[\d\^]+')
characters = dict()
words = dict()
item_mapper = {
    'lue': 'lve',
    'nue': 'nve',
    'zhei': 'zhe',
    'r': 'er',
    'n': 'ng',
    'hng': 'heng',
    'm': 'wu',
}
with open('polyphone.txt') as f:
  for i in f:
    i = i.strip()
    if not i:
      continue
    # character
    i = re.sub(r'u:', 'v', i)
    if i.startswith('#'):
      # we use character's pronounciations from pinyin_analysis.txt
      continue
      i = i[1:]
      character, pronounciation = i.split('=', maxsplit=1)
      if not CHARACTERS.match(character):
        print('unknown character:', character)
        continue
      if ',' in pronounciation:
        # multiple pronounciations
        continue
      pronounciation = NUMBER_REGEX.sub('', pronounciation)
      pronounciation = item_mapper.get(pronounciation, pronounciation)
      if pronounciation not in AVAILABLE_PINYINS:
        print('unknown pinyin:', character, pronounciation)
        continue
      if character in characters:
        # the first one is the most common
        continue
      characters[character] = pronounciation
    else:
      # word
      word, pronounciation = i.split('=', maxsplit=1)
      if not CHARACTERS.match(word):
        print('unknown word:', word)
        continue
      pronounciation = NUMBER_REGEX.sub('', pronounciation)
      pronounciations = pronounciation.split()
      pronounciations = [item_mapper.get(i, i) for i in pronounciations]
      if set(pronounciations) - AVAILABLE_PINYINS:
        print('unknown word pinyin:', word, pronounciations)
        continue
      if len(word) < 2:
        continue
        # is a character
        if word in characters:
          continue
        characters[word] = pronounciations[0]
      else:
        if word in words:
          if len(words[word]) != len(pronounciations):
            print('word pronounciations length mismatch', word, words[word],
                  pronounciations)
            continue
          combined_pronounciations = []
          for i, j in zip(words[word], pronounciations):
            if i == j:
              combined_pronounciations.append(i)
            else:
              combined_pronounciations.append(f'{i}|{j}')
          words[word] = combined_pronounciations
        else:
          words[word] = pronounciations

# add single non polyphonic pinyin
with open('pinyin_analysis.txt') as f:
  for i in f:
    i = re.sub(r'u:', 'v', i)
    character, pronounciation = i.strip().split('=', maxsplit=1)
    if not pronounciation:
      continue
    if character in characters:
      print('duplicate character:', character)
      continue
    pronounciation = NUMBER_REGEX.sub('', pronounciation)
    pronounciations = pronounciation.split(',')
    pronounciations = [item_mapper.get(i, i) for i in pronounciations]
    if set(pronounciations) - AVAILABLE_PINYINS:
      print('unknown character pinyin:', character, pronounciations)
      continue
    characters[character] = set(pronounciations)
# complement missing characters
with open('pinyin_spelling.txt') as f:
  for i in f:
    character, pronounciations = i.strip().split(',', maxsplit=1)
    if character in characters:
      continue
    pronounciations = pronounciations.strip('|').split('|')
    pronounciations = [item_mapper.get(i, i) for i in pronounciations]
    if set(pronounciations) - AVAILABLE_PINYINS:
      print('unknown complement character pinyin:', character, pronounciations)
      continue
    characters[character] = set(pronounciations)
with open('polyphone.csv', 'w') as f:
  for k, v in sorted(characters.items()):
    f.write(f'{k},{"|".join(sorted(v))}\n')
  for k, v in sorted(words.items()):
    f.write(f'{k},{" ".join(v)}\n')
print(len(characters), len(words))
