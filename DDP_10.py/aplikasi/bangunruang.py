import math

def l_balok(p,l,t):
    hitung = 2 * (p*l)+(p*t)+(l*t) 
    print(f'luas balok adalah {hitung}')

def l_kubus(s):
    hitung = 6 * s ** 2
    print(f'luas kubus adalah {hitung}')

def l_tabung(r, t):
    hitung =  2 * math.pi * r * (r+t)
    print(f'luas tabung adalah {hitung}')

def l_limas_segitiga(tinggi_alas, alas, tinggi1, tinggi2, tinggi3):
    luas_alas = 1/2 * tinggi_alas * alas
    total_l_tegak = 1/2 * alas * tinggi1 + 1/2 * alas * tinggi2 + 1/2 * alas * tinggi3 
    hitung = luas_alas + total_l_tegak
    print(f'luas limas adalah {hitung}')

def l_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma, p1, p2, p3):
    hitung = alas * tinggi_segitiga + ((p1+p2+p3) * tinggi_prisma)
    print(f'luas prisma segitiga adalah {hitung}')