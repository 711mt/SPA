# w. Kreirati jednostruko olančanu listu, gdje svaki čvor predstavlja pjesmu.
# Data dio svakog čvora sadrži 4 podatka i to naziv (string), zanr (string),
# godina (int), ocjena (float) pjesme.
# i. Izračunati ukupnu prosječnu ocjenu svih pjesama za zadatu
# godinu (godina parametar funkcije).
# ii. Štampati one pjesme čija je čija je godina manja od zadate
# godine (parametar funkcije max_godina).
# Input: 2000 - 1993 - 2011 - 2007; 2007 Output: 2000 - 1993
# iii. Štampati pjesme koje imaju veću ocjenu od prosječne ocjene
# svih pjesama. Iskoristiti funkciju pod a) za računanje prosječne
# ocjene.
# iv. Sve funkcije je potrebno pozvati i testirati za bar 5 pjesama.
class SongNode:
    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating
        self.next = None  # Pointer to the next node

class SongList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def add_song(self, title, genre, year, rating):
        new_song = SongNode(title, genre, year, rating)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_song

    def average_rating(self, year):
        total_rating = 0
        count = 0
        current = self.head
        while current:
            if current.year == year:
                total_rating += current.rating
                count += 1
            current = current.next
        return total_rating / count if count > 0 else 0

    def print_songs_before_year(self, max_year):
        current = self.head
        while current:
            if current.year < max_year:
                print(f"{current.title} - {current.year}")
            current = current.next

    def print_above_average(self):
        average = self.average_rating(0)  # Calculate average for all songs
        current = self.head
        while current:
            if current.rating > average:
                print(f"{current.title} - {current.rating}")
            current = current.next

# Test the implementation
song_list = SongList()
song_list.add_song("Song A", "Pop", 1993, 4.5)
song_list.add_song("Song B", "Rock", 2000, 3.8)
song_list.add_song("Song C", "Jazz", 2011, 4.2)
song_list.add_song("Song D", "Classical", 2007, 4.0)
song_list.add_song("Song E", "Hip-Hop", 1995, 3.5)

# i. Calculate average rating for the year 2000
average_2000 = song_list.average_rating(2000)
print(f"Average rating for year 2000: {average_2000}")

# ii. Print songs with year less than 2007
print("\nSongs before the year 2007:")
song_list.print_songs_before_year(2007)

# iii. Print songs with rating above average
print("\nSongs with rating above average:")
song_list.print_above_average()