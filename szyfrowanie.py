import re

def klucz_podziel(key):
    key1 = key[0:4] 
    key1 = (key1[1:] + key1[0]) 
    key2 = key[4:8]
    key2 = (key2[1:] + key2[0])
    print("klucz1 " + key1 + "    klucz1 " + key2)
    result_key = key1 + key2
    print("klucz podziel : "+result_key)
    return result_key
    
def Klucz_polacz(key3):
    key3 = (key3[1:] + key3[0])
    print("klucz polacz: " + key3)
    result_key = key3
    return result_key

def klucz_bity(klucz):
    new_text = klucz[0] + klucz[2] + klucz[4] + klucz[6]
    print("klucz_wejsciowy: "+new_text)
    return new_text

def f1(klucz, dane):
    k=bool(int(klucz[0]))
    x1=bool(int(dane[4]))
    x2=bool(int(dane[5]))
    x3=bool(int(dane[6]))
    x4=bool(int(dane[7]))
    wynik=x1 ^ x1 & x3 ^ x2 & x4 ^ x2 & x3 & x4 ^ x1 & x2 & x3 & x4 ^ k
    return wynik

def f2(klucz, dane):
    k=bool(int(klucz[1]))
    x1=bool(int(dane[4]))
    x2=bool(int(dane[5]))
    x3=bool(int(dane[6]))
    x4=bool(int(dane[7]))
    wynik=x2 ^ (x1 & x3) ^ (x1 & x2 & x4) ^ (x1 & x3 & x4) ^ (x1 & x2 & x3 & x4) ^ k
    return wynik

def f3(klucz, dane):
    k=bool(int(klucz[2]))
    x1=bool(int(dane[4]))
    x2=bool(int(dane[5]))
    x3=bool(int(dane[6]))
    x4=bool(int(dane[7]))
    wynik=True ^ x3 ^ (x1 & x4) ^ (x1 & x2 & x4) ^ (x1 & x2 & x3 & x4) ^ k
    return wynik

def f4(klucz, dane):
    k=bool(int(klucz[3]))
    x1=bool(int(dane[4]))
    x2=bool(int(dane[5]))
    x3=bool(int(dane[6]))
    x4=bool(int(dane[7]))
    wynik=True ^ (x1 & x2) ^ (x3 & x4) ^ (x1 & x2 & x4) ^ (x1 & x3 & x4) ^ (x1 & x2 & x3 & x4) ^ k
    return wynik

def magiczna_skrzynka(klucz,dane):
    fun1=f1(klucz,dane)
    print("wynik f1: "+str(fun1)+" bit0: "+str(bool(int(dane[0]))))
    fun2=f2(klucz,dane)
    print("wynik f2: "+str(fun2)+" bit1: "+str(bool(int(dane[1]))))
    fun3=f3(klucz,dane)
    print("wynik f3: "+str(fun3)+" bit2: "+str(bool(int(dane[2]))))
    fun4=f4(klucz,dane)
    print("wynik f4: "+str(fun4)+" bit3: "+str(bool(int(dane[3]))))
    
    bit1=fun1^bool(int(dane[0]))
    bit2=fun2^bool(int(dane[1]))
    bit3=fun3^bool(int(dane[2]))
    bit4=fun4^bool(int(dane[3]))
    strona_lewa=str(int(bit1))+str(int(bit2))+str(int(bit3))+str(int(bit4))
    print("obecnie_lewa: "+strona_lewa)
    strona_prawa=dane[4:8]
    print("obecnie_prawa: "+strona_prawa)
    wynik=strona_prawa + strona_lewa
    print("iteracja: "+wynik)
    return wynik  


#początek programu
print("Program jest implementacja prostego szyfru blokowego\n")
dane = ""
while len(dane)!=8:
    print("Podaj dane, powinien się on składać z samych wartości binarnych i powieny mieć 8 bitów dłuigości:")
    #dane =input("Podaj klucz: ")
    dane="00010010"
    while not re.match("^[0-1 ]*$", dane): #https://stackoverflow.com/questions/89909/how-do-i-verify-that-a-string-only-contains-letters-numbers-underscores-and-da
        print('\nKlucz może składać się tylko z "0" oraz "1"')
        dane =input("Podaj dane: ")       

klucz = ""
while len(klucz)!=8:
    print("Podaj klucz, powinien się on składać z samych wartości binarnych i powienien mieć 8 bitów dłuigości:")
    #klucz =input("Podaj klucz: ")
    klucz="00110100"
    while not re.match("^[0-1 ]*$", klucz): #https://stackoverflow.com/questions/89909/how-do-i-verify-that-a-string-only-contains-letters-numbers-underscores-and-da
        print('\nKlucz może składać się tylko z "0" oraz "1"')
        klucz =input("Podaj klucz: ")
        
print("Klucz: "+klucz)
print("Dane: "+dane)

chomukuj=dane
chomukuj_klucz=klucz
tablica_kluczy=[]

print("\nprzejscie nr1")
kluczobliczenia=klucz_podziel(klucz)
klucz=klucz_bity(kluczobliczenia)
print("wejście "+dane)
wynik=magiczna_skrzynka(klucz,dane)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr2")
kluczobliczenia=Klucz_polacz(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
print("wejście "+wynik)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr3")
kluczobliczenia=klucz_podziel(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr4")
kluczobliczenia=Klucz_polacz(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr5")
kluczobliczenia=klucz_podziel(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr6")
kluczobliczenia=Klucz_polacz(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr7")
kluczobliczenia=klucz_podziel(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

print("\nprzejscie nr8")
kluczobliczenia=Klucz_polacz(kluczobliczenia)
klucz=klucz_bity(kluczobliczenia)
wynik=magiczna_skrzynka(klucz,wynik)
tablica_kluczy.append(kluczobliczenia)

odwrot=wynik[4:8]+wynik[0:4]

print("\nwszystkie klucze: "+str(tablica_kluczy))
print("wynik końcowy: "+ odwrot+" a klucz to: "+kluczobliczenia)


print("\n \n deszyfracja")

print("\nprzejscie nr1")
klucz=klucz_bity(tablica_kluczy[7])
print("wejście "+wynik)
wynik=magiczna_skrzynka(klucz,odwrot)

print("\nprzejscie nr2")
klucz=klucz_bity(tablica_kluczy[6])
print("wejście "+wynik)
wynik=magiczna_skrzynka(klucz,wynik)


print("\nprzejscie nr3")
klucz=klucz_bity(tablica_kluczy[5])
wynik=magiczna_skrzynka(klucz,wynik)


print("\nprzejscie nr4")
klucz=klucz_bity(tablica_kluczy[4])
wynik=magiczna_skrzynka(klucz,wynik)


print("\nprzejscie nr5")
klucz=klucz_bity(tablica_kluczy[3])
wynik=magiczna_skrzynka(klucz,wynik)


print("\nprzejscie nr6")
klucz=klucz_bity(tablica_kluczy[2])
wynik=magiczna_skrzynka(klucz,wynik)


print("\nprzejscie nr7")
klucz=klucz_bity(tablica_kluczy[1])
wynik=magiczna_skrzynka(klucz,wynik)


print("\nprzejscie nr8")
klucz=klucz_bity(tablica_kluczy[0])
wynik=magiczna_skrzynka(klucz,wynik)

odwrot=wynik[4:8]+wynik[0:4]

print("\n Powinno być "+ chomukuj + " klucz "+chomukuj_klucz)
print(" wynik:      "+odwrot)
input('Nacisnij enter aby zakończyć')