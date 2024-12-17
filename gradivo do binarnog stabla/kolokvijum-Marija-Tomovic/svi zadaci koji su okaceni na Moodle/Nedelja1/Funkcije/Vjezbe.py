#1
"""def update(a,x):
    for i in range(len(a)):
        if a[i]%2==0:
            a[i]+=x
    return a

lista=[4,6,9,14,7]

print(update(lista,4))
"""
#2
"""def dodaj_proizvode(n):
    lista_proizvoda=[]

    for i in range(n):
        naziv=input("Unesi naziv")
        opis= input ("Unesi opis ")
        cijena=float(input("Unesi cijenu"))
        broj_artikala= int(input("Unesi broj artikala"))
        lista_proizvoda.append({"naziv":naziv,"opis":opis,"cijena":cijena,"broj_artikala":broj_artikala})

    return lista_proizvoda

proizvodi=dodaj_proizvode(2)
def pretraga_proizvoda(proizvodi,termin_pretrage):
    nadjeni_proizvodi=[]
    for proizvod in proizvodi:
        if proizvod["naziv"].startswith(termin_pretrage):
            nadjeni_proizvodi.append(proizvod)

    return nadjeni_proizvodi

print(pretraga_proizvoda(proizvodi,"M"))"""



#3
"""def drugi_najveci(lista):
    lista2=list(set(lista))
    lista2.sort()
    return lista2[-2]


lista=[14,22,22,19,4,9,7]
print(drugi_najveci(lista))"""


#3

"""def drugi_najveci1(lista):
    najveci=0
    drugi_najveci=0

    for i in lista:
        if i>najveci:
            najveci=i
    lista.remove(najveci)
    for j in lista:
          if j>drugi_najveci:
              drugi_najveci=j

    return drugi_najveci
lista =[1,4,5,7,14,17,11,42,49,44,96]
print(drugi_najveci1(lista))"""

#4
"""def filter(igrice):
    filtriraneigrice=[]
    x=float(input("Unesi zeljenu ocjenu"))
    y= input("Unesi zeljenog izdavaca")
    for igrica in igrice:
        ime,izdavac,godina,ocjena=igrica

        if izdavac==y and ocjena>x:
            filtriraneigrice.append(igrica)
    return filtriraneigrice


igrice= [("Igrac1","Student",2014,8.5),
         ("Igrac2","Nela",2014,7.5),
         ("Igrac3","Student",2014,9.5),
         ("Igrac4","In Copy",2014,9.5)]

print(filter(igrice))"""

#5
"""def dodaj_proizvode(n):
    lista_proizvoda=[]

    for i in range(n):
        naziv=input("Unesi naziv")
        opis= input ("Unesi opis ")
        cijena=float(input("Unesi cijenu"))
        broj_artikala= int(input("Unesi broj artikala"))
        lista_proizvoda.append({"naziv":naziv,"opis":opis,"cijena":cijena,"broj_artikala":broj_artikala})

    return lista_proizvoda

proizvodi=dodaj_proizvode(2)

def koliko_mogu_kupiti(proizvodi, naziv, raspolozivi_novac):
    for proizvod in proizvodi:
        if proizvod['naziv'] == naziv:
            max_mogucih_kupovina = int(raspolozivi_novac / proizvod['cijena'])
            if max_mogucih_kupovina > proizvod['broj_artikala']:
                return proizvod['broj_artikala']
            else:
                return max_mogucih_kupovina
    return 0  


print(koliko_mogu_kupiti(proizvodi,"Sapun",100))"""
#6
"""def prisustvo(studenti):
    lista=[]
    for student in studenti:
        ukupno_prisustvo=student["prisutan"]+student["odustan"]
        prisustvo=student["prisutan"]/ukupno_prisustvo
        if prisustvo>=0.75:
             lista.append((student["ime"],round(prisustvo,2)))
    return lista




studenti=[{"ime":"Marko Markovic","prisutan":10,"odustan":2},
{"ime":"Milos Milosevic","prisutan":8,"odustan":4},
{"ime":"Marija Cetkovic","prisutan":6,"odustan":6},
{"ime":"Nikola Milivojevic","prisutan":2,"odustan":10},
{"ime":"Marijana Minic","prisutan":11,"odustan":1}]

print(prisustvo(studenti))"""