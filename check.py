import os
print("\033[94m")
print('''
    _ _ _      _          _               _    
  (_|_) | ___| |_    ___| |__   ___  ___| | __
  | | | |/ _ \ __|  / __| '_ \ / _ \/ __| |/ /
  | | | |  __/ |_  | (__| | | |  __/ (__|   < 
 _/ |_|_|\___|\__|  \___|_| |_|\___|\___|_|\_\
|__/                                          
	        	
           jilet check hoşgeldin sadece adsoyad vardır (şuanlık) .D
            
           

''')
asistansecenek = input("isim soyisim ve şehir girin! ")

if(asistansecenek=="1"):
	dosya = input("Dosya yolu belirtiniz > ")
	hedef = input("Hedef yolu belirtiniz >")
	os.system("cp "+dosya+" "+hedef)

elif(asistansecenek=="2"):
	dosya = input("Dizin adı girin > ")
	os.system("mkdir "+dosya)
elif(asistansecenek=="3"):
	dosya = input("Dosya yolu belirtiniz > ")
	os.system("rm -rf "+dosya)
elif(asistansecenek=="4"):
	dosya = input("Dosya yolu belirtiniz > ")
	hedef = input("Hedef yolu belirtiniz >")
	os.system("mv "+dosya+" "+hedef)
elif(asistansecenek=="5"):
	dosya = input("Uzantısı ile beraber dosya adı girin > ")
	os.system("touch "+dosya)
elif(asistansecenek=="6"):
	dosya = input("Dosya yolu belirtiniz > ")
	os.system("cat "+dosya)
elif(asistansecenek=="7"):
	os.system("apt install zip unzip")
	print(''' 

1-) sülale tc

2-) Sıkıştırılmış Dosyayı Çıkar

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
	print("Kendisi	23615109388	BÜŞRA	YILGIN	4.3.2006	MUTEBER	28106513972	MEHMET	28202510752	YOZGAT	SORGUN	deus@efe:~#
Kardeşi	28076514924	FATİH	YILGIN	20.3.1993	MUTEBER	28106513972	MEHMET	28202510752	YOZGAT	SORGUN	deus@efe:~#
Kardeşi	56170693580	AZRA	YILGIN	15.7.2013	MUTEBER	28106513972	MEHMET	28202510752	YOZGAT	SORGUN	deus@efe:~#
Kardeşi	28052515716	DİLARA	ALTUNOK	27.11.1998	MUTEBER	28106513972	MEHMET	28202510752	YOZGAT	SORGUN	deus@efe:~#
Babası	28202510752	MEHMET	YILGIN	1.1.1976	NAZİK	28265508680	DURSUN	28280508160	YOZGAT	SORGUN	deus@efe:~#
Halası/Amcası	28109513818	HAYDAR	YILGIN	15.10.1992	ADALET	28115513680	DURSUN	28280508160	İSTANBUL	SULTANBEYLİ	deus@efe:~#
Halası/Amcası	30614431136	FADİME	YÜCE	10.7.1978	NAZİK	28265508680	DURSUN	28280508160	İSTANBUL	MALTEPE	deus@efe:~#
Kuzeni	23741660470	ESRA	YÜCE	21.7.2002	FADİME	30614431136	ADİL	30761426290	İSTANBUL	MALTEPE	deus@efe:~#
Kuzeni	30560432980	MUSTAFA	YÜCE	20.2.1998	FADİME	30614431136	ADİL	30761426290	İSTANBUL	MALTEPE	deus@efe:~#
Halası/Amcası	28139512898	ARİFE	KARAHAN	1.10.1984	NAZİK	28265508680	DURSUN	28280508160	YOZGAT	SORGUN	deus@efe:~#
Kuzeni	69436137346	CEMİLE	KARAHAN	4.8.2004	ARİFE	28139512898	MURAT	23891654480	YOZGAT	SORGUN	deus@efe:~#
Kuzeni	21662729702	MUHAMMET MAHMUT	KARAHAN	23.11.2001	ARİFE	28139512898	MURAT	23891654480	YOZGAT	SORGUN	deus@efe:~#
Kuzeni	22007719648	HATİCE ZEHRA	KARAHAN	19.4.2012	ARİFE	28139512898	MURAT	23891654480	YOZGAT	SORGUN	deus@efe:~#
Halası/Amcası	28094514340	SALİH	YILGIN	22.12.1994	ADALET	28115513680	DURSUN	28280508160	YOZGAT	SORGUN	deus@efe:~#
Kuzeni	12393039932	DURSUN EFE	YILGIN	10.10.2016	YARA	99130928292	SALİH	28094514340	YOZGAT	SORGUN	deus@efe:~#
Halası/Amcası	28112513744	ÖZLEM	ÖZ	15.10.1990	ADALET	28115513680	DURSUN	28280508160	null	null	deus@efe:~#
Kuzeni	70270216128	AMİNE HİRANUR	ÖZ	27.1.2015	ÖZLEM	28112513744	MUHAMMED UĞUR	15778434582	İSTANBUL	ESENYURT	deus@efe:~#
Kuzeni	40960502466	DUYGU	DOĞANALP	10.8.2008	ÖZLEM	28112513744	ZEKERİYA	59839456144	null	null	deus@efe:~#
Kuzeni	42346482744	RANA	ÖZ	14.12.2018	ÖZLEM	28112513744	MUHAMMED UĞUR	15778434582	null	null	deus@efe:~#
Kuzeni	22069217762	MUHAMMED UVEYS	ÖZ	25.8.2012	ÖZLEM	28112513744	MUHAMMED UĞUR	15778434582	İSTANBUL	ESENYURT	deus@efe:~#
Halası/Amcası	31466402770	ZEYNEP	GÜGÜL	31.12.1976	NAZİK	28265508680	DURSUN	28280508160	İSTANBUL	SULTANGAZİ	deus@efe:~#
Kuzeni	10212111852	ESRA	GÜGÜL	15.12.2004	ZEYNEP	31466402770	MURAT	31475402488	İSTANBUL	SULTANGAZİ	deus@efe:~#
Kuzeni	41540067108	GÜLAY	GÜRAN	8.1.2000	ZEYNEP	31466402770	MURAT	31475402488	YOZGAT	SORGUN	deus@efe:~#
Kuzeni	11016086148	DÖNDÜ	GÜGÜL	2.10.2006	ZEYNEP	31466402770	MURAT	31475402488	İSTANBUL	SULTANGAZİ	deus@efe:~#
Kuzeni	36149348840	FATMA	GÜGÜL	22.3.2012	ZEYNEP	31466402770	MURAT	31475402488	İSTANBUL	SULTANGAZİ	deus@efe:~#
Kuzeni	41543067044	HATİCE	KANAR	6.6.1998	ZEYNEP	31466402770	MURAT	31475402488	İSTANBUL	SULTANGAZİ	deus@efe:~#
Halası/Amcası	28136512952	HATİCE	GÜRGÖZ	4.12.1988	NAZİK	28265508680	DURSUN	28280508160	İSTANBUL	MALTEPE	deus@efe:~#
Kuzeni	10707095032	BERAT	ŞAHİN	29.9.2005	HATİCE	28136512952	RAGIP	51649729418	YOZGAT	SORGUN	deus@efe:~#
Kuzeni	28348959996	BATUHAN	GÜRGÖZ	1.6.2013	HATİCE	28136512952	NUREDDİN	37306276846	İSTANBUL	MALTEPE	deus@efe:~#
Kuzeni	11307075622	BENGÜSU	ŞAHİN	24.6.2007	HATİCE	28136512952	RAGIP	51649729418	YOZGAT	SORGUN	deus@efe:~#
Büyük Babası	28280508160	DURSUN	YILGIN	25.1.1948	ZEYNEP	28283508006	SALİH	28304507346	YOZGAT	SORGUN	deus@efe:~#
Büyük Babası	28304507346	SALİH	YILGIN	1.3.1917	RUKKİYE	28301507400	MEHMET	28343506034	null	null	deus@efe:~#
Annesi	28106513972	MUTEBER	YILGIN	5.6.1976	CEMİLE	23921653438	BEKİR	23930653146	YOZGAT	SORGUN	deus@efe:~#
Teyzesi/Dayısı	23888654554	GÜLHANIM	ALPARSLAN	26.10.1981	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	EYÜPSULTAN	deus@efe:~#
Teyzesi/Dayısı	23900654166	HAYDAR	KARAHAN	1.2.1970	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	GAZİOSMANPAŞA	deus@efe:~#
Teyzesi/Dayısı	29564465360	DÖNE	TEMUR	2.2.1968	CEMİLE	23921653438	BEKİR	23930653146	YOZGAT	SORGUN	deus@efe:~#
Teyzesi/Dayısı	23006683930	MELEK	UGUZ	3.1.1956	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	EYÜPSULTAN	deus@efe:~#
Teyzesi/Dayısı	23879654846	SAİT	KARAHAN	2.1.1987	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	GAZİOSMANPAŞA	deus@efe:~#
Teyzesi/Dayısı	23915653666	PENBE	KARAHAN	15.1.1960	CEMİLE	23921653438	BEKİR	23930653146	YOZGAT	SORGUN	deus@efe:~#
Teyzesi/Dayısı	28166511932	KUDRET	YILGIN	5.3.1969	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	EYÜPSULTAN	deus@efe:~#
Teyzesi/Dayısı	67249209144	ZELİHA	ARISOY	1.1.1964	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	GAZİOSMANPAŞA	deus@efe:~#
Teyzesi/Dayısı	23471668456	ZAHİDE	KABLAN	1.8.1966	CEMİLE	23921653438	BEKİR	23930653146	İSTANBUL	GAZİOSMANPAŞA	deus@efe:~#
Teyzesi/Dayısı	22070715172	SULTAN	KARAARSLAN	31.7.1974	CEMİLE	23921653438	BEKİR	23930653146	KONYA	SELÇUKLU	deus@efe:~#
Teyzesi/Dayısı	23891654480	MURAT	KARAHAN	2.1.1980	CEMİLE	23921653438	BEKİR)
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
