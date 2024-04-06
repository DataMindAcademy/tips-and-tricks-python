
print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

data_list = ['belajar', 'itu', 'asyik']
str = ''
for word in data_list:
    str += f'{word} '

print(f'str = {str}')





print(f'\n{15*'*'} Pythonic {15*'*'}')
    
str = ', '.join(data_list)
print(f'str = {str}')