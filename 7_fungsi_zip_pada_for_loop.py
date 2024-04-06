print(f'\n{15*'*'} Pythonic {15*'*'}')

nim = [1001, 1002, 1003]
nama = ['ketsar','bagas','anjas']
hobi = ['belajar','bermain','berenang']

for d_nim, d_nama, d_hobi in zip(nim, nama, hobi):
    print(f'{d_nim} - {d_nama} - {d_hobi}')