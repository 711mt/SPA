#Zadatak 1
#Pod a)
def proveri(S,P):
    if len(S)==1 and S[0] in P:
        return True
    elif len(S)==1 and S[0] not in P:
        return False
    else:
        if S[0] in P:
            return True * proveri(S[1:],P)
        else:
            return False
        
def check_print(S,P):
    if proveri(S,P):
        print("Da")
    else:
        print("Ne")
        
S="Bsr"
P="Balsa"
check_print(S,P)
#Pod b)
