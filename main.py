import tkinter as tk
import random

defaultFont = ("Source Code Pro", 14)


class App:
    def __init__(self):
        self.clickmeButton = None
        self.copyHexValueButton = None
        self.hexLabel = None
        self.hexValue = None

        self.window = tk.Tk()
        self.window.title("Random Color")
        self.window.geometry("300x300")
        self.window.resizable(False, False)

        self.add_hex_label()
        self.add_copy_hex_value_button()
        self.add_clickme_button()
        self.generate_hex_value()

    def generate_hex_value(self):
        self.hexValue = ""
        for i in range(0, 6):
            self.hexValue = self.hexValue + str(random.randint(0, 9))

        self.change_color()
        self.change_label()

    def change_color(self):
        self.window.config(
            background=f"#{self.hexValue}"
        )

    def change_label(self):
        self.hexLabel.config(
            text=f"#{self.hexValue}"
        )

    def add_clickme_button(self):
        self.clickmeButton = tk.Button(
            text="Click Me!",
            font=defaultFont,
            cursor="hand2",
            borderwidth=2,
            relief="groove",
            command=self.generate_hex_value,
        )
        self.clickmeButton.pack(expand=True)

    def copy_hex_value(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(f"#{self.hexValue}")

    def add_copy_hex_value_button(self):
        self.copyHexValueButton = tk.Button(
            text="Copy!",
            font=defaultFont,
            cursor="hand2",
            borderwidth=2,
            relief="groove",
            command=self.copy_hex_value
        )
        self.copyHexValueButton.pack()

    def add_hex_label(self):
        self.hexLabel = tk.Label(
            font=defaultFont,
            borderwidth=2,
            relief="groove"
        )
        self.hexLabel.pack(expand=True)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    myApp = App()
    myApp.run()
