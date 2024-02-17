class Library:
   def kitapekle(self):
        isim = input("Kitap Ad :")
        yazar = input("Kitap Yazar :")
        sayfa = input("Kitap Sayfa Sayısı :")
        yil = input("Kitabın Basım Yılı : ")
        with open("book.txt","a+",encoding="utf-8") as file:
            file.write(f"{isim},{yazar},{sayfa},{yil}\n")
        print(f"{isim} Adlı Kitap  Başarıyla Eklendi.")
   def kitaplistele(Self):
         print("Listeleme yapılıyor.")
         with open("book.txt","r",encoding="utf-8") as file:
            satirlar = file.read().splitlines()
            for i in satirlar:
                veriler = i.split(",")
                print(veriler[0:2])
   def kitapsil(self):
        kitap_ismi = input("Silmek İstediğiniz Kitabın Adı : ")
        with open("book.txt","r",encoding="utf-8") as file:
            satirlar = file.readlines()
        with open("book.txt","w",encoding="utf-8") as file:
            for i  in satirlar:
                if i[0] == kitap_ismi:
                    file.__del__("kitap_ismi\n")
        print(f"{kitap_ismi} isimli kitap silindi.")            

library = Library()
while True :
   secim = input("Kütüphanemize hoşgeldiniz, Yapmak istediğiniz işlemi seçiniz.\n1-Kitap eklemek istiyorum.\n2-Kitap silmek istiyorum.\n3-Kitapları listelemek istiyorum.\n4- Çıkış yapmak istiyorum.\n Seçim : ")
   if secim == "1":
       library.kitapekle()
   elif secim == "2":
       library.kitapsil()
   elif secim == "3":
       library.kitaplistele()
   elif secim == "4":
       print("Program kapatılıyor...")
       break