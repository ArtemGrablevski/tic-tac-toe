import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("594x700+400+20")
        self.window["bg"] = "#d9eefa"
        self.window.title("Крестики-нолики")
        self.window.resizable(False, False)
        self.counter = 0


    def app_exit(self):
        if messagebox.askokcancel("Выход", "Вы хотите выйти?"):
            self.window.destroy()


    def create_field(self):

        b1 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b1))
        b2 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b2))
        b3 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b3))
        b4 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b4))
        b5 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b5))
        b6 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b6))
        b7 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b7))
        b8 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b8))
        b9 = tk.Button(self.window, text="", font=("Verdana", 60, 'bold'), width=3, height=1, padx=10, pady=10, bd=3, command = lambda: self.draw(b9))

        self.field = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

        index = 0
        while index != 9:
            for i in range(3):
                for j in range(3):
                    self.field[index].grid(row=i, column=j)
                    index += 1


    def create_clear_button(self):
        clear_button = tk.Button(self.window, text="Начать сначала", font=("Calibri", 15), command=self.clear_all)
        clear_button.place(relx=0.382, rely=0.87)


    def clear_all(self):
        for i in self.field:
            i["text"] = ""
        self.counter = 0 


    def draw(self, button):
        if not button["text"]:
            if self.counter % 2 == 0:
                button["text"] = "O"
                button["foreground"] = "red"
            else:
                button["text"] = "X"
                button["foreground"] = "blue"
            self.counter += 1
            self.check_win()


    def check_win(self):
        win_coordinates = ((0, 1, 2), (0, 3, 6), (3, 4, 5), (6, 7, 8), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in win_coordinates:
            if self.field[i[0]]["text"] == self.field[i[1]]["text"] == self.field[i[2]]["text"] != "":
                if self.counter % 2 == 0:
                    answer = messagebox.askyesno(title="Конец игры!", message="Выиграл Х!\nНачать заново?")
                    if not answer:
                        self.window.destroy()
                    else:
                        self.clear_all()
                else:
                    answer = messagebox.askyesno(title="Конец игры!", message="Выиграл O!\nНачать заново?")
                    if not answer:
                        self.window.destroy()
                    else:
                        self.clear_all()
        if self.counter == 9:
            answer = messagebox.askyesno(title="Конец игры!", message="Ничья!\nНачать заново?")
            if not answer:
                self.window.destroy()
            else:
                self.clear_all()


    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self.app_exit)
        self.create_field()
        self.create_clear_button()
        self.window.mainloop()

