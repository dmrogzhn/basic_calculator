import islemler as ism
import islemListele as ismlist


islemler=ismlist.islemler
islemIsmi=ismlist.islemID

print(islemler)
secilenİslem=int(input("Yapmak İstedğiniz İşlemin Numarasını Giriniz..."))
num1=int(input("İşlem Yapmak İstediğiniz İlk Tam Sayıyı Giriniz..."))
num2=int(input("İşlem Yapmak İstediğiniz İkinci Tam Sayıyı Giriniz..."))
secim=islemIsmi[secilenİslem]

result=ism.Islemler(num1,num2)

if(secilenİslem==islemler[secim]):
     result.topla
elif(secilenİslem==islemler[secim]):
     result.cikar
elif(secilenİslem==islemler[secim]):
     result.carp
elif(secilenİslem==islemler[secim]):
     result.bol
else:
    print("Geçerli Değer Giriniz...")


print(result)
#print(secim)