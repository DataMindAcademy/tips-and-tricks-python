print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')
numbers = [10,20,30,40,50,60,70,80,90]
new_numbers = []
for i in range(2,5):
    new_numbers.append(numbers[i])

print(f'new_numbers = {new_numbers}')





print(f'\n{15*'*'} Pythonic {15*'*'}')

new_numbers = numbers[2:]
print(f'new_numbers = {new_numbers}')

new_numbers = numbers[:5]
print(f'new_numbers = {new_numbers}')

str = 'BERSEKOLAH'
new_str = str[3:10]
print(f'new_str = {new_str}')
