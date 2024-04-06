print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

def multiple_return_values():
    nama = 'ketsar'
    nim = 1001
    ipk = 4.0
    mahasiswa = (nama, nim, ipk)
    return mahasiswa

results = multiple_return_values()

print(f'hasilnya adalah {results}')

print(f'nama = {results[0]}')
print(f'nim = {results[1]}')
print(f'ipk = {results[2]}')




print(f'\n{15*'*'} Pythonic {15*'*'}')

def multiple_return_values():
    nama = 'ketsar'
    nim = 1001
    ipk = 4.0
    return nama, nim, ipk

x,y,z = multiple_return_values()

print(f'nama = {x}')
print(f'nim = {y}')
print(f'ipk = {z}')