data_list = [10,20,30]

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

a = data_list[0]
b = data_list[1]
c = data_list[2]


print(f'''
a = {a} | b = {b} | c = {c}
''')

print(f'\n{15*'*'} Pythonic {15*'*'}')

a,b,c = data_list

print(f'''
a = {a} | b = {b} | c = {c}
''')
