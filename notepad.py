import tkinter as tk
from tkinter import filedialog


class Notepad(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("900x600")
        self.resizable(width=False, height=False)

        self.OPTIONS = [
            "File",
            "Save File",
        ]

        self.file_var = tk.StringVar()
        self.file_var.set(self.OPTIONS[0])
        self.file_var.trace_add('write', self.check_file_var)
        file_option_menu = tk.OptionMenu(
            self, self.file_var, *self.OPTIONS)
        file_option_menu.grid(row=0, column=0, sticky="nsew")
        edit_btn = tk.Button(self, text="Edit", height=2)
        edit_btn.grid(row=0, column=1, sticky="nsew")
        exit_btn = tk.Button(self, text="Exit",
                             height=2, command=self.delete)
        exit_btn.grid(row=0, column=2, sticky="nsew")

        self.input_text = tk.Text(self)
        self.input_text.grid(row=1, column=0, columnspan=3)
        self.input_text.config(width=112, height=37)

        for i in range(2):
            self.rowconfigure(i, weight=1)
        for i in range(3):
            self.columnconfigure(i, weight=1)

        self.mainloop()

    def delete(self):
        self.destroy()

    def picker(self):
        if self.file_var.get() == "save_file":
            self.save_file()

    def save_file(self):
        self.file_var.set(self.OPTIONS[0])
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            f = open(file_path, "w")
            text = self.input_text.get('1.0', tk.END)
            f.write(text)
            f.close()

    def check_file_var(self, *args):
        if self.file_var.get() == "Save File":
            self.save_file()
