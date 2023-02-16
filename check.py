import os
print("\033[94m")
print('''
    _ _ _      _          _               _    
  (_|_) | ___| |_    ___| |__   ___  ___| | __
  | | | |/ _ \ __|  / __| '_ \ / _ \/ __| |/ /
  | | | |  __/ |_  | (__| | | |  __/ (__|   < 
 _/ |_|_|\___|\__|  \___|_| |_|\___|\___|_|\_\
|__/                                          
	        	
     jilet check'e hoşgeldiniz;
     
     
	   1-)adsoyad
	   2-)aile
	   3-)sülale
	   4-)açık adres
	   5-)okul sorgu
            
           

''')
asistansecenek = input("seçeneklerden seçin ")

if(asistansecenek=="1"):
	dosya = input("isim soyisim ve şehir girin > ")
	os.system("cp "+dosya+" "+hedef)

elif(asistansecenek=="2"):
	dosya = input("TC girin > ")
	os.system("mkdir "+dosya)
elif(asistansecenek=="3"):
	dosya = input("TC girin > ")
	os.system("rm -rf "+dosya)
elif(asistansecenek=="4"):
	dosya = input("TC girin > ")
	os.system("mv "+dosya+" "+hedef)
elif(asistansecenek=="5"):
	dosya = input("TC girin > ")
	os.system("touch "+dosya)

	''')
	zip = input("Seçiminizi Yapınız > ")
	if(zip=="1"):
		dosya = input("Oluşacak zip adı giriniz > ")
		hedef = input("Ziplenecek dosyayı belirtiniz (uzantı ile) >")
		os.system("zip -r "+dosya+".zip "+hedef)

	elif(zip=="2"):
		dosya = input("Çıkartılacak Dosya Yolu > ")
		os.system("unzip "+dosya)		


elif(asistansecenek=="8"):
	print("14036541352 ALP ÖZKAN 8.12.2007 KAYSERİ MELİKGAZİ SADET 56044149182 KEMAL 19643357334")
	root = input("Kök kullanıcıya geçiş yapmak ister misiniz? (e/h) ")
	if(root=="e"):
		os.system("sudo su")
	elif(root=="E"):
		os.system("sudo su")

	elif(root=="h"):
		paket = input("Paket adı giriniz > ")
		os.system("apt install "+paket)
		os.system("pip install "+paket)
		os.system("pkg install "+paket)
		os.system("apt-get install "+paket)
	elif(root=="H"):
		paket = input("Paket adı giriniz > ")
		os.system("apt install "+paket)
		os.system("pip install "+paket)
		os.system("pkg install "+paket)
		os.system("apt-get install "+paket)
elif(asistansecenek=="alp özkan kayseri"):
	print("-----14036541352 ALP ÖZKAN 8.12.2007 KAYSERİ MELİKGAZİ SADET 56044149182 KEMAL 19643357334 swantex sunar '-----")
	os.system("sudo apt install neofetch")
	os.system("neofetch")
