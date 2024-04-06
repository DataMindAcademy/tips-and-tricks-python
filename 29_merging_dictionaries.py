print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

data1 = {
    'nim':1001, 
    'nama':'ketsar'
}

data2 = {
    'ipk':4.00,
    'semester':8
}

merging_dictionaries = {}

for dic1 in data1:
    merging_dictionaries[dic1] = data1[dic1]

for dic2 in data2:
    merging_dictionaries[dic2] = data2[dic2]
    
print(f'hasil = {merging_dictionaries}')



print(f'\n{15*'*'} Pythonic {15*'*'}')

data3 = {
    'hobi':'mengeksplor',
    'asal':'jakarta'
}

merging_dictionaries = {**data1, **data2, **data3}
print(f'hasil = {merging_dictionaries}')
