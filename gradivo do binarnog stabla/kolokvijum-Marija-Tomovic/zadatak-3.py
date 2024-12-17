# Zadatak 3 - Red i stek

#a) Red
class Red:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
        print("Kurs", value, " je dodat.")

    def dequeue(self):
        print("Ovaj kurs je završen: ", self.items[0])
        self.pop()
        return self.items

    def pop(self):
        return self.items.pop(0)

    def stack_pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

# Funkcija koja filtrira svaki drugi kurs
    def filtriraj_svaki_drugi_kurs(self, N):
        new_red = Red()
        while not self.is_empty():
            if self.peek()[0] <= N:
                self.pop()
                continue
            else:
                new_red.enqueue(self.peek())
                self.pop()
        return new_red.items

    def push(self, value):
        self.items.append(value)

    def stack_peek(self):
        return self.items[-1]

    def convert_to_stack(self):
        stack = Red()
        while not self.is_empty():
            stack.push(self.stack_peek())
            self.stack_pop()
        return stack.items
#b funkcija koja koristi stack za obrtanje redosljeda kurseva
    def reverse_courses(self):
        stack = Red()
        while not self.is_empty():
            stack.push(self.pop())
        while not stack.is_empty():
            self.enqueue(stack.pop())
        return self.items

# Testiranje reda i funkcija
r = Red()
kurs1 = (700, "Matematika")
kurs2 = (500, "Hemija")
kurs3 = (600, "Fizika")

r.enqueue(kurs1)
r.enqueue(kurs2)
r.enqueue(kurs3)
#testiranje funkcija
print("Filtrirani kursevi:", r.filtriraj_svaki_drugi_kurs(500))
print("Originalni red:", r.items)
print("Pretvaranje u stek:", r.convert_to_stack())
print("Obrnut redosljed kurseva:", r.reverse_courses())
