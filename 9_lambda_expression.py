print(f'\n{15*'*'} Pythonic {15*'*'}')

my_list = [2,4,6]
your_list = list(map(lambda x : x * 2, my_list))

print(f'''
my_list = {my_list}
your_list = {your_list}
''')