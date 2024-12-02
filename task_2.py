from task_1 import calc_prices, check_round
import tkinter as tk
from tkinter import messagebox

def is_number(num):
    return str(num).replace(".", "", 1).isdigit()


# Функция для проверки корректности решения
def check_solution():
    input_price_with_nds = price_with_nds.get()
    input_proc_nds = proc_nds.get()

    if not is_number(input_price_with_nds):
        result = 'Некорректный ввод. \nРекомендованная цена с НДС должна быть указана в виде целого или ' \
                 'вещественного числа. \nПожалуйста, введите корректное цифровое значение.'
    elif not is_number(input_proc_nds) or not 0 < float(input_proc_nds) < 99:
        result = 'Некорректный ввод. \nПроцент НДС должен быть указан в виде целого или вещественного числа ' \
                 'в интервале от 0 до 99. \nПожалуйста, введите корректное цифровое значение.'
    else:
        with_nds, without_nds = calc_prices(float(input_price_with_nds), float(input_proc_nds))
        result = f"Цена c НДС = {with_nds}\nЦена без НДС = {without_nds}\nСтавка НДС = {input_proc_nds}"

    # Показываем результат в messagebox
    messagebox.showinfo("Результат проверки", result)


# Создание основного окна
root = tk.Tk()
root.title("Проверка решения")

# Создание метки и текстового поля для ввода
price_with_nds = tk.Label(root, text="Рекомендованная цена с НДС")
price_with_nds.pack(pady=3)
price_with_nds = tk.Entry(root)
price_with_nds.pack(pady=2)

proc_nds = tk.Label(root, text="Ставка НДС")
proc_nds.pack(pady=3)
proc_nds = tk.Entry(root)
proc_nds.pack(pady=2)

# Создание кнопки для проверки
check_button = tk.Button(root, text="Вычислить", command=check_solution)
check_button.pack(pady=10)

# Запуск основного цикла
root.mainloop()
