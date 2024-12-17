def count_and_list_odd_digits(number, odd_digits=None):
    # Inicijalizacija liste za neparne cifre prilikom prvog poziva
    if odd_digits is None:
        odd_digits = []

    # Konvertuj broj u pozitivan ako je negativan
    number = abs(number)

    # Bazni slučaj: ako je broj 0, vrati rezultat
    if number == 0:
        return len(odd_digits), odd_digits

    # Provjeri da li je poslednja cifra neparna
    last_digit = number % 10
    if last_digit % 2 != 0:
        odd_digits.append(last_digit)

    # Rekurzivni poziv za ostatak broja
    return count_and_list_odd_digits(number // 10, odd_digits)

# Testiranje funkcije
number = -1234567
count, odd_list = count_and_list_odd_digits(number)
print(f"Broj neparnih cifara u broju {number} je: {count}")
print(f"Neparne cifre su: {odd_list}")
