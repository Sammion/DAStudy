'''
@author Sam
@date 2017-12-29
@des 第七章数据规整化：清理、转换、合并、重塑
这里主要练习字符串操作
pandas 有对复杂的模式匹配和文本操作的功能进行加强。
'''

import pandas as pd
import numpy as np
import re

val = 'ab, guido'
tmp = val.split(',')
print(val)
pieces = [x.strip() for x in val.split(',')]
print('================>我就是分隔线 1 <==============')
print(pieces)
f, s = pieces
print(f + '::' + s)
print('::'.join(pieces))
print('a' in pieces)
print('================>我就是分隔线 2 <==============')
print(val.index(','))
print(val.find(':'))
print(val.count(','))
print(val.replace(',', '::'))
print('================>我就是分隔线 3 <==============')
val = '   ad   bu      in morining         hello                  '
val = [x.strip() for x in val.split(' ')]
tmp = [y for y in val if y != '']
print(val)
print(tmp)
print('================>我就是分隔线 3 <==============')
val = 'morning   '
print(val.ljust(12, ':'))
print('================>我就是分隔线 4 <==============')
text = "foo bar\t baz \tqux"
print(re.split('\s+', text))
print('================>我就是分隔线 5 <==============')
regex = re.compile('\s+')
print(regex.split(text))
print(regex.findall(text))
print('================>我就是分隔线 5 <==============')
# http://blog.csdn.net/make164492212/article/details/51656638
pattern1 = '[A-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+'
regex = re.compile(pattern1, flags=re.IGNORECASE)
text = """Dave Sian@163.com
Samqian163@gmail.com
Rob rob@gmail.com
Ryan ran@yahoo.com"""
print(regex.findall(text))
print('================>我就是分隔线 6 <==============')
m = regex.search(text)
print(m)
print(text[m.start():m.end()])
print('================>我就是分隔线 7 <==============')
print(regex.match(text))
print('================>我就是分隔线 8 <==============')
print(regex.sub('Replaced', text))
print('================>我就是分隔线 9 <==============')
pattern1 = '([A-Z0-9_-]+)@([a-zA-Z0-9_-]+)(\.[a-zA-Z0-9_-]+)'
regex = re.compile(pattern1, flags=re.IGNORECASE)
m = regex.match('wem@awesomel.com')
print(m)
print(m.groups())
print(regex.findall(text))
print('================>我就是分隔线 10 <==============')
pattern1 = '([A-Z0-9 _-]+)@([a-zA-Z0-9_-]+)\.([a-zA-Z0-9_-]+)'
regex = re.compile(pattern1, flags=re.IGNORECASE)
print(regex.sub('Username: \0, Domain: \2, Suffix: \3', text))
print('================>我就是分隔线 11 <==============')
regex = re.compile("""
(?P<Username>[A-Za-z0-9_-]+)
@(?P<Domain>[a-zA-Z0-9_-]+)
\.(?P<suffix>[a-zA-Z0-9_-]+)""", flags=re.IGNORECASE | re.VERBOSE)
tmp = 'samqian163@163.com'
m = regex.match(tmp)
print(m.groupdict())

print('================>我就是分隔线 11 <==============')
data = {'Dave': 'Sian@163.com', 'Sam': 'qian163@gmail.com', 'Rob': 'rob@gmail.com', 'Ryan': 'ran@yahoo.com'}
pattern = '([A-Z0-9 _-]+)@([a-zA-Z0-9_-]+)\.([a-zA-Z0-9_-]+)'
data = pd.Series(data)
print(data)
print('================>我就是分隔线 12 <==============')
print(data.isnull())
print('================>我就是分隔线 13 <==============')
print(data.str.contains('gmail'))
print('================>我就是分隔线 14 <==============')
print(data.str.findall(pattern, flags=re.IGNORECASE))
print('================>我就是分隔线 15 <==============')
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)
print(matches[:2])

