import tkinter as tk
from tkinter import scrolledtext
import sys
import io

class PythonCompiler:
    def __init__(self, win):
        self.win = win
        self.win.title("Python Compiler")

        self.code_input = scrolledtext.ScrolledText(win, width=80, height=20)
        self.code_input.pack(pady=10)

        self.run_button = tk.Button(win, text="Run", command=self.run_code)
        self.run_button.pack(pady=5)

        self.output_area = scrolledtext.ScrolledText(win, width=80, height=10)
        self.output_area.pack(pady=10)

    def run_code(self):
        self.output_area.delete(1.0, tk.END)

        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        code = self.code_input.get("1.0", tk.END)

        try:
            exec(code)
        except Exception as e:
            print(f"Error: {e}")

        sys.stdout = old_stdout

        output = new_stdout.getvalue()
        self.output_area.insert(tk.END, output)

if __name__ == "__main__":
    win = tk.Tk()
    compiler = PythonCompiler(win)
    win.mainloop()