import tkinter as tk
from tkinter import messagebox, filedialog, ttk


# Функция для калькулятора
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка: деление на ноль"
        else:
            result = "Выберите операцию"

        result_label.config(text=f"Результат: {result}")
    except ValueError:
        result_label.config(text="Ошибка: введите числа")


# Функция для чекбоксов
def show_selection():
    selected_options = []
    if var1.get():
        selected_options.append("Первый вариант")
    if var2.get():
        selected_options.append("Второй вариант")
    if var3.get():
        selected_options.append("Третий вариант")

    if selected_options:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected_options)}")
    else:
        messagebox.showinfo("Выбор", "Ничего не выбрано")


# Функция для загрузки текста из файла
def load_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            text_area.delete(1.0, tk.END)  # Очищаем текстовое поле
            text_area.insert(tk.END, text)  # Вставляем текст из файла


# Создаем главное окно
root = tk.Tk()
root.title("Лобанов Александр Андреевич")  # Название приложения
root.geometry("600x600")  # Размер окна
root.resizable(width=False, height=False)


# Создаем вкладки
tab_control = ttk.Notebook(root)

# Первая вкладка - Калькулятор
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')

label1 = tk.Label(tab1, text="Первое число:")
label1.pack(pady=5)
entry1 = tk.Entry(tab1)
entry1.pack(pady=5)

label2 = tk.Label(tab1, text="Второе число:")
label2.pack(pady=5)
entry2 = tk.Entry(tab1)
entry2.pack(pady=5)

operation_var = tk.StringVar(value='+')
operation_menu = ttk.Combobox(tab1, textvariable=operation_var, values=['+', '-', '*', '/'])
operation_menu.pack(pady=5)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculate)
calculate_button.pack(pady=5)

result_label = tk.Label(tab1, text="Результат:")
result_label.pack(pady=5)

# Вторая вкладка - Чекбоксы
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack(anchor=tk.W, padx=10)

checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack(anchor=tk.W, padx=10)

checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack(anchor=tk.W, padx=10)

selection_button = tk.Button(tab2, text="Показать выбор", command=show_selection)
selection_button.pack(pady=10)

# Третья вкладка - Работа с текстом
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Работа с текстом')

load_button = tk.Button(tab3, text="Загрузить текст из файла", command=load_text)
load_button.pack(pady=10)

text_area = tk.Text(tab3, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Упаковываем вкладки
tab_control.pack(expand=1, fill='both')

# Запускаем главный цикл приложения
root.mainloop()
