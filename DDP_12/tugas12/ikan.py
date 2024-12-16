from Animal import Animal

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.warna = warna
        self.habitat = habitat
    def info_ikan(self):
        super().info_animal,
        print(f"warna \t\t\t :", self.warna,
                "\nHabitat \t\t : ", self.habitat)
ikan_tuna = ikan("tuna", "cumi cumi", "air", "bertelur", "kuning", "perairan laut dalam")
ikan_tongkol = ikan("tongkol", "cumi cumi", "air", "bertelur", " biru kehijauan, putih", "perairan dangkal dekat pesisir")
ikan_tuna.info_ikan()
ikan_tongkol.info_ikan()