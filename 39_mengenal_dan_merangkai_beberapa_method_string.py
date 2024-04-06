data_str = '  Bahasa pemrograman Python: guido vAn roSSum   '

print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

menghilangkan_spasi = data_str.strip()

print(f'''
sebelum dipangkas = {data_str}
setelah dipangkas = {menghilangkan_spasi}
''')

data_str = menghilangkan_spasi.upper()

print(f'''
normal = {menghilangkan_spasi}
ubah = {data_str}
''')

data_str = data_str.replace(':',',')

print(f'''
normal = {menghilangkan_spasi}
ubah = {data_str}
''')



data_str = '  Bahasa pemrograman Python: guido vAn roSSum   '

data_str = data_str.strip().upper().replace(':',' -')

print(f'''
ubah = {data_str}
''')

