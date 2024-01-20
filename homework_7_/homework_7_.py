import re


def safe_calculator(func):
    def wrapper(expression):
        try:

            result = func(expression)

            if not isinstance(result, (int, float)):
                raise ValueError("Результат не є числом")

            return result
        except Exception as e:

            print(f"Помилка обчислення: {e}. Проблема у виразі: {expression}")

    return wrapper



@safe_calculator
def calculate(expression):
    return eval(expression)

while True:
    user_input = input("Введіть вираз або 'exit' для виходу: ")

    if user_input.lower() == 'exit':
        break

    result = calculate(user_input)
    if result is not None:
        print(f"Результат: {result}")
