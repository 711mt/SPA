#rekurzija vezbe
#1. zadatak
#Napisati rekurzivnu funkciju koja sabira prvih N brojeva

def first_n(n):
    if n==1:
        return 1
    else:
        return n + first_n(n-1)
    
print(first_n(5))

#2.zadatak
#Napisati rekurzivnu funkciju koja izracunava faktorijel broja N

def faktorijel(n):
    if n==1:
        return n
    else:
        return n*faktorijel(n-1)
    
print(faktorijel(5))

#3.zadatak
#Napisati rekurzivnu funkciju koja stampa sve elemente liste redom

def stampanje_liste(lista):
    if len(lista)==1:
        return lista[0]
    else:
        print(lista[0])
        return stampanje_liste(lista[1:])
    
    
lista1=[1,2,3,4,5]
print(stampanje_liste(lista1))
niz=["Dejan","Marija","Milija",2,3,4]
print(stampanje_liste(niz))

#4.zadatak
#Napisati rekurzivnu funkciju koja stampa string unazad 
#[-1] za string unazad

def string_unazad(string):
    if len(string)==1:
        return string
    else:
        return string[-1] + string_unazad(string[0:len(string)-1])
    
print(string_unazad("Marija"))

#5.zadatak
#Napisati rekurzivnu funkciju koja pronalazi najveci element niza

def najveci_element(niz):
    if len(niz)==1:
        return niz[0]
    else:
        if niz[0]>niz[1]:
            niz.remove(niz[1])
        else:
            niz.remove(niz[0])
        return najveci_element(niz)

arr=[3,4,7,6,4]
print(najveci_element(arr))
    
# 1.Napisati rekurzivnu funkciju koja stampa sve elemente liste obrnutim redosljedom

def obrnuta_lista(lista):
    if len(lista)==1:
        return lista[0]
    else:
        print(lista[-1])
        return obrnuta_lista(lista[0:len(lista)-1])

lista=[1,2,3,4,5]
print(obrnuta_lista(lista))

#2. Napisati rekurzivnu funkciju koja provjerava koliko zadati broj ima parnih cifara
def broj_parnih_cifara(n):
    if n==0:
        return 0
    else:
        poslednja_cifra= n % 10
        if poslednja_cifra % 2 == 0:
            return 1 + broj_parnih_cifara(n//10)
        else:
            return broj_parnih_cifara(n//10)
        
n=123456
print(broj_parnih_cifara(n))

#3. Napisati rekurzivnu funkciju koja proverava je li dati niz znakova palindrom

def palindrom(tekst):
    if len(tekst)==1:
        return True
    else:
        return tekst[0]==tekst[-1] and palindrom(tekst[1:-1])
    #if tekst[0]!=tekst[-1]:
        #return False
   # return palindrom(tekst[1:-1])

tekst = "Radar"
mala_slova=tekst.lower()
print(palindrom(mala_slova))

#4. Napisati rekurzivnu funkciju koja prebrojava koliko se puta odredjeni element pojavljuje u listi

def ponavljanje(b,n):
    if len(b)==1:
        if b[0] == n:
            return 1
        else:
            return 0
    else:
        if b[0] == n:
            return 1 + ponavljanje(b[1:],n)
        else:
            return ponavljanje(b[1:],n)
        
print(ponavljanje([1,2,2,3,2],2))

#5 Napisati rekurzivnu funkciju koja pretvara decimalni broj u binarni oblik

def int_to_binary(number):

  if number == 1:

    return str(number%2)

  else:

    return str(number%2) + int_to_binary(number//2)

  

def float_to_decimal(number):

  if number == 0:

    return str(int((number*2)//1))

  else:

    return str(int((number*2)//1)) + float_to_decimal((number*2)%1)

  

def convert_to_binary(number):

  integer_part = int(number)

  float_part = number - integer_part

  integer_binary = int_to_binary(integer_part)

  if float_part > 0:

    fractional_binary = float_to_decimal(float_part)

    return integer_binary[::-1] + '.' + fractional_binary

  else:

    return integer_binary[::-1]



print(convert_to_binary(37.75))

#napisati rekurzivnu funkciju koja proverava koliko zadati broj ima neparnih cifara
def broj_neparnih_cifara(n):
    if n==0:
        return 0
    else:
        poslednja_cifra= n % 10
        if poslednja_cifra % 2 != 0:
            return 1 + broj_neparnih_cifara(n//10)
        else:
            return broj_neparnih_cifara(n//10)
        
n=123456
print(broj_neparnih_cifara(n))

#petlja 
# Unesi broj koji želiš da proveriš
broj = int(input("Unesi broj: "))

# Pretvori broj u string da bi mogao iterirati kroz cifre
broj_str = str(broj)

# Inicijalizuj brojač za neparne cifre
brojac_neparnih = 0

# Prođi kroz svaku cifru u broju
for cifra in broj_str:
    # Pretvori cifru nazad u broj
    cifra = int(cifra)
    # Proveri da li je cifra neparna
    if cifra % 2 != 0:
        brojac_neparnih += 1

# Prikaži rezultat
print("Broj neparnih cifara:", brojac_neparnih)

#napisati rekurzivnu funkciju koja racuna Fibonacijev broj
def fib(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

print(fib(5))

#napisati rekurzivnu funkcija koliko niz ima negativnih parnih brojeva
def neg_parni(niz):
    if len(niz)==0:
        return 0
    else:
        prvi_element=niz[0]
        if prvi_element<0 and prvi_element%2==0:
            return 1 + neg_parni(niz[1:])
        else:
            return neg_parni(niz[1:])

#1 Napisati rekurzivnu funkciju koja stepenuje broj X
def stepenovanje(x,n):
    if n==0:
        return 1
    elif x==1:
        return 1
    elif x==0:
        return 0
    else:
        return x * stepenovanje(x,n-1)

broj=stepenovanje(10,2)
print(broj)

#2 Napisati rekurzivnu funkciju koja prima pozitivan cijeli broj i vraca sumu njegovih cifara

def suma_cifara(broj):
    if broj //10 ==0:
        return broj
    else:
        return broj % 10 + suma_cifara(broj//10)

print(suma_cifara(123))


#3 Napisati rekurzivnu funkciju koja broji koliko puta se odredjeno slovo/karakter pojavljuje u zadatom stringu

def ponavljanje(n,string):
    if len(string)==0:
        return 0
    elif n==string[0]:
        return 1+ponavljanje(n,string[1:])
    else:
        return ponavljanje(n,string[1:])

print(ponavljanje("2","12342"))

#4 Napisati rekurzivnu funkciju koja prima dva broja, a i b, i vraca zbir svih cijelih brojeva izmedju njih
# ukljucujuci i a i b. Pretpostaviti da je a uvijek manje od b
def count(a,b):
    if a==b:
        return a
    else:
        return b+count(a,b-1)
    
print(count(5,7))
        
#prebrojavanje cifara nekog broja

def prebrojavanje(n):
    if n <= 1:
        return n
    else:
        return 1 + prebrojavanje(n//10)
    
print(prebrojavanje(5505))

#rekurzivna funkcija koja vraca proizvod cifara zadatog broja n

def proizvod_cif(n):
    if n == 0:
        return 1
    else:
        return (n%10) * proizvod_cif(n//10)

print(proizvod_cif(5213))
        
#rekurzivna funkcija koja vraca prvo veliko slovo u stringu 10

def prvo_veliko_slovo(string,i):
    if i==len(string)-1:
        if str(string[i]).isupper():
           return string[i]
    else:
        if str(string[i]).isupper():
            return string[i]
        else:
            return prvo_veliko_slovo(string,i+1)
        
print(prvo_veliko_slovo("AsB",0))

#Napisati rekurzivnu funkciju koja racuna x gdje su x i n prirodni brojevi n
#Napisati rekurzivnu funkciju koja vraća poslednje veliko slovo zadatog stringa. Input: “Neka Ulazna Recenica”
#Output "R"
def poslednje_veliko_slovo(slovo,recenica,i):
    if i == len(recenica):
        if slovo:
            return slovo
        else:
            return 'Nema velikih slova'
    else:
        if recenica[i].isupper():
            slovo = recenica[i]
            return poslednje_veliko_slovo(slovo,recenica,i+1)
        else:
            return poslednje_veliko_slovo(slovo,recenica,i+1)
        
print(poslednje_veliko_slovo('',"marija polako sve je okej",0))

#Napisati rekurzivnu funkciju sa dva parametra koja vraća stepenovan
#broj x. Parametri su broj koji se stepenuje i stepen
#Input: (3, 3) Output: 27
def stepenovan_broj(broj, broj_ponavljanja):
    if broj_ponavljanja==1:
        return broj
    else:
        return broj*(stepenovan_broj(broj,broj_ponavljanja-1))

print(stepenovan_broj(5,2))


#Napisati rekurzivnu funkciju koja računa koliko niz/lista ima negativnih
#brojeva koji su djeljivi sa 2.

def neg_parni(niz):
    if len(niz)==0:
        return 0
    else:
        prvi_element=niz[0]
        if prvi_element<0 and prvi_element%2==0:
            return 1 + neg_parni(niz[1:])
        else:
            return neg_parni(niz[1:])

#Napisati rekurzivnu funkciju koja provjerava da li su sve cifre zadatog
#broja m djelioci broja n. Brojevi m i n su prirodni brojevi

def provera(m,n,result):
    if m == 0:
        return result
    else:
        zadnja_cifra  = m%10 
        if n%zadnja_cifra == 0:
            result = True
            return provera(m//10,n,result)
        else:
            result = False
            return provera(m//10,n,result)

        
print(provera(217,17,False))

#Kule Hanoja
#pomoćna funkcija koja štampa informaciju
def stampaj_korak(polazni, dolazni):   
    #sa kog štapa na koji štap se prebacio disk
    print ("Pomeri sa " + str(polazni) + " na " + str(dolazni)) 

#f-ja Kule za argumente uzima broj diskova i nazive štapova
def Kule(n, polazni, dolazni, pomocni):	
    if n == 1:	#bazni slučaj. Ako postoji samo jedan disk, izvršiti prebacivanje
        stampaj_korak(polazni, dolazni)
    else:		#rekurzivni korak
	#prvo se prebacuje n-1 diskova sa polaznog na pomoćni štap
        Kule(n-1, polazni, pomocni, dolazni)
	#najveći disk se prebaci sa polaznog na dolazni štap
        Kule(1, polazni, dolazni, pomocni)	 
	#na kraju, n-1 diskova se prebacuje sa pomoćnog na dolazni štap
        Kule(n-1, pomocni, dolazni, polazni)  

Kule(3, "A", "C", "B")

#napraviti rekurzivnu funkciju koja ima dva argumenta,prvi argument broj, drugi broj ponavljanja
#treba napraviti novi broj od prvog argumenta
#pr. kreiraj_broj(12,16) ==> 12121212121212121212...

def kreiraj_broj(broj,broj_ponavljanja,result):
    if broj_ponavljanja==0:
        return result
    else:
        result += str(broj)
        return kreiraj_broj(broj,broj_ponavljanja-1,result)

print(kreiraj_broj(12,2,''))

#1 Napisati rekurzivnu funkciju koja proverava koliko broj ima parnih cifara
def broj_parnih_cifara(n):
    if n==0: #ako stavimo da je n==1, rekurzija se ne bi nikad zavrsila
        return 0
    else:
        poslednja_cifra= n % 10
        if poslednja_cifra % 2 == 0:
            return 1 + broj_parnih_cifara(n//10)
        else:
            return broj_parnih_cifara(n//10)
        
n=123456
print(broj_parnih_cifara(n))

#2 Dobili smo zahtjev od tima koji organizuje takmicenje iz programiranja. Organizatori su nam dostavili broj bodova 
#za svakog ucesnika i poslali uvid da mozemo proveriti koliko je bilo ucenika sa negativnom ocenom
#Za implementaciju rjesenja, koristiti rekurzivnu funkciju

def broj_bodova(lista):
    if len(lista)==0:
        return 0
    else:
        if lista[0]<0:
            return 1+broj_bodova(lista[1:])
        else:
            return broj_bodova(lista[1:])

print(broj_bodova([-10,22,39,-3])) # output 2

#Koliko string ima cifara? Iz zadatog stringa(karaktera i cifara) izdvojiti cifre
def string_cifre(s):
    if len(s)==0:
        return ""
    if s[0].isdigit():
        return s[0]+string_cifre(s[1:])
    else:
        return string_cifre(s[1:])
    
print(string_cifre("Ab11C2")) # --> "112"

#napisati rekurzivnu funkciju koja na osnovu zadatog broja i ponavlja na tom broju,kreira novi broj
#f(12,3)---> 12 12 12, br>0
def kreira_broj(broj,ponavljanje):
    if ponavljanje==1:
        return str(broj)
    else:
        return str(broj)+kreira_broj(broj,ponavljanje-1)

print(kreira_broj(12,3))

'''
niz sastavljen od stringova, gdje svaki string predstavlja jednu recenicu. Pronaći onaj element u nizu koji ima najviše velikih slova
'''
def count_uppercase(s):
    if not s:
        return 0
    return (1 if s[0].isupper() else 0) + count_uppercase(s[1:])

def most_upper(recenica, max_recenica="", max_brojac=0):
    if not recenica:
        return max_recenica
    current_recenica = recenica[0]
    current_brojanje = count_uppercase(current_recenica)
    if current_brojanje > max_brojac:
        return most_upper(recenica[1:], current_recenica, current_brojanje)
    else:
        return most_upper(recenica[1:], max_recenica, max_brojac)

# Primjer korištenja
recenica = ["ABc","abC","ABC"]

result = most_upper(recenica)
print("Rečenica s najviše velikih slova je:", result)

#napraviti rekurzivnu funkciju koja ima dva argumenta,prvi argument broj, drugi broj ponavljanja
#treba napraviti novi broj od prvog argumenta
#pr. kreiraj_broj(12,16) ==> 12121212121212121212...

def kreiraj_broj(broj,broj_ponavljanja,result):
    if broj_ponavljanja==0:
        return result
    else:
        result += str(broj)
        return kreiraj_broj(broj,broj_ponavljanja-1,result)

print(kreiraj_broj(12,2,''))

#rekurzivna funkcija za proveru koliko ima velikih slova u zadatom stringu
def pronadji_veliko_slovo(string):
    if len(string)==1:
        if string[0].isUpper():
            return 1
        else:
            return 0
    else:
        if string[0].isUpper():
            return 1+pronadji_veliko_slovo(string[1:])
        else:
            return pronadji_veliko_slovo(string[1:])
        
#zadat je string, iz tog stringa prebrojiti koliko ima jedinica i da to predstavlja binarni broj

def broj_jedinica(string):
    if len(string)==0:
        return 0
    else:
        if string[0]=='1':
            return 1+broj_jedinica(string[1:])
        else:
            return broj_jedinica(string[1:])

#max
def max(niz):
    if len(niz)==1:
        return niz
    else:
        if niz[0] > niz[1]:
            return niz.remove[0]
        else:
            return niz.remove[1]
            return max[niz]
#drugi nacin za max
def nadji_max(niz):
    if len(niz)==0:
        return 0
    else:
        return nadji_max(niz[0], nadji_max(niz[1:]))
    
#
def najveci(broj, maksimum):
    if len(broj)==0:
        return maksimum
    else:
        current=n[0]
        current_count = count(current)
        max_count=count(maksimum)
        if current>max_count:
            maksimum=current (n[1:],maksimum)

#
def count(s):
    if len(s)==0:
        return 0
    else:
        if s[0].isUpper():
            return 1+count(s[1:])
        else:
            return count(s[1:])


################################################
lista = [{"ime":"Marko", "prezime":"Markovic"}, {"ime":"Ivan", "prezime":"Ivanovic"}]
for element in lista:
    print(element["ime"])

# Neka Ulazna R -> R

def poslednje_veliko_slovo(string):
    lista_velikih_slova = []
    for karakter in string:
        if karakter.isupper():
            lista_velikih_slova.append(karakter)
    return lista_velikih_slova[-1]

def poslednje_veliko_slovo_rec(string):
    if len(string) == 0:
        return False
    elif string[-1].isupper():
        print(string[-1])
    else:
        poslednje_veliko_slovo_rec(string[:-1])

#Napisati rekurzivnu fju koja prima dva broja, a i b, i vraca zbir svih cijelih brojeva izmedju
#njih, ukljucujuci i a i b. Pretpostaviti da je a uvijek manje od b.
def count(a, b):
 if a == b:
   return a
 else:
   return b + count(a, b-1)
print(count(5,7))



  


    
            
