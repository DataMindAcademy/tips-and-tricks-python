# note = a i e o -> 4130
str_input = 'kota cirebon'
str_output = '' # ! 'k0t4 c1r3b0n'

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')
translasi = {
    'a':'4',
    'i':'1',
    'e':'3',
    'o':'0'
}

for char in str_input:
    val = translasi.get(char)
    str_output += val if val else char

print(f'hasil konversi = {str_output}')



print(f'\n{15*'*'} Pythonic {15*'*'}')
sumber = 'aieo'
tujuan = '4130'
tabel_translasi = str.maketrans(sumber, tujuan)
str_output = str_input.translate(tabel_translasi)

print(tabel_translasi)
print(f'hasil konversi = {str_output}')
