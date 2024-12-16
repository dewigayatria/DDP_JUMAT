from Animal import Animal

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, habitat, berbisa_atau_tidak):
        super().__init__(nama, makanan, hidup, berkembang_biak),
        self.habitat = habitat
        self.berbisa_atau_tidak = berbisa_atau_tidak
    def info_ular(self):
        super().info_animal,
        print(f"Berbisa atau Tidak \t\t\t :", self.berbisa_atau_tidak,
                "\nHabitat \t\t : ", self.habitat)
ular_tanah = ular("tanah", "tikus", "darat", "bertelur", "perkebunan", "berbisa")
ular_air = ular("air", "amfibi", "perairan", "melahirkan", " sungai rawa, kolam dan perairan lainnya", "tidak")
ular_tanah.info_ular()
ular_air.info_ular()