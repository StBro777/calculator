import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Калькулятор")
        self.geometry("400x600")
        self.resizable(False, False)

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Экран
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        # Кнопки
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=self.calculate)
            elif button == 'C':
                btn = tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=self.clear)
            else:
                btn = tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.append_to_expression(b))

            btn.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_expression(self, value):
        current_expression = self.result_var.get()
        new_expression = current_expression + str(value)
        self.result_var.set(new_expression)

    def clear(self):
        self.result_var.set("")

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Ошибка")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()