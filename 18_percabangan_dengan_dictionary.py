def mahasiswa_satu():
    print('ketsar | 1001')

def mahasiswa_dua():
    print('nabil | 2002')

def mahasiswa_tiga():
    print('irwan | 3003')

status = 'kumlot'


print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

if status == 'kumlot':
    mahasiswa_satu()
elif status == 'hampir kumlot':
    mahasiswa_tiga()
else: 
    mahasiswa_dua()





print(f'\n{15*'*'} Pythonic {15*'*'}')

status = 'tidak kumlot'

switch = {
    'kumlot':mahasiswa_satu,
    'hampir kumlot':mahasiswa_tiga,
    'tidak kumlot':mahasiswa_dua
}

switch[status]()