class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"Type: {self.__class__.__name__}, Health: {self.health}, Attack: {self.attack}"

    def __add__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Not valid value")
        health = self.health + other
        attack = self.attack + other
        return Warrior(health, attack)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError("Not valid value")
        health = self.health * other
        attack = self.attack * other
        return Warrior(health, attack)

    def attacking(self, other):
        other.defend(self.attack)

    def defend(self, value):
        self.health -= value


class Elf(Warrior):
    action_counter = 0

    def __init__(self, health=45, attack=7, agility=3):
        super().__init__(health, attack)
        self.agility = agility

    def __str__(self):
        return super().__str__() + f" agility: {self.agility}"

    def attacking(self, other):
        other.defend(self.attack)

    def defend(self, value):
        self.action_counter += 1
        if self.action_counter % (self.agility + 1):
            self.health -= value


class Orc(Warrior):
    action_counter = 0

    def __init__(self, health=55, attack=6, fury=2):
        super().__init__(health, attack)
        self.fury = fury

    def __str__(self):
        return super().__str__() + f" fury: {self.fury}"

    def attacking(self, other):
        self.action_counter += 1
        if not self.action_counter % 3:
            other.defend(self.attack + self.fury)
        else:
            other.defend(self.attack)

    def defend(self, value):
        self.health -= value


def fight(warrior1, warrior2):
    while warrior1.is_alive and warrior2.is_alive:
        warrior1.attacking(warrior2)
        print(warrior2)
        if warrior2.is_alive:
            warrior2.attacking(warrior1)
            print(warrior1)

    return warrior1.is_alive
