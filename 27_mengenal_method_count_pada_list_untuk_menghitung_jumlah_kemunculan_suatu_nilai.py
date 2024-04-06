import os

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')


input_user = int(input('\nmasukan angka (1-10) = '))

os.system('cls' if os.name == 'nt' else 'clear')

list_numbers = [1,1,1,2,2,2,3,2,3,2,3,2,4,5,6,6,6,4,5,7,4,1,3,8,9,9,0,9,4,5]
sum_number = input_user
count = 0

for num in list_numbers:
    if num == sum_number:
        count += 1

print(f'saya mencari angka {sum_number} dan saya menemukan sebanyak {count} kali')






print(f'\n{15*'*'} Pythonic {15*'*'}')

sum_number = input_user
count = list_numbers.count(sum_number)
print(f'saya mencari angka {sum_number} dan saya menemukan sebanyak {count} kali')