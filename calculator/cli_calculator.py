def is_exit(value):
    return value.strip().lower().replace('"', '').replace("'", '') == "exit"

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль!"
        return num1 / num2
    else:
        return "Неизвестный оператор"

print("=== Калькулятор на Python ===")
print("Напиши 'exit' или \"exit\" в любой момент, чтобы выйти\n")

while True:
    first = input("Введите первое число: ")
    if is_exit(first):
        print("Выход из калькулятора")
        break

    operator = input("Введите оператор (+, -, *, /): ")
    if is_exit(operator):
        print("Выход из калькулятора")
        break

    second = input("Введите второе число: ")
    if is_exit(second):
        print("Выход из калькулятора")
        break

    try:
        num1 = float(first)
        num2 = float(second)
        result = calculate(num1, operator, num2)
        print("Результат:", result, "\n")
    except ValueError:
        print("Пожалуйста, вводите только числа\n")
