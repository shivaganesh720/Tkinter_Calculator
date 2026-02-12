import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x300")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        frame = tk.Frame(self.root)
        frame.pack()            #pack() used to display frame.

        entry = tk.Entry(frame, textvariable=self.input_text,
                         font=("Arial", 18), justify="right")
        entry.pack()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for text, row, col in buttons:
            if text == '=':
                btn = tk.Button(frame, text=text, width=6, height=2,
                                command=self.calculate)
            else:
                btn = tk.Button(frame, text=text, width=6, height=2,
                                command=lambda t=text: self.press(t))
            btn.grid(row=row, column=col)

        tk.Button(frame, text='C', width=26, height=2,
                  command=self.clear).grid(row=5, column=0, columnspan=4)

    def press(self, value):
        self.expression += value
        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.input_text.set(self.expression)
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.input_text.set("")
        self.expression = ""


root = tk.Tk()          #Tk() used to create a window
Calculator(root)
root.mainloop()         # mainloop() used to display window
