import tkinter as tk
import random

def teleport():
    x = random.randint(0,1000)
    y = random.randint(0,600)

    root.geometry(f"400x200+{x}+{y}")

    root.after(500, teleport)


def do_nothing():
    pass

root = tk.Tk()
root.title("СИСТЕМА ВЗЛОМА")
root.geometry("400x200")
root.configure(bg = 'black')


root.protocol("WM_DELETE_WINDOW", do_nothing)

label = tk.Label(root, text = "ПЛАТИ МНЕ БИТКОИН", font = ("Arial",20), bg = 'black',fg = 'green')
label.pack(expand = True)

teleport()
root.mainloop()