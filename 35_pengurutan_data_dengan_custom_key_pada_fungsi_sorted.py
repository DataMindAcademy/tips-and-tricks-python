print(f'\n{15*'*'} Tidak Pythonic (Langkah Konvensional) {15*'*'}')

kota = ['dki jakarta','medan','gorontalo','pontianak','kabupaten bandung','bogor kota']

print(f'sebelum = {kota}')

for i in range(len(kota) - 1):
    for j in range(i + 1, len(kota)):
        if kota[i].split()[-1] > kota[j].split()[-1]:
            kota[i], kota[j] = kota[j], kota[i]

print(f'setelah = {kota}')




print(f'\n{15*'*'} Pythonic {15*'*'}')

# def custom_key(words):
#     return words.split()[-1]

# kota = ['dki jakarta','medan','gorontalo','pontianak','kabupaten bandung','bogor kota']
# terurut = sorted(kota, key=custom_key)

# print(f'sebelum = {kota}')
# print(f'setelah = {terurut}')


kota = ['dki jakarta','medan','gorontalo','pontianak','kabupaten bandung','bogor kota']

terurut_lambda = sorted(kota, key=lambda data:data.split()[-1])

print(f'\nsebelum lambda = {kota}')
print(f'setelah lambda = {terurut_lambda}')
