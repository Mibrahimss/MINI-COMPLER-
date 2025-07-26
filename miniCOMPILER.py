import tkinter as tk
from tkinter import scrolledtext
import sys
import io

class PythonCompiler:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Compiler")
        
        
        self.code_input = scrolledtext.ScrolledText(root, width=80, height=20)
        self.code_input.pack(pady=10)
        
        
        self.run_button = tk.Button(root, text="Run", command=self.run_code)
        self.run_button.pack(pady=5)
        
        # Create a text area for output
        self.output_area = scrolledtext.ScrolledText(root, width=80, height=10)
        self.output_area.pack(pady=10)

    def run_code (self):
        self.output_area.delete(1.0, tk.END)
        
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        
        code = self.code_input.get("1.0", tk.END)
        
        try:
            exec(code)
        except Exception as e:
            print(f"Error: {e}")
        
        # Reset stdout
        sys.stdout = old_stdout
        
        # Get output and display it
        output = new_stdout.getvalue()
        self.output_area.insert(tk.END, output)

if __name__ == "__main__":
    root = tk.Tk()
    compiler = PythonCompiler(root)
    root.mainloop()
