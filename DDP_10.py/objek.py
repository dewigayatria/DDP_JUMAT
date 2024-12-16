class orang:

    #variabel(properti)
    def __init__(self, nama, usia, gender, alamat):
        self.nama = nama
        self.usia = usia
        self.gender = gender
        self.alamat

    #fungsi (method)
    def ngomong(self):
        print("saya bisa bicara")

    def jalan(self, kata):
        print("saya bisa jalan", kata)

#objek1
supir = orang()
print(supir.nama)
supir.jalan("kapan?")
supir.sim ="A"
print(supir.sim)

#objek2
mahasiswa = orang()