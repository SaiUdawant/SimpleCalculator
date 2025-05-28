import tkinter as tk

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

window = tk.Tk()
window.configure(background="light grey")
window.title("Simple Calculator")
window.geometry("300x400")

expression = ""
equation = tk.StringVar()

input_field = tk.Entry(window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14,
                       borderwidth=4)
input_field.grid(columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, height=2, width=7, command=equalpress).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, height=2, width=7, command=lambda t=text: press(t)).grid(row=row, column=col)

tk.Button(window, text='Clear', height=2, width=30, command=clear).grid(row=5, columnspan=4)

window.mainloop()
