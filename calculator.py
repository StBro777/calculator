import tkinter as tk
from tkinter import messagebox

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

def perform_calculation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operation = operation_var.get()
    
        result = calculate(a,b,operation)
        result_label.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовые значения.")

# Создаем основное окно
root = tk.Tk()
root.title("Калькулятор")

#Поля ввода
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
tk.Label(root, text="Введите первое число:").grid(row=0, column=0)


entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)
tk.Label(root, text="Введите второе число:").grid(row=1, column=0)

#Переменная для выбора операции
operation_var = tk.StringVar(value='+')

#Радио кнопки для операций
tk.Radiobutton(root, text="+", variable=operation_var, value='+').grid(row=2, column=0)
tk.Radiobutton(root, text="-", variable=operation_var, value='-').grid(row=2, column=1)
tk.Radiobutton(root, text="*", variable=operation_var, value='*').grid(row=2, column=2)
tk.Radiobutton(root, text="/", variable=operation_var, value='/').grid(row=2, column=3)

#Кнопка для выполнения расчета
calculate_button = tk.Button(root, text="Вычислить", command=perform_calculation)
calculate_button.grid(row=3, columnspan=4)


#Метка для отображения результата
result_label = tk.Label(root, text="Результат: ")
result_label.grid(row=4, columnspan=4)

#Запуск главного цикл приложения
root.mainloop()


