class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100

    def sleep(self, hours):
        self.energy += hours * 10
        print(f"{self.name} спить і набирає енергію.")

    def play(self, hours):
        if self.energy >= hours * 5:
            self.energy -= hours * 5
            print(f"{self.name} грається і витрачає енергію.")
        else:
            print(f"{self.name} занадто втомлений для гри.")

    def eat(self, food):
        if self.energy <= 90:
            self.energy += 10
            print(f"{self.name} їсть і отримує енергію.")
        else:
            print(f"{self.name} вже не хоче їсти.")

    def display_info(self):
        print(f"{self.name} - {self.species}")
        print(f"Енергія: {self.energy}")

# Приклад використання класу
if __name__ == "__main__":
    cat = Pet(name="Мурзик", species="Кіт")
    dog = Pet(name="Бобік", species="Собака")

    cat.display_info()
    cat.sleep(5)
    cat.play(2)
    cat.eat("Риба")
    cat.display_info()

    print("\n")

    dog.display_info()
    dog.sleep(3)
    dog.play(4)
    dog.eat("Кістка")
    dog.display_info()

