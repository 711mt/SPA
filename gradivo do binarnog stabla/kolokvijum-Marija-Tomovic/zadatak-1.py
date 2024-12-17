#Zadatak 1 - Rekurzija

# a)
def provjera(S,P):
    if len(S)==1 and S[0] in P:
        return True
    elif len(S)==1 and S[0] not in P:
        return False
    else:
        if S[0] in P:
            return True * provjera(S[1:],P)
        else:
            return False
# funkcija koja ce da umesto true vrati Da, i umesto false da vrati false   
def provjera_print(S,P):
    if provjera(S,P):
        print("Da")
    else:
        print("Ne")
        
S="Mra"
P="Marija"
provjera_print(S,P) #vraca nam da, jer se karakteri Mra nalaze u P
S1="Mil"
P1="Likovno"
provjera_print(S1,P1) #vraca nam ne, jer se karakteri Mil ne nalaze u P1


# b)
def nadji_grad_sa_max_temp_raz(par, max_raz_grad=None, max_raz=0):
    if not par:
        return max_raz_grad

    grad, min_temp, max_temp = par[0]

    if min_temp >= 0:
        raz = max_temp - min_temp 
        if raz > max_raz:
            max_raz = raz
            max_raz_grad = grad 

    return nadji_grad_sa_max_temp_raz(par[1:], max_raz_grad, max_raz)

gradovi_temperature = [
    ("Podgorica", 10, 35),
    ("Pljevlja", -5, 20),
    ("Becice", 15, 40),
    ("Niksic", 0, 25)
]

result = nadji_grad_sa_max_temp_raz(gradovi_temperature)
print("Grad sa najvećom razlikom u temperaturama je:", result)

