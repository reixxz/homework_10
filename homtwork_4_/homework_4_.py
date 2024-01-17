import random

class Shuffler:
    def __init__(self, number):
        self.number = number

    def _random_operation(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)
        if operation == '+':
            return self.number + operand
        elif operation == '-':
            return self.number - operand
        elif operation == '*':
            return self.number * operand
        elif operation == '/':
            return self.number / operand

    def encrypt(self):
        self.number = self._random_operation()

    def decrypt(self):
        return self.number

if __name__ == "__main__":
    number_to_encrypt = 42
    shuffler = Shuffler(number_to_encrypt)

    shuffler.encrypt()

    encrypted_result = shuffler.decrypt()
    print(f"Зашифроване число: {encrypted_result}")
