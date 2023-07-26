import tkinter as tk
from tkinter import TclError
from search_abr import CursAbrIter


class Window(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.curs_abr = CursAbrIter(['BYN', 'USD', 'EUR', 'RUB', 'BUS', 'BYK'])
        self.entry = tk.Entry(self)
        self.entry.bind('<KeyRelease>', self.parse)
        self.entry.pack()
        self.list_box = tk.Listbox(self)
        self.list_box.pack()
        for item in self.curs_abr:
            self.list_box.insert(tk.END, item)
        self.button = tk.Button(self, text='ОК', command=self.make_a_choice)
        self.button.pack(expand=True)

    def make_a_choice(self):
        try:
            selected_item = self.list_box.get(self.list_box.curselection())
            print(selected_item)
        except TclError:
            print('Выберите значение')

    def parse(self, e):
        self.list_box.delete(0, 'end')
        char = e.widget.get()
        data = []
        for item in self.curs_abr:
            # if item.lower().startswith(char.lower()):
            if char.lower() in item.lower():
                data.append(item)
        for item in data:
            self.list_box.insert(tk.END, item)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Temp_search_window")
    root.geometry("665x450")
    root.resizable(False, False)
    window = Window(root)
    window.pack()
    root.mainloop()
