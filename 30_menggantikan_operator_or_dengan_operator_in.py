nama = 'rizal'

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

if nama == 'nabil' or nama == 'irwan' or nama == 'ketsar':
    print(f'{nama.capitalize()} siswa terbaik')
else:
    print(f'{nama.capitalize()} bukan siswa terbaik')




print(f'\n{15*'*'} Pythonic {15*'*'}')

if nama in ('ketsar','irwan','nabil'):
    print(f'{nama.capitalize()} siswa terbaik')
    
else:
    print(f'{nama.capitalize()} bukan siswa terbaik')