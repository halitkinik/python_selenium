class Banka:
    def krediBasvur(self):
        print("Krediye başvuruldu")

    def krediHesapla(self):
        print("Hesaplar yapildi")


banka = Banka()
banka.krediBasvur()


class Matematik:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Matematik başladi")
    
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2

matematik = Matematik(5,3)
sonuc = matematik.carp()
print(f"sonuc: {sonuc}")


class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

musteri1 = Person("Halit","KINIK")
musteri2 = Person("Taha","KINIK")
musteri3 = Person("Hasan","KINIK")
print(musteri1.name)
