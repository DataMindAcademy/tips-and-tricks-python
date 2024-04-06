print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

def penjumlahan(p_satu, p_dua):
    return p_satu + p_dua

my_list = [20,30]
dictionary = {
    'p_satu':150,
    'p_dua':250
}

hasil_satu = penjumlahan(my_list[0],my_list[1])
hasil_dua = penjumlahan(dictionary['p_satu'], dictionary['p_dua'])
print(f'''
hasil my list = {hasil_satu}
hasil dictionary = {hasil_dua}
''')



print(f'\n{15*'*'} Pythonic {15*'*'}')

hasil_satu = penjumlahan(*my_list)
hasil_dua = penjumlahan(**dictionary)
print(f'''
hasil my list = {hasil_satu}
hasil dictionary = {hasil_dua}
''')
