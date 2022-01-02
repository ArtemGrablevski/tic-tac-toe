import tkinter as tk
from tkinter import messagebox

COUNTER = 0


window = tk.Tk()
window.geometry("594x700+400+20")
window["bg"] = "#d9eefa"
window.title("Крестики-нолики")
window.resizable(False, False)


def app_exit():
    if messagebox.askokcancel("Выход", "Вы хотите выйти?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", app_exit)

def draw(button):
    global COUNTER
    if not button["text"]:
        if COUNTER % 2 == 0:
            button["text"] = "O"
            button["foreground"] = "red"
            FIELD[button] = "O"
        else:
            button["text"] = "X"
            button["foreground"] = "blue"
            FIELD[button] = "X"
        COUNTER += 1
    check_win()

def check_win():
    win_coordinates = ((b1,b2,b3), (b1,b4,b7), (b4,b5,b6), (b7,b8,b9), (b2,b5,b8), (b3,b6,b9), (b1,b5,b9), (b3,b5,b7))
    for i in win_coordinates:
        if FIELD[i[0]] == FIELD[i[1]] == FIELD[i[2]] != "":
            if COUNTER % 2 == 0:
                answer = tk.messagebox.askyesno(title="Конец игры!", message="Выиграл Х!\nНачать заново?")
                if not answer:
                    window.destroy()
                else:
                    clear_all()
            else:
                answer = tk.messagebox.askyesno(title="Конец игры!", message="Выиграл O!\nНачать заново?")
                if not answer:
                    window.destroy()
                else:
                    clear_all()
    if COUNTER == 9:
        answer = tk.messagebox.askyesno(title="Конец игры!", message="Ничья!\nНачать заново?")
        if not answer:
            window.destroy()
        else:
            clear_all()
            

def clear_all():
    global COUNTER
    global FIELD
    COUNTER = 0
    for i in FIELD.keys():
        FIELD[i] = ""
    for i in FIELD:
        i["text"] = ""
    

b1 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b1))
b1.grid(row=0, column=0)

b2 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b2))
b2.grid(row=0, column=1)

b3 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b3))
b3.grid(row=0, column=2)

b4 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b4))
b4.grid(row=1, column=0)

b5 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b5))
b5.grid(row=1, column=1)

b6 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b6))
b6.grid(row=1, column=2)

b7 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b7))
b7.grid(row=2, column=0)

b8 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b8))
b8.grid(row=2, column=1)

b9 = tk.Button(window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: draw(b9))
b9.grid(row=2, column=2)

FIELD = {b1: "", b2: "", b3: "", b4: "", b5: "", b6: "", b7: "", b8: "", b9: ""}


clear_button = tk.Button(window, text="Начать сначала", font=("Calibri", 15), command=clear_all)
clear_button.place(relx=0.382, rely=0.87)


if __name__ == "__main__":
    window.mainloop()

  
    

    