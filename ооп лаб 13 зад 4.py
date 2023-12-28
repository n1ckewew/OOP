import tkinter as tk
from math import sqrt, log, exp

def calculate():
    x = float(entry.get())
    result = log(sqrt(abs(x - 2)) + 1.2) / (2 + exp(x)) + sqrt(2 / x)
    label_result.config(text=str(result))

root = tk.Tk()
root.title("Calculator")

label_prompt = tk.Label(root, text="Введите значение x:")
label_prompt.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Рассчитать", command=calculate)
button.pack()

label_result = tk.Label(root, text="Выражение:")
label_result.pack()

root.mainloop()
