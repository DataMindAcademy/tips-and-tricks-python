print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

kota = ['jakarta','medan','gorontalo','pontianak','bandung','bogor']
print(f'sebelum = {kota}')
kota.sort() #! hanya bisa diterapkan pada sequence data type yang bersifat mutable
print(f'setelah = {kota}')


print(f'\n{15*'*'} Pythonic {15*'*'}')

kota = ['jakarta','medan','gorontalo','pontianak','bandung','bogor']
print(f'sebelum = {kota}')
terurut = sorted(kota) #! bisa diterapkan pada semua sequence data type apapun
print(f'setelah = {terurut}')