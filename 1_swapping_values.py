# tidak pythonic

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

a = 10
b = 20

print(f'''
{10*'-'} sebelum {10*'-'} 
a = {a}
b = {b}
''')

a = b
c = a

print(f'''
{10*'-'} sesudah {10*'-'} 
a = {a}
b = {b}
''')


# pythonic
print(f'\n{15*'*'} Pythonic {15*'*'}')

a, b = 10, 20

print(f'''
{10*'-'} sebelum {10*'-'} 
a = {a}
b = {b}
''')

a, b = b, a

print(f'''
{10*'-'} sesudah {10*'-'} 
a = {a}
b = {b}
''')