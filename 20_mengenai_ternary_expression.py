
print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

a = -15
if a < 0:
    b = 'angka negatif'
else: 
    b = 'angka positif'

print(f'{a} bernilai {b}')

print(f'\n{15*'*'} Pythonic {15*'*'}')

b = 'angka negatif' if a < 0 else 'angka positif'

print(f'{a} bernilai {b}')