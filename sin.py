import tkinter as tk
from tkinter import ttk
import math

root = tk.Tk()
root.title("Graphic of sin(x)")

selected_value = tk.StringVar()

# Combobox
cb = ttk.Combobox(root, textvariable=selected_value)
cb['values'] = ["0.5","1","2","3"]
cb['state'] = 'readonly'
cb.pack()

# Canvas
width = 290
height = 280
c = tk.Canvas(width=width, height=height, bg='white')
c.pack()

def value_is_chosen(event):

    # Clearing Canvas
    c.delete("all")

    # text
    str_ox = ['-П',' -П/2','         0','          П/2','              П']
    x = 70
    for i in str_ox:
        c.create_text(x, 170, anchor='sw', text=i)
        x += 30

    # sin(x)
    ok = float(selected_value.get())
    if ok >= 1:
            x_stretch = 0.04*ok
    else:
            x_stretch = 0.04*(-1)*ok

    y_stretch = -80
    center = height // 2
    x_plus = 1
    center_line = c.create_line(0, center, width, center, fill='blue')
    xy = []

    for x in range(400):
        xy.append(x * x_plus)
        xy.append(int(math.sin(x * x_stretch) * y_stretch) + center)
    sin_line = c.create_line(xy, width=2, fill='orange')


cb.bind('<<ComboboxSelected>>', value_is_chosen)

root.mainloop()
