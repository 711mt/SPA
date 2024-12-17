#Nalazimo se u gornjem lijevom uglu mreže dimenzija nxm. Možemo se kretati samo desno ili dolje. 
#Napisati rekurzivnu funkciju koja računa ukupan broj mogućih puteva do donjeg desnog ugla mreže
#Ulaz: dimenzije mreže nxm, npr.(3,3)
#Izlaz: ukupan broj mogućih puteva do krajnje tačke. Za primer (3,3), rezultat bi bio 6
#Detalji zadatka(bitno za rekurziju, jer govori o uslovima):
# Ako smo na početnoj poziciji(0,0), možemo se kretati samo desno ili dolje
#Ako smo došli do kraja bilo koje ivice mreže(n=0 ili m=0), postoji samo jedan put, jer možemo ići samo u jednom smeru
#Funkcija treba da računa broj mogućih puteca sa donje i desne strane

def broj_puteva(n, m):
    # bazni slucaj rekurzije
    if n == 1 or m == 1: #ne radi mi da je uslov n == 0 or m == 0,jer mi output bude 20, sto nije bio cilj ovog zadatka, pa sam izmenila uslove
        return 1
    else:
        return broj_puteva(n - 1, m) + broj_puteva(n, m - 1)

n = 3
m = 3
print(broj_puteva(n, m)) 

#ovo je slicno kao i sa Fibonnacijevim nizom
