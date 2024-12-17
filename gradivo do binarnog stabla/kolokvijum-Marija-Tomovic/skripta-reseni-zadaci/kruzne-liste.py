# kruzne liste: g. Tramvaj broj 8 koji kruži “u krugu osmice” ima N stajališta (N se zadaje
# na ulazu). Tramvaj sa početnog stajališta kreće bez putnika (prazan).
# Za svako stajalište se unose naziv (jedna riječ), ulaz (broj putnika koji
# ulaze – prirodan broj) i izlaz (broj putnika koji izlaze – prirodan broj).
# Napraviti kružnu povezanu listu, koja predstavlja trasu tramvaja broj 8,
# pri čemu putnici uvijek mogu da uđu u tramvaj, ali ukoliko se navede da
# na datom stajalištu izlazi više putnika nego što trenutno postoji u
# tramvaju, tada izlaze svi putnici. Svaki element liste odgovara jednom
# stajalištu i sadrži naziv stajališta i broj putnika u tramvaju u trenutku
# kada tramvaj kreće sa tog stajališta. Ispisati trasu tramvaja broj 8 sa
# podacima naziv stajališta i broj putnika. Tramvaj nastavlja da kruži, i
# za svako trenutno stajalište se ponovo unose samo brojevi putnika
# (bez naziva stajališta) koji ulaze i koji izlaze iz tramvaja. Tramvaj kruži
# bez prestanka sve dok ne ostane samo jedno stajalište na kom
# završava svoju smenu i svi putnici koji se nalaze u tom trenutku u
# tramvaju izlaze iz njega. Nakon svakog kruga (kad god tramvaj stigne
# do polaznog stajališta) ispisati trasu tramvaja. Smatra se da će tramvaj
# u nekom trenutku sigurno završiti smjenu.

class Station:
    def __init__(self, name):
        self.name = name
        self.passengers = 0
        self.next_station = None

class Tram:
    def __init__(self, num_stations):
        self.head = None
        self.current_station = None
        self.num_stations = num_stations
        self.create_stations(num_stations)
        
    def create_stations(self, num_stations):
        prev_station = None
        for i in range(num_stations):
            station_name = input(f"Unesite naziv stajališta {i + 1}: ")
            new_station = Station(station_name)
            if self.head is None:
                self.head = new_station
            if prev_station:
                prev_station.next_station = new_station
            prev_station = new_station
        if prev_station:
            prev_station.next_station = self.head  # Link last station to head to make it circular

    def run(self):
        self.current_station = self.head
        while True:
            # Ispis trenutne trase
            print("\nTrasa tramvaja broj 8:")
            self.print_route()
            
            # Unos putnika na trenutnom stajalištu
            self.manage_passengers()

            # Prelazak na sledeće stajalište
            self.current_station = self.current_station.next_station
            
            # Uslov za završavanje smene
            if self.current_station == self.head and self.current_station.passengers == 0:
                print(f"\nTramvaj završava smenu na stajalištu '{self.current_station.name}'.")
                break

    def manage_passengers(self):
        while True:
            try:
                enter = int(input(f"Unesite broj putnika koji ulaze na '{self.current_station.name}': "))
                exit = int(input(f"Unesite broj putnika koji izlaze na '{self.current_station.name}': "))
                break
            except ValueError:
                print("Molimo unesite validne brojeve.")

        # Ažuriranje broja putnika
        self.current_station.passengers += enter
        if exit >= self.current_station.passengers:
            self.current_station.passengers = 0
        else:
            self.current_station.passengers -= exit

    def print_route(self):
        current = self.head
        while True:
            print(f"Stajalište: {current.name}, Putnici: {current.passengers}")
            current = current.next_station
            if current == self.head:
                break

# Glavni deo programa
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Unesite broj stajališta: "))
            if n > 0:
                break
            else:
                print("Broj stajališta mora biti prirodan broj.")
        except ValueError:
            print("Molimo unesite validan broj.")
    
    tram = Tram(n)
    tram.run()