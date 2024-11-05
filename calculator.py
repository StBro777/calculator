def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Ошибка: Деление на ноль!"
        return a / b
    else:
        return "Ошибка: Неверная операция!"

def main():
    print("Добро пожаловать в калькулятор!")
    print("Введите 'exit' для выхода.")
    
    while True:
        operation = input("Введите операцию (+, -, *, /): ")
        if operation.lower() == 'exit':
            print("Выход из программы.")
            break
        
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: Пожалуйста, введите числовые значения.")
            continue
        
        result = calculate(a, b, operation)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()