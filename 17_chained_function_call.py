def tambah(a,b):
    return a + b

def kali(a,b):
    return a * b

x, y = 5,10
kondisi = False
hasil = 0

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

if kondisi: hasil = kali(x,y)
else: hasil = tambah (x,y)

print(f'hasil = {hasil}')





print(f'\n{15*'*'} Pythonic {15*'*'}')

hasil = (kali if kondisi else tambah)(x,y)

print(f'hasil = {hasil}')