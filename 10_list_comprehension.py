print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

my_list = []

for num in range(1,51):
    my_list.append(num)

print(f'my_list = {my_list}')




print(f'\n{15*'*'} Pythonic For Loop {15*'*'}')

my_list = [num for num in range(1,51)]

print(f'my_list = {my_list}')





print(f'\n{15*'*'} Pythonic For Loop & If Statement {15*'*'}')

my_list_second = [num for num in range(1,11) if num % 2 == 1]

print(f'my_list_second = {my_list_second}')





print(f'\n{15*'*'} Tidak Pythonic For Loop & Zip {15*'*'}')

nama = ['ketsar', 'nabil', 'sadam']
usia = [18, 10, 23]
my_list_third = []

for i in range(len(nama)):
    my_list_third.append([nama[i], usia[i]])

print(f'my_list_third = {my_list_third}')





print(f'\n{15*'*'} Pythonic For Loop & Zip {15*'*'}')

my_list_third = [[d_nama, d_usia] for d_nama, d_usia in zip(nama, usia)]
print(f'my_list_third = {my_list_third}')




