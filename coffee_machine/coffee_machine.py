class CupSize:
    SMALL = 3
    MEDIUM = 5
    LARGE = 7

#Clases de excepciones
class NoCupsException(Exception):
    pass

class NoSugarException(Exception):
    pass

class NoCoffeeException(Exception):
    pass

class CoffeeMachine:
    def __init__(self):
        self.cups = 10
        self.sugar = 10
        self.coffee = 50

    def select_cup_size(self, size):
        if self.cups <= 0:
            raise NoCupsException("No cups available")
        if self.coffee < size:
            raise NoCoffeeException("Not enough coffee")
        self.cups -= 1
        self.coffee -= size
        return size

    def select_sugar(self, amount):
        if amount < 0:
            raise ValueError("Cantidad de azúcar insuficiente")
        if amount > 5:
            raise ValueError("El máximo de azúcar disponible es 5")
        if self.sugar < amount:
            raise NoSugarException("Not enough sugar")
        self.sugar -= amount
        return amount

def main():
    machine = CoffeeMachine()
    print("Bienvenido a la Máquina de Café")
    while True:
        print("\nSeleccione el tamaño del vaso: 1. Pequeño 2. Mediano 3. Grande")
        choice = int(input())
        if choice == 1:
            size = CupSize.SMALL
        elif choice == 2:
            size = CupSize.MEDIUM
        elif choice == 3:
            size = CupSize.LARGE
        else:
            print("No hay ese tipo de vaso.")
            continue

        print("Seleccione la cantidad de azúcar (0-5):")
        try:
            sugar = int(input())
            machine.select_sugar(sugar)
        except ValueError as e:
            print(e)
            continue

        try:
            machine.select_cup_size(size)
            print(f"Preparando su café de {size} Oz con {sugar} cucharadas de azúcar.")
        except (NoCupsException, NoSugarException, NoCoffeeException) as e:
            print(e)

        print("¿Desea otro café? (s/n)")
        if input().lower() != 's':
            break

if __name__ == "__main__":
    main()
