from tkinter import *
import math as mat

# defining window

win = Tk()
win.title("Канкулятр")
win.resizable(False, False)
show_button = Entry(win, justify=LEFT, font=("Times New Roman", "22"),
                    relief="flat", bg="#ffffff", fg="Black", width=30,
                    borderwidth=5)
show_button.grid(row=0, column=0, columnspan=4, padx=16, pady=5, )


def button_click(num):
    x = show_button.get()
    show_button.delete(0, END)
    show_button.insert(0, str(x) + str(num))


# Functions of Operators

def button_add():
    first_num = show_button.get()
    global f_num
    global math
    math = "addition"
    try:
        f_num = int(first_num)
        show_button.delete(0, END)
    except ValueError:
        pass


def button_sub():
    first_num = show_button.get()
    global f_num
    global math
    math = "subtraction"
    try:
        f_num = int(first_num)
        show_button.delete(0, END)
    except ValueError:
        pass


def button_mul():
    first_num = show_button.get()
    global f_num
    global math
    math = "multiplication"
    try:
        f_num = int(first_num)
        show_button.delete(0, END)
    except ValueError:
        pass


def button_div():
    first_num = show_button.get()
    global f_num
    global math
    math = "division"
    try:
        f_num = int(first_num)
        show_button.delete(0, END)
    except ValueError:
        pass


def button_square():
    first_num = show_button.get()
    global f_num
    global math
    math = "square"
    try:
        f_num = int(first_num)
    except ValueError:
        pass


def button_percentage():
    first_num = show_button.get()
    global f_num
    global math
    math = "percentage"
    try:
        f_num = int(first_num)
        show_button.delete(0, END)
    except ValueError:
        pass


def button_power():
    first_num = show_button.get()
    global f_num
    global math
    math = "power"
    try:
        f_num = int(first_num)
    except ValueError:
        pass


def button_factorial():
    first_num = show_button.get()
    global f_num
    global math
    math = "factorial"
    try:
        f_num = int(first_num)
    except ValueError:
        pass


def button_clear1():
    first_num = show_button.get()
    for k in range(len(first_num) - 1, -1, -1):
        show_button.delete(k)
        break


def button_clear():
    try:
        show_button.delete(0, END)
    except ValueError:
        pass


def button_equal():
    second_num = show_button.get()
    show_button.delete(0, END)
    try:
        if math == "addition":
            show_button.insert(0, f_num + int(second_num))
        elif math == "subtraction":
            show_button.insert(0, f_num - int(second_num))
        elif math == "multiplication":
            show_button.insert(0, f_num * int(second_num))
        elif math == "division":
            show_button.insert(0, f_num // int(second_num))
        elif math == "square":
            show_button.insert(0, mat.sqrt(f_num))
        elif math == "power":
            show_button.insert(0, f_num * f_num)
        elif math == "percentage":
            show_button.insert(0, f_num / 100 * int(second_num))
        else:
            show_button.insert(0, mat.factorial(f_num))
    except NameError:
        pass


# Creating Number Buttons


button_1 = Button(win, text="1", activebackground="#cce7e8", bg="#808080",
                  relief="flat", padx=24, pady=4, font=("Arial", 23),
                  bd=2, width=3, borderwidth=10,
                  activeforeground="#5e0808", command=lambda: button_click(1))
button_2 = Button(win, text="2", activebackground="#cce7e8", bg="#808080",
                  relief="flat", padx=24, pady=4, font=("Arial", 23),
                  bd=2, width=3, borderwidth=10,
                  activeforeground="#5e0808", command=lambda: button_click(2))
button_3 = Button(win, text="3", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(3))
button_4 = Button(win, text="4", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(4))
button_5 = Button(win, text="5", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(5))
button_6 = Button(win, text="6", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(6))
button_7 = Button(win, text="7", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(7))
button_8 = Button(win, text="8", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(8))
button_9 = Button(win, text="9", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(9))
button_0 = Button(win, text="0", activebackground="#cce7e8", bd=2, width=3,
                  bg="#808080", padx=24, pady=4, font=("Arial", 23),
                  borderwidth=10, relief="flat", activeforeground="#5e0808",
                  command=lambda: button_click(0))
button_dot = Button(win, text=".", activebackground="#cce7e8", bd=2, width=3,
                    bg="#808080", padx=24, pady=4, font=("Arial", 23),
                    borderwidth=10, relief="flat", activeforeground="#5e0808",
                    command=lambda: button_click("."))
# Creating Operation Buttons


button_add = Button(win, text="+", activebackground="#e07b39", bd=2, width=3,
                    padx=24, bg="#ffa500", pady=4, font=("Arial", 23),
                    borderwidth=10, relief="flat", activeforeground="#5e0808",
                    command=button_add)
button_sub = Button(win, text="-", activebackground="#e07b39", bd=2, width=3,
                    padx=24, bg="#ffa500", pady=4, font=("Arial", 23),
                    borderwidth=10, activeforeground="#5e0808", relief="flat",
                    command=button_sub)
button_mul = Button(win, text="x", activebackground="#e07b39", bd=2, width=3,
                    padx=24, bg="#ffa500", pady=4, font=("Arial", 23),
                    borderwidth=10, activeforeground="#5e0808", relief="flat",
                    command=button_mul)
button_div = Button(win, text="÷", activebackground="#e07b39",
                    bd=2, width=3, padx=24, bg="#ffa500", pady=4,
                    font=("Arial", 23), borderwidth=10,
                    activeforeground="#5e0808", relief="flat",
                    command=button_div)
button_clear1 = Button(win, text="<=", activebackground="#e07b39",
                       bd=2, width=3, padx=24, bg="#ffa500", pady=4,
                       font=("Arial", 23), borderwidth=10,
                       activeforeground="#5e0808", relief="flat",
                       command=button_clear1)
button_clear = Button(win, text="C",  activebackground="#e07b39",
                      bd=2, width=3, padx=24, bg="#5e5d5d", pady=4,
                      font=("Arial", 23), borderwidth=10, relief="flat",
                      command=button_clear)
button_percentage = Button(win, text="%", activebackground="#cce7e8",
                           bd=2, width=3, padx=24, bg="#5e5d5d", pady=4,
                           font=("Arial", 23), borderwidth=10,
                           relief="flat", command=button_percentage)
button_power = Button(win, text="x²", activebackground="#cce7e8",
                      bd=2, width=3, padx=24, bg="#808080",
                      pady=4, font=("Arial", 23), borderwidth=10,
                      relief="flat", command=button_power)
button_factorial = Button(win, text="N!", activebackground="#cce7e8",
                          bd=2, width=3, padx=24,
                          bg="#5e5d5d", pady=4,
                          font=("Arial", 23), borderwidth=10,
                          relief="flat", command=button_factorial)
button_equal = Button(win, text="=", activebackground="#e07b39",
                      bd=2, width=13,
                      padx=123, bg="#ffa500", pady=4,
                      font=("Arial", 23), borderwidth=10,
                      relief="flat", command=button_equal)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=4, column=3)
button_div.grid(row=5, column=3)

button_percentage.grid(row=1, column=1)
button_power.grid(row=5, column=0)
button_factorial.grid(row=1, column=0)
button_clear.grid(row=1, column=2)
button_clear1.grid(row=1, column=3)
button_equal.grid(row=6, column=0, columnspan=5)

win.mainloop()
