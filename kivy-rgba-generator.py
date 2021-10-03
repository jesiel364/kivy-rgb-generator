import re

rgb = input('RGB: ')
res = re.split(', ', rgb)
res.append('1')

print(f'{res[0]}/255,{res[1]}/255,{res[2]}/255,{res[3]}')
