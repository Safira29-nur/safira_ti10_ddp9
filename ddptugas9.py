#nomor 1
print()
print('## nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    konversi=(celcius*89/5 +32)
    return konversi
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#nomor2
print()
print('## nomor 2 ##')
def ganjil_genap(bilangan):
    penentu=bilangan % 2 == 0
    return penentu
print(ganjil_genap(4))
print(ganjil_genap(7))

#nomor 3
print()
print('## nomor 3 ##')

def nilai(keterangan): 
    if keterangan >= 80:
        print('lulus')
    elif keterangan <= 60:
        print('gagal')
    else :
        print("tidak valid")
        
nilai(90)
nilai(60)

#nomor4
print()
print("## noomor 4 ##")
def bilangan_ganjil(prima):
    return[i for i in range(1, prima, 2)]
print(bilangan_ganjil(20))