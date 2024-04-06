print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

for i in range(2):
    print('belajar python')



print(f'\n{15*'*'} Pythonic {15*'*'}')

for _ in range(2):
    print('belajar python')

my_list = ['ketsar','nabil',10,20,'jakarta']

a,b, *_ = my_list

print(f'variable my_list = {my_list}')
print(f'nilai a = {a} | nilai b = {b}')