import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = combo_op.get()
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else 'Бесконечность не предел'
        else:
            result = "Неизвестная операция"
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Ошибка: введите числа")

def show_selection():
    selected = []
    if var1.get():
        selected.append("Первый")
    if var2.get():
        selected.append("Второй")
    if var3.get():
        selected.append("Третий")
    if selected:
        messagebox.showinfo("Выбор", "Вы выбрали: " + ", ".join(selected))
    else:
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")

def load_text():
    filepath = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())

root = tk.Tk()
root.title("Левин Иван Александрович")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Вкладка 1 - калькулятор
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Калькулятор")

entry_num1 = tk.Entry(tab1)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

combo_op = ttk.Combobox(tab1, values=["+", "-", "*", "/"], width=3)
combo_op.current(0)
combo_op.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = tk.Entry(tab1)
entry_num2.grid(row=0, column=2, padx=5, pady=5)

btn_calc = tk.Button(tab1, text="Вычислить", command=calculate)
btn_calc.grid(row=0, column=3, padx=5, pady=5)

label_result = tk.Label(tab1, text="Результат:")
label_result.grid(row=1, column=0, columnspan=4)

# Вкладка 2 - чекбоксы
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Выбор")

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

chk1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
chk2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
chk3 = tk.Checkbutton(tab2, text="Третий", variable=var3)

chk1.pack(anchor='w', padx=5, pady=2)
chk2.pack(anchor='w', padx=5, pady=2)
chk3.pack(anchor='w', padx=5, pady=2)

btn_show = tk.Button(tab2, text="Показать выбор", command=show_selection)
btn_show.pack(pady=10)

# Вкладка 3 - работа с текстом
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Текст")

btn_load = tk.Button(tab3, text="Загрузить текст из файла", command=load_text)
btn_load.pack(pady=5)

text = tk.Text(tab3, wrap='word')
text.pack(expand=True, fill='both', padx=5, pady=5)

root.mainloop()
