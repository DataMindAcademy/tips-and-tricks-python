print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')
numbers = [1,2,3,4,5,6,7,8]
new_numbers = []


for i in range(len(numbers)):
    reverse_numbers = len(numbers) - 1 - i
    new_numbers.append(numbers[reverse_numbers])
    

print(f'new_numbers = {new_numbers}')





print(f'\n{15*'*'} Pythonic {15*'*'}')
new_numbers = numbers[::-1]
print(f'new_numbers = {new_numbers}')





print(f'\n{15*'*'} Pythonic {15*'*'}')
numbers = [1,2,3,4,5,6,7,8]
numbers.sort(reverse=True)
print(f'numbers = {numbers}')




print(f'\n{15*'*'} Pythonic {15*'*'}')
str = 'KETSAR'
new_str = str[::-1]
print(f'new_str = {new_str}')
