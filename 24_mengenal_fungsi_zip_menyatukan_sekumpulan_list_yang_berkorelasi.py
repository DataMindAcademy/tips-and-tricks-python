print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

nama = ['ketsar','nabil','kemal']
nim = [1001,2002,3003]
ipk = [4.0, 3.8, 3.7]
mahasiswa = []

for mhs in range(len(nama)): 
    mahasiswa.append((nama[mhs], nim[mhs], ipk[mhs]))

print(f'hasilnya = {mahasiswa}')



print(f'\n{15*'*'} Pythonic {15*'*'}')

mahasiswa = list(zip(nama, nim, ipk))
print(f'hasilnya = {mahasiswa}')
