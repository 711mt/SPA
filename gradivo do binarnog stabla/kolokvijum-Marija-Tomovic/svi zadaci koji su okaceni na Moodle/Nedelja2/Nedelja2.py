#1
"""def print_elements_vv(lista):
  if (len(lista)==0):
    return None
  else:
    print(lista[-1])
    return print_elements_vv(lista[0:len(lista)-1])
  
lista = [1,2,3,4,5,51,6,7]
print_elements_vv(lista)"""


#2
"""def check_num(number):
  if(number<10):
    if (number%2==0):
      return 1
    else:
      return 0
  else:
    if(number%10%2==0):
      return 1 + check_num(number//10)
    else:
      return 0 + check_num(number//10)
print(check_num(12348564798))"""





#3
"""def je_palindrom(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and je_palindrom(s[1:-1])


print(je_palindrom("anavolimilovana")) """



#4
"""def broj_pojavljivanja(lista, element):
    if not lista:
        return 0
    else:
        count = 1 if lista[0] == element else 0
        return count + broj_pojavljivanja(lista[1:], element)


lista = [1, 2,2,2, 3, 2, 4, 2, 5]
print(broj_pojavljivanja(lista, 5)) """


#5
"""def decimal_u_binarni(n):
    if n == 0:
        return ''
    else:
        return decimal_u_binarni(n // 2) + str(n % 2)


n = 55
binarni = decimal_u_binarni(n)
print(binarni or '0') """

#6
