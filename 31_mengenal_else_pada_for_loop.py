print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

kecepatan = [30,40,40,20,40,50,90,60,70]
ambang_batas = 40
laju_normal = True

for laju in kecepatan:
    if laju > ambang_batas:
        laju_normal = False
        print(f'kecepatan {laju}km/jam melampaui ambang batas')
        break

if laju_normal:
    print('laju kendaraan normal')


print(f'\n{15*'*'} Pythonic {15*'*'}')

for laju in kecepatan:
    if laju > ambang_batas:
        laju_normal = False
        print(f'kecepatan {laju}km/jam melampaui ambang batas')
        break
else: 
    print('laju kendaraan normal')