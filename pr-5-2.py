komsuIller=['Kırıkkale','Kırşehir','Nevşehir','Kayseri','Sivas','Tokat',
            'Amasya','Çorum']
print('Yozgat ilinin komşularını öğrenelim')
girilen=input('İlk harfi büyük giriniz:')

if girilen in komsuIller:
    print('Tebrikler!..Bildin') 
else:
    print('Bilemedin')
