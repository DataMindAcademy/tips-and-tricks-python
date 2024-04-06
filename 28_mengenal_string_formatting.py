
nama = input('masukan nama anda = ')
usia = int(input('masukan usia anda = '))

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

print('nama saya ' + nama + ' saat ini saya berusia ' + str(usia))

print(f'\n{15*'*'} Pythonic {15*'*'}')

print('nama saya {1}, saat ini saya berusia {0}'.format(usia, nama))
print(f'nama saya {nama}, saat ini saya berusia {usia}')

mahasiswa = {
    'nama' : nama,
    'usia' : usia
}

print('nama saya {nama}, saat ini saya berusia {usia}'.format(**mahasiswa))
