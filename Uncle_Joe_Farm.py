class Animals:
    name = ""
    weight = ""
    food = ""

    def feed(self):
        self.food = "Накормлен/а"
        print(self.food)

    def _add_(self, other):
        return self.weight + other.weight

class Birds(Animals):
    eggs = ""

    def collect_eggs(self):
        self.eggs = "Яйца собраны"
        print(self.eggs)

class Horned_animals(Animals):
    milk = ""
    fur = ""

    def give_milk(self):
        self.milk = "Подоили"
        print(self.milk)

    def cut_fur(self):
        self.fur = "Подстригли"
        print(self.fur)

get_name = {}
weight_list = []

class Goose(Birds):
    sound = "Га-га"

goose_1 = Goose()
goose_2 = Goose()

goose_1.name = "Серый"
goose_2.name = "Белый"
goose_1.weight = 10
goose_2.weight = 12

get_name[goose_1.weight] = goose_1.name
get_name[goose_2.weight] = goose_2.name

class Chicken(Birds):
    sound = "Ко-ко"

chicken_1 = Chicken()
chicken_2 = Chicken()

chicken_1.name = "Ко-ко"
chicken_2.name = "Кукареку"
chicken_1.weight = 5
chicken_2.weight = 6

get_name[chicken_1.weight] = chicken_1.name
get_name[chicken_2.weight] = chicken_2.name

class Duck(Birds):
    sound = "Кря-кря"

duck = Duck()

duck.name = "Кряква"
duck.weight = 10

get_name[duck.weight] = duck.name

class Cow(Horned_animals):
    sound = "Му-му"

cow = Cow()
cow.name = "Манька"
cow.weight = 130 
get_name[cow.weight] = cow.name

class Sheep(Horned_animals):
    sound = "Бе-бе"

sheep_1 = Sheep()
sheep_2 = Sheep()

sheep_1.name = "Барашек"
sheep_2.name = "Кудрявый"
sheep_1.weight = 80
sheep_2.weight = 90

get_name[sheep_1.weight] = sheep_1.name
get_name[sheep_2.weight] = sheep_2.name

class Goat(Horned_animals):
    sound = "Бе-бе"

goat_1 = Goat()
goat_2 = Goat()

goat_1.name = "Рога"
goat_2.name = "Копыта"
goat_1.weight = 50
goat_2.weight = 60

get_name[goat_1.weight] = goat_1.name
get_name[goat_2.weight] = goat_2.name

general_weight = goose_1.weight + goose_2.weight + chicken_1.weight + chicken_2.weight + duck.weight + cow.weight + sheep_1.weight + sheep_2.weight + goat_1.weight + goat_2.weight
print(f"Общий вес всех животных равен: {general_weight}")

for weight in get_name:
    weight_list.append(weight)
print(f"Наибольший вес у {get_name[max(weight_list)]}")