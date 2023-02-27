import tkinter as tk
import random

# setting up the window and title
main_window = tk.Tk()
main_window.title("Psychedelic Calculator")
main_window.geometry("400x500")
main_window.resizable(False, False)

# Getting the prompt set up
prompt = tk.StringVar()
field = tk.Entry(main_window, textvariable=prompt, justify="right", font=("Jokerman", 20),
                 width=18, bd=10, state="readonly")
field.grid(row=0, column=0, columnspan=4, padx=20, pady=10)


# Getting the colors
def colors():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"#{red:02x}{green:02x}{blue:02x}"  # use hexidecimal


# Functions
def click(number):
    current = prompt.get()
    if len(current) >= 20:
        current = current[:19]
    prompt.set(current + str(number))


def clear():
    prompt.set("")


def equal():
    try:
        result = eval(prompt.get())
        prompt.set(result)
    except SyntaxError:
        prompt.set("Please try again")
    except ZeroDivisionError:
        prompt.set("Undefined")


# Button grid
buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    'C', '0', '=', '/',
]

# Configuring the buttons
r = 1
c = 0
for v in buttons:
    b = tk.Button(main_window, text=v, padx=30, pady=20)
    b.grid(row=r, column=c, sticky='news')
    if v == "C":
        b.configure(command=clear)
    elif v == "=":
        b.configure(command=equal)
    else:
        b.configure(command=lambda value=v: click(value))
    c += 1
    if c > 3:
        r += 1
        c = 0


# Randomize colors
def random_c():
    main_window.configure(bg=colors())
    for w in main_window.winfo_children():
        if isinstance(w, tk.Button):
            w.configure(bg=colors())
    field.configure(bg=colors(), foreground=colors())
    main_window.after(5000, random_c)


random_c()  # activate the colors

# Keep window open
main_window.mainloop()
