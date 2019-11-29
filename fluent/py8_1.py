class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)

bus3.pick('Dave')
print(bus2.passengers)

print(dir(HauntedBus.__init__), HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)