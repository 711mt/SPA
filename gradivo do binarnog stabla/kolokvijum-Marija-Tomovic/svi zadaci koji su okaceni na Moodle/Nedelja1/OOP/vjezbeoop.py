"""class Televizor:
    def __init__(self):
        self.__broj_tekuceg_kanala = 0
        self.__naziv_tekuceg_kanala = ""
        self.__kanali = []
        self.__jacina_tona = 0

    def get_broj_tekuceg_kanala(self):
        return self.__broj_tekuceg_kanala

    def set_broj_tekuceg_kanala(self, broj):
        if 0 <= broj < len(self.__kanali):
            self.__broj_tekuceg_kanala = broj
            self.__naziv_tekuceg_kanala = self.__kanali[broj]
        else:
            print("Nevalidan broj kanala.")

    def get_naziv_tekuceg_kanala(self):
        return self.__naziv_tekuceg_kanala

    def get_kanali(self):
        return self.__kanali

    def get_jacina_tona(self):
        return self.__jacina_tona

    def set_jacina_tona(self, jacina):
        if 0 <= jacina <= 10:
            self.__jacina_tona = jacina
        else:
            print("Nevalidna jačina tona. Mora biti između 0 i 10.")

    def dodaj_kanal(self, naziv_kanala):
        self.__kanali.append(naziv_kanala)

    def obrisi_kanal(self, naziv_kanala):
        if naziv_kanala in self.__kanali:
            self.__kanali.remove(naziv_kanala)
            if self.__naziv_tekuceg_kanala == naziv_kanala:
                self.__broj_tekuceg_kanala = 0
                self.__naziv_tekuceg_kanala = ""
        else:
            print("Kanal nije pronađen.")

    def pojacaj_ton(self):
        self.set_jacina_tona(self.__jacina_tona + 1)

    def ime_kanala(self, broj_kanala):
        if 1 <= broj_kanala <= len(self.__kanali):
            return self.__kanali[broj_kanala - 1]
        else:
            return "Nevalidan broj kanala."
tv = Televizor()

tv.dodaj_kanal("Kanal 1")
tv.dodaj_kanal("Kanal 2")
tv.dodaj_kanal("Kanal 3")
print(tv.get_kanali()) 

tv.obrisi_kanal("Kanal 2")
print(tv.get_kanali()) 
tv.set_broj_tekuceg_kanala(1)
print(tv.get_naziv_tekuceg_kanala()) 
tv.set_jacina_tona(5)
tv.pojacaj_ton()
print(tv.get_jacina_tona())"""

#5
class Player:
    def __init__(self, x, y, width, height, health):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__health = health

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_health(self):
        return self.__health

    def set_health(self, health):
        if 0 <= health <= 100:
            self.__health = health
        else:
            print("Health mora biti između 0 i 100.")

class Enemy:
    def __init__(self, x, y, width, height, damage):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__damage = damage

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        if 0 <= damage <= 100:
            self.__damage = damage
        else:
            print("Damage mora biti između 0 i 100.")

def check_collision(player, enemy):
    
    player_left = player.get_x()
    player_right = player.get_x() + player.get_width()
    player_top = player.get_y()
    player_bottom = player.get_y() + player.get_height()

   
    enemy_left = enemy.get_x()
    enemy_right = enemy.get_x() + enemy.get_width()
    enemy_top = enemy.get_y()
    enemy_bottom = enemy.get_y() + enemy.get_height()

   
    return (player_left < enemy_right and
            player_right > enemy_left and
            player_top < enemy_bottom and
            player_bottom > enemy_top)

def decrease_health(player, enemy):
    if check_collision(player, enemy):
        new_health = player.get_health() - enemy.get_damage()
        player.set_health(new_health if new_health >= 0 else 0)


player = Player(10, 10, 50, 50, 100)
enemy1 = Enemy(20, 20, 30, 30, 20)
enemy2 = Enemy(100, 100, 40, 40, 10)

print(player.get_health())  
decrease_health(player, enemy1)
print(player.get_health()) 
decrease_health(player, enemy1)
print(player.get_health())