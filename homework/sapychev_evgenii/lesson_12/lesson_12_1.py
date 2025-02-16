class Flower():
    def __init__(self, name, freshness, color, stem_lenght, life_time, price):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_lenght = stem_lenght
        self.life_time = life_time
        self.price = price

    def __str__(self):
        return (f'{self.name}, Свежесть от 0 до 10 - {self.freshness},'
                f'цвет - {self.color}, длина стебля - {self.stem_lenght} см,'
                f'среднее время жизни - {self.life_time} дней, цена - {self.price}р.')


class Rose(Flower):
    def __init__(self, name, freshness, color, stem_lenght, life_time, price):
        super().__init__(name, freshness, color, stem_lenght, life_time, price)


class Gladiolus(Flower):
    def __init__(self, name, freshness, color, stem_lenght, life_time, price):
        super().__init__(name, freshness, color, stem_lenght, life_time, price)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def __str__(self):
        return "\n".join(str(flower) for flower in self.flowers)

    def withering(self):
        return sum(flower.life_time for flower in self.flowers) / len(self.flowers)

    def sort_freshness(self):
        return self.flowers.sort(key=lambda flower: flower.freshness)

    def sort_color(self):
        return self.flowers.sort(key=lambda flower: flower.color)

    def sort_stem_lenght(self):
        return self.flowers.sort(key=lambda flower: flower.stem_lenght, reverse=True)

    def sort_price(self):
        return self.flowers.sort(key=lambda flower: flower.price)


rose1 = Rose('боза', 1, 'red', 25, 10, 500)
rose2 = Rose('воза', 2, 'red', 26, 10, 499)
rose3 = Rose('аоза', 20, 'red', 98, 10, 498)
gladiolus1 = Gladiolus('Гладиолус', 99, 'white', 30, 5, 499)
gladiolus2 = Gladiolus('Гладиолус', 27, 'blue', 30, 5, 300)
gladiolus3 = Gladiolus('Гладиолус', 28, 'green', 30, 5, 200)
bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(rose2)
bouquet.add_flower(rose3)
bouquet.add_flower(gladiolus1)
bouquet.add_flower(gladiolus2)
bouquet.add_flower(gladiolus3)
print(f'Состав букета \n{bouquet}')
print(f'Среднее время жизни букета \n{bouquet.withering()}')
bouquet.sort_freshness()
print(f'Соритировка по свежести \n{bouquet}')
bouquet.sort_color()
print(f'Соритировка по цвету \n{bouquet}')
bouquet.sort_stem_lenght()
print(f'Соритировка по длине стебля \n{bouquet}')
bouquet.sort_price()
print(f'Соритировка по цене \n{bouquet}')
