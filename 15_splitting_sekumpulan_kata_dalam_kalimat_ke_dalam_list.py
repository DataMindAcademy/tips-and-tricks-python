str = 'saya seorang scientist'


print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

new_str = []
words = ''
for letter in str:
    if letter != ' ':
        words += letter

    else:
        new_str.append(words)
        words = ''
new_str.append(words)

print(f'new_str = {new_str}')





print(f'\n{15*'*'} Pythonic {15*'*'}')

str = 'halo, nama saya ketsar, halo kawan'
new_str = str.split(',')
print(f'new_str = {new_str}')