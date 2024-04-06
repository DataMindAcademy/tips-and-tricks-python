print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

mahasiswa = [('ketsar', 1001, 4.0), 
             ('nabil', 2002, 3.8), 
             ('kemal', 3003, 3.7)]

nama = []
nim = []
ipk = []

for mhs in mahasiswa:
    nama.append(mhs[0])
    nim.append(mhs[1])
    ipk.append(mhs[2])

print(f'''
nama = {nama}
nim  = {nim}
ipk  = {ipk}
''')



print(f'\n{15*'*'} Pythonic {15*'*'}')

nama, nim, ipk = zip(*mahasiswa)

print(f'''
nama = {nama}
nim  = {nim}
ipk  = {ipk}
''')

