# First task

class Food:
    name = 'Pizza'
    kind = 'fast food'

    def describe(self):
        print(f'My favourite {self.kind} is {self.name}!')

f1 = Food()
f1.describe()

print('-' * 30)

# Second task

class Food:
    name = 'Pizza'
    kind = 'fast food'

    @classmethod
    def describe(cls):
        print(f'My favourite {cls.kind} is {cls.name}!')

f1 = Food()
f1.describe()


class Food:
    name = 'Pizza'
    kind = 'fast food'

    @staticmethod
    def describe():
        print(f'My favourite {Food.kind} is {Food.name}!')

f1 = Food()
f1.describe()

print('-' * 30)

# Third task

class Food:

    def __init__(self, food_name, food_kind):
        self.name = food_name
        self.kind = food_kind

    def describe(self):
        print(f'My favourite {self.kind} is {self.name}!')

class Meat(Food):

    def cook(self):
        print(f'{self.name} is cooked!')


class Fruit(Food):

    def clean(self):
        print(f'{self.name} has been washed!')

f1 = Food('Pizza', 'fast food')
f1.describe()

m1 = Meat('Sausage', 'barbecue')
m1.describe()
m1.cook()

fr1 = Fruit('Apple', 'homegrown')
fr1.describe()
fr1.clean()

print('-' * 30)


# Fourth task

class Food:

    def __init__(self, food_name, food_kind):
        self.name = food_name
        self.kind = food_kind

    def __repr__(self):
        return f'Class: Food, name: {self.name}, kind: {self.kind}'

    def describe(self):
        print(f'My favourite {self.kind} is {self.name}!')


f1 = Food('Pizza', 'fast food')
print(f1)

print('-' * 30)

        
