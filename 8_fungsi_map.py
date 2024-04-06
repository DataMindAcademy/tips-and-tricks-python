def kuadrat(x):
    return x * 2

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

my_list = [2,4,6]
your_list = []

for num in my_list:
    your_list.append(kuadrat(num))

print(f'''
my_list = {my_list}
your_list = {your_list}
''')


print(f'\n{15*'*'} Pythonic {15*'*'}')

my_list = [2,4,6]
your_list = list(map(kuadrat, my_list))

print(f'''
my_list = {my_list}
your_list = {your_list}
''')