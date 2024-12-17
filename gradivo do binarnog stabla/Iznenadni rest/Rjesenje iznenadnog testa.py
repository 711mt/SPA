def broj_puteva(n, m):
    # Ako smo stigli do ivice mreže (n = 0 ili m = 0), postoji samo jedan put (sve pravo)
    if n == 1 or m == 1:
        return 1
    # Rekurzivno računamo broj puteva kao zbir puteva iz desnog i donjeg pravca
    return broj_puteva(n-1, m) + broj_puteva(n, m-1)

# Testiranje funkcije za mrežu 3x3
n = 3
m = 3
print(f"Broj mogućih puteva za mrežu {n}x{m}: {broj_puteva(n, m)}")


#2

# Definisanje čvora koji predstavlja knjigu
"""class BookNode:
    def __init__(self, name, author, year, rating, genre, pages):
        # Svaki čvor sadrži podatke o knjizi
        self.book = {
            'name': name,       # Naziv knjige
            'author': author,   # Autor knjige
            'year': year,       # Godina izdavanja
            'rating': rating,   # Ocjena knjige
            'genre': genre,     # Žanr knjige
            'pages': pages      # Broj stranica knjige
        }
        self.prev = None  # Pokazivač na prethodni čvor (knjigu)
        self.next = None  # Pokazivač na sljedeći čvor (knjigu)

# Definisanje klase za dvostruko olancanu listu
class DoublyLinkedListBooks:
    def __init__(self):
        self.head = None  # Glava liste
        self.tail = None  # Rep liste

    # Funkcija za dodavanje knjige na kraj liste
    def append(self, new_book):
        if not self.head:
            self.head = new_book  # Ako je lista prazna, nova knjiga postaje glava i rep
            self.tail = new_book
        else:
            self.tail.next = new_book  # Dodavanje nove knjige na kraj liste
            new_book.prev = self.tail  # Postavljanje pokazivača ka prethodnoj knjizi
            self.tail = new_book       # Nova knjiga postaje novi rep

    # Funkcija koja računa prosječnu ocjenu svih knjiga iz zadate godine
    def avg_rating_by_year(self, year):
        current = self.head
        total_rating = 0
        count = 0
        while current:
            if current.book['year'] == year:  # Provjera da li je godina izdavanja zadana
                total_rating += current.book['rating']  # Sabiranje ocjena
                count += 1
            current = current.next
        return total_rating / count if count > 0 else None  # Vraćanje prosjeka

    # Funkcija koja ispisuje sve knjige čija je godina izdavanja veća ili jednaka zadatoj godini
    def print_books_after_year(self, year):
        current = self.head
        while current:
            if current.book['year'] >= year:
                print(current.book)
            current = current.next

    # Funkcija za brojanje knjiga određenog žanra
    def count_books_by_genre(self, genre):
        current = self.head
        count = 0
        while current:
            if current.book['genre'].lower() == genre.lower():
                count += 1
            current = current.next
        return count

    # Funkcija za brisanje knjige iz liste na osnovu naziva
    def delete_book_by_name(self, name):
        current = self.head
        while current:
            if current.book['name'].lower() == name.lower():
                if current == self.head:
                    self.head = current.next  # Ažuriranje glave
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev  # Ažuriranje repa
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next  # Ažuriranje pokazivača između čvorova
                    if current.next:
                        current.next.prev = current.prev
                return True  # Vraća True nakon brisanja
            current = current.next
        return False  # Ako knjiga nije pronađena, vraća False

    # Funkcija za ažuriranje ocjene knjige na osnovu naziva
    def update_book_rating(self, name, new_rating):
        current = self.head
        while current:
            if current.book['name'].lower() == name.lower():
                current.book['rating'] = new_rating
                return True
            current = current.next
        return False  # Ako knjiga nije pronađena, vraća False

    # Funkcija koja pronalazi i ispisuje sve knjige određenog autora
    def print_books_by_author(self, author):
        current = self.head
        while current:
            if current.book['author'].lower() == author.lower():
                print(current.book)
            current = current.next

    # Funkcija koja ispisuje sve knjige koje imaju više od zadatog broja stranica
    def print_books_by_pages(self, min_pages):
        current = self.head
        while current:
            if current.book['pages'] > min_pages:
                print(current.book)
            current = current.next


# Testiranje funkcionalnosti

# Kreiranje čvorova za knjige
book1 = BookNode("The Great Gatsby", "F. Scott Fitzgerald", 1925, 8.5, "Drama", 180)
book2 = BookNode("1984", "George Orwell", 1949, 9.0, "Dystopia", 328)
book3 = BookNode("To Kill a Mockingbird", "Harper Lee", 1960, 9.2, "Fiction", 281)
book4 = BookNode("Moby Dick", "Herman Melville", 1851, 7.5, "Adventure", 635)
book5 = BookNode("The Catcher in the Rye", "J.D. Salinger", 1951, 8.0, "Fiction", 214)

# Kreiranje dvostruko olancane liste i dodavanje knjiga
book_list = DoublyLinkedListBooks()
book_list.append(book1)
book_list.append(book2)
book_list.append(book3)
book_list.append(book4)
book_list.append(book5)

# 1. Računanje prosječne ocjene svih knjiga iz 1951. godine
print("Prosječna ocjena knjiga iz 1951. godine:", book_list.avg_rating_by_year(1951))

# 2. Ispis svih knjiga koje su izdane nakon 1900. godine
print("Knjige izdane nakon 1900. godine:")
book_list.print_books_after_year(1900)

# 3. Brojanje knjiga određenog žanra (npr. Fiction)
print("Broj knjiga u žanru 'Fiction':", book_list.count_books_by_genre('Fiction'))

# 4. Brisanje knjige iz liste na osnovu naziva ("1984")
print("Brisanje knjige '1984':", book_list.delete_book_by_name("1984"))
book_list.print_books_after_year(1800)

# 5. Ažuriranje ocjene knjige "Moby Dick"
print("Ažuriranje ocjene knjige 'Moby Dick':", book_list.update_book_rating("Moby Dick", 8.2))
book_list.print_books_after_year(1800)

# 6. Ispis knjiga određenog autora ("Harper Lee")
print("Knjige autora 'Harper Lee':")
book_list.print_books_by_author("Harper Lee")

# 7. Ispis knjiga koje imaju više od 300 stranica
print("Knjige sa više od 300 stranica:")
book_list.print_books_by_pages(300)"""


#3

"""# Definisanje čvora koji predstavlja zaposlenog
class EmployeeNode:
    def __init__(self, name, position, year, salary, team, projects):
        # Svaki čvor sadrži podatke o zaposlenom
        self.employee = {
            'name': name,        # Ime zaposlenog
            'position': position, # Pozicija zaposlenog
            'year': year,        # Godina zaposlenja
            'salary': salary,    # Plata zaposlenog
            'team': team,        # Tim kojem pripada
            'projects': projects # Broj projekata
        }
        self.prev = None  # Pokazivač na prethodnog zaposlenog
        self.next = None  # Pokazivač na sljedećeg zaposlenog

# Definisanje klase za dvostruko olancanu listu zaposlenih
class DoublyLinkedListEmployees:
    def __init__(self):
        self.head = None  # Glava liste
        self.tail = None  # Rep liste

    # Funkcija za dodavanje zaposlenog na kraj liste
    def append(self, new_employee):
        if not self.head:
            self.head = new_employee  # Ako je lista prazna, novi zaposleni postaje glava i rep
            self.tail = new_employee
        else:
            self.tail.next = new_employee  # Dodavanje zaposlenog na kraj liste
            new_employee.prev = self.tail  # Postavljanje pokazivača ka prethodnom zaposlenom
            self.tail = new_employee       # Novi zaposleni postaje novi rep

    # Funkcija koja pronalazi zaposlenike sa platom većom od prosječne
    def employees_above_avg_salary(self):
        current = self.head
        total_salary = 0
        count = 0
        # Računanje ukupne plate i broja zaposlenih
        while current:
            total_salary += current.employee['salary']
            count += 1
            current = current.next
        avg_salary = total_salary / count if count > 0 else 0
        
        # Ispis zaposlenih sa platom većom od prosječne
        current = self.head
        print(f"Zaposleni sa platom većom od prosječne ({avg_salary}):")
        while current:
            if current.employee['salary'] > avg_salary:
                print(current.employee)
            current = current.next

    # Funkcija koja ispisuje sve zaposlenike koji su angažovani na više od zadatog broja projekata
    def print_employees_by_projects(self, min_projects):
        current = self.head
        print(f"Zaposleni angažovani na više od {min_projects} projekata:")
        while current:
            if current.employee['projects'] > min_projects:
                print(current.employee)
            current = current.next

    # Funkcija koja povećava platu zaposlenima koji su zaposleni duže od zadatog broja godina
    def increase_salary_by_years(self, min_years, percent_increase):
        current = self.head
        print(f"Povećanje plata za zaposlenike koji su zaposleni duže od {min_years} godina za {percent_increase}%:")
        while current:
            if 2024 - current.employee['year'] > min_years:  # Pretpostavimo da je trenutna godina 2024
                increase = current.employee['salary'] * (percent_increase / 100)
                current.employee['salary'] += increase
                print(f"Plata zaposlenom {current.employee['name']} povećana na {current.employee['salary']}")
            current = current.next

    # Funkcija koja vraća listu zaposlenika koji pripadaju određenom timu i imaju platu iznad zadate vrijednosti
    def employees_by_team_and_salary(self, team, min_salary):
        current = self.head
        print(f"Zaposleni iz tima '{team}' sa platom većom od {min_salary}:")
        while current:
            if current.employee['team'].lower() == team.lower() and current.employee['salary'] > min_salary:
                print(current.employee)
            current = current.next

    # Funkcija za brisanje zaposlenog iz liste na osnovu imena
    def delete_employee_by_name(self, name):
        current = self.head
        while current:
            if current.employee['name'].lower() == name.lower():
                if current == self.head:
                    self.head = current.next  # Ažuriranje glave
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev  # Ažuriranje repa
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next  # Ažuriranje pokazivača između čvorova
                    if current.next:
                        current.next.prev = current.prev
                return True  # Vraća True nakon brisanja
            current = current.next
        return False  # Ako zaposleni nije pronađen, vraća False

    # Funkcija za ažuriranje broja projekata zaposlenog na osnovu imena
    def update_employee_projects(self, name, new_projects):
        current = self.head
        while current:
            if current.employee['name'].lower() == name.lower():
                current.employee['projects'] = new_projects
                return True
            current = current.next
        return False  # Ako zaposleni nije pronađen, vraća False

    # Funkcija koja ispisuje listu zaposlenih prema godini zaposlenja (najprije zaposleni na vrhu liste)
    def print_employees_by_year(self):
        current = self.head
        employees = []
        # Skupljanje svih zaposlenih u listu
        while current:
            employees.append(current.employee)
            current = current.next
        # Sortiranje po godini zaposlenja
        employees.sort(key=lambda x: x['year'])
        # Ispisivanje zaposlenih po godini zaposlenja
        print("Zaposleni sortirani po godini zaposlenja:")
        for emp in employees:
            print(emp)

# Testiranje funkcionalnosti

# Kreiranje čvorova za zaposlene
employee1 = EmployeeNode("Ivan Ivanovic", "Developer", 2015, 1500, "IT", 5)
employee2 = EmployeeNode("Jovan Jovanovic", "Designer", 2018, 1200, "Design", 3)
employee3 = EmployeeNode("Ana Anic", "Manager", 2012, 2000, "Management", 8)
employee4 = EmployeeNode("Milica Milic", "Developer", 2020, 1300, "IT", 2)
employee5 = EmployeeNode("Petar Petrovic", "HR", 2017, 1100, "Human Resources", 4)

# Kreiranje dvostruko olancane liste i dodavanje zaposlenih
employee_list = DoublyLinkedListEmployees()
employee_list.append(employee1)
employee_list.append(employee2)
employee_list.append(employee3)
employee_list.append(employee4)
employee_list.append(employee5)

# 1. Pronalaženje zaposlenika sa platom većom od prosječne
employee_list.employees_above_avg_salary()

# 2. Ispis zaposlenih koji su angažovani na više od 3 projekta
employee_list.print_employees_by_projects(3)

# 3. Povećanje plate zaposlenima koji su zaposleni duže od 5 godina za 10%
employee_list.increase_salary_by_years(5, 10)

# 4. Ispis zaposlenih koji pripadaju IT timu i imaju platu veću od 1200
employee_list.employees_by_team_and_salary("IT", 1200)

# 5. Brisanje zaposlenog iz liste na osnovu imena ("Ana Anic")
print("Brisanje zaposlenog 'Ana Anic':", employee_list.delete_employee_by_name("Ana Anic"))

# 6. Ažuriranje broja projekata za zaposlenog "Jovan Jovanovic"
print("Ažuriranje broja projekata za zaposlenog 'Jovan Jovanovic':", employee_list.update_employee_projects("Jovan Jovanovic", 5))

# 7. Ispis zaposlenih po godini zaposlenja
employee_list.print_employees_by_year()"""
