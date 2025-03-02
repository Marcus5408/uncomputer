import tkinter as tk
from io import StringIO
import sys

def create_task_window(parent, on_complete=None):
    frame = tk.Frame(parent, bg='white')
    frame.place(relx=0.5, rely=0.5, anchor='center')
    
    # Add instructions label
    instructions = tk.Label(
        frame,
        text="Write a Python 'Hello World' program:",
        font=('Arial', 14),
        bg='white'
    )
    instructions.pack(pady=5)
    
    # Add text input
    code_input = tk.Text(
        frame,
        height=5,
        width=40,
        font=('Courier', 12)
    )
    code_input.pack(pady=10)
    
    # Result label
    result_label = tk.Label(
        frame,
        text="",
        font=('Arial', 12),
        bg='white',
        wraplength=300
    )
    result_label.pack(pady=5)
    
    def evaluate_code():
        code = code_input.get("1.0", tk.END).strip()
        # Capture stdout
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output
        
        try:
            exec(code)
            output = redirected_output.getvalue().strip()
            if output == "Hello World":
                result_label.config(text="Correct! Task completed!", fg='green')
                code_input.destroy()
                btn.destroy()
                parent.after(1000, lambda: on_complete() if on_complete else None)
            else:
                result_label.config(text="Output must be exactly 'Hello World'", fg='red')
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}", fg='red')
        finally:
            sys.stdout = old_stdout
    
    btn = tk.Button(
        frame,
        text="Check Code",
        font=('Arial', 14),
        command=evaluate_code
    )
    btn.pack(pady=10)
    
    return frame