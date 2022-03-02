import tkinter as tk

def clean_exit():
    root.destroy()

def alternate_window(is_in_root, is_in_window, window):
    def alternate_processing():
        if is_in_root and not is_in_window:
            root.withdraw()
            window.deiconify()
        else:
            window.withdraw()
            root.deiconify()
    return alternate_processing

def create_window(window, text_label):
    label = tk.Label(window, text=text_label)
    button = tk.Button(window, text="Revenir vers root", command=alternate_window(False, True, window))
    label.grid(column=0, row=0)
    button.grid(column=0, row=1)
    window.protocol("WM_DELETE_WINDOW", clean_exit)

root = tk.Tk()

a_window = tk.Toplevel(root)
b_window = tk.Toplevel(root)
c_window = tk.Toplevel(root)

create_window(a_window, "Je suis dans la fenetre a")
create_window(b_window, "Je suis dans la fenetre b")
create_window(c_window, "Je suis dans la fenetre c")

a_window.withdraw()
b_window.withdraw()
c_window.withdraw()

a_button = tk.Button(root, command=alternate_window(True, False, a_window), text="affiche fenetre a")
b_button = tk.Button(root, command=alternate_window(True, False, b_window), text="affiche fenetre b")
c_button = tk.Button(root, command=alternate_window(True, False, c_window), text="affiche fenetre c")

a_button.grid()
b_button.grid(column=1, row=0)
c_button.grid(column=2, row=0)

root.mainloop()