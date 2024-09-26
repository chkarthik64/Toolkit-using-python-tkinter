import tkinter as tk


class Calculator:
    prevAns = None

    def inputNumbers(self, button):
        def innerFunc():
            self.entry.insert(tk.END, button["text"])
        return innerFunc

    def takeEntryInput(self):
        global prevAns
        string = self.entry.get()
        solution = eval(string)

        self.entry.delete(0, tk.END)
        self.entry.insert(0, solution)
        prevAns = float(solution)

    def clearEntry(self):
        self.entry.delete(0, tk.END)

    def backSpace(self):
        self.entry.delete(len(self.entry.get()) - 1, tk.END)

    def prevAnsPrint(self):
        global prevAns
        self.entry.insert(len(self.entry.get()), prevAns)

    def main(self):
        self.root = tk.Tk()
        self.root.title("Simple Calculator")
        self.root.geometry("500x500")

        self.entry = tk.Entry(self.root, font=('arial', 25))
        self.entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

        self.numberButtons = []

        for i in range(1, 10):
            row = (i - 1) // 3 + 1
            col = (i - 1) % 3
            self.button = tk.Button(self.root, text=str(i))
            self.numberButtons.append(self.button)
            self.button.config(command=self.inputNumbers(self.button))
            self.button.grid(row=row, column=col, sticky="nsew")

        self.dot = tk.Button(self.root, text=".")
        self.dot.config(command=self.inputNumbers(self.dot))
        self.dot.grid(row=4, column=2, sticky="nsew")
        self.zeroButton = tk.Button(self.root, text="0")
        self.zeroButton.config(command=self.inputNumbers(self.zeroButton))
        self.zeroButton.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.plusButton = tk.Button(self.root, text="+")
        self.plusButton.config(command=self.inputNumbers(self.plusButton))
        self.plusButton.grid(row=1, column=3, columnspan=1, sticky="nsew")
        self.subtractButton = tk.Button(self.root, text="-")
        self.subtractButton.config(
            command=self.inputNumbers(self.subtractButton))
        self.subtractButton.grid(row=2, column=3, columnspan=1, sticky="nsew")
        self.multiplyButton = tk.Button(self.root, text="*")
        self.multiplyButton.config(
            command=self.inputNumbers(self.multiplyButton))
        self.multiplyButton.grid(row=3, column=3, columnspan=1, sticky="nsew")
        self.divideButton = tk.Button(self.root, text="/")
        self.divideButton.config(command=self.inputNumbers(self.divideButton))
        self.divideButton.grid(row=4, column=3, columnspan=1, sticky="nsew")

        self.clearButton = tk.Button(self.root, text="Clear")
        self.clearButton.config(command=self.clearEntry)
        self.clearButton.grid(row=1, column=4, columnspan=1, sticky="nsew")

        self.backButton = tk.Button(self.root, text="BackSpace")
        self.backButton.config(command=self.backSpace)
        self.backButton.grid(row=2, column=4, columnspan=1,
                             rowspan=3, sticky="nsew")

        self.prevButton = tk.Button(self.root, text="Ans")
        self.prevButton.config(command=self.prevAnsPrint)
        self.prevButton.grid(row=5, column=4, columnspan=1,
                             rowspan=1, sticky="nsew")

        self.solveButton = tk.Button(self.root, text="=")
        self.solveButton.config(command=self.takeEntryInput)
        self.solveButton.grid(row=5, column=0, columnspan=4, sticky="nsew")

        for i in range(6):
            self.root.rowconfigure(i, weight=1)
        for i in range(5):
            self.root.columnconfigure(i, weight=1)

        self.root.mainloop()

