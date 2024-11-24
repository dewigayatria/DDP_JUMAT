# deklarasi fungsi
def hai():
    print('hello selamat datang di NF')
    print()

# panggil fungsi
hai()
hai()
hai()

def cetak(kata):
    print(kata)
cetak('hello world')
cetak('selamat datang di NF')


def biodata(nama, alamat, umur):
    cetak('nama saya adalah'+ nama)
    cetak('alamat saya di'+ alamat)
    cetak('umur saya adalah'+ str(umur))

biodata('ayy', 'bogor', 20)

def perkalian (angka1, angka2):
    cetak(angka1*angka2)

perkalian(3, 4) #12
perkalian(10,10)


def luas_persegi(sisi):
    cetak(sisi*sisi)

luas_persegi(5) #25

def angka1(x):
    return x*2

def angka2(y):
    return y*y

cetak(angka1(2)+angka2(3))