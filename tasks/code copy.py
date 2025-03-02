import tkinter as tk
from tkinter import ttk
import random

def create_task_window(parent, on_complete=None):
    frame = tk.Frame(parent, bg='white')
    frame.place(relx=0.5, rely=0.5, anchor='center')
    
    # Add instructions label
    instructions = tk.Label(
        frame,
        text="Complete the following task:",
        font=('Arial', 14),
        bg='white'
    )
    instructions.pack(pady=5)
    
    # Add checkbox
    checkbox_var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(
        frame,
        text="I have completed this task",
        variable=checkbox_var,
        style='TCheckbutton'
    )
    checkbox.pack(pady=10)
    
        # Add checkbox
    checkbox2_var = tk.BooleanVar()
    checkbox2_var.set(random.choice([True, False]))
    checkbox2 = ttk.Checkbutton(
        frame,
        text="I haven't completed this task",
        variable=checkbox2_var,
        style='TCheckbutton'
    )
    checkbox2.pack(pady=10)
    
    # Result label
    result_label = tk.Label(
        frame,
        text="",
        font=('Arial', 12),
        bg='white',
        wraplength=300
    )
    result_label.pack(pady=5)
    
    def validate_task():
        if checkbox_var.get() and not checkbox2_var.get():
            result_label.config(text="Correct! Task completed!", fg='green')
            checkbox.destroy()
            checkbox2.destroy()
            btn.destroy()
            parent.after(1000, lambda: on_complete() if on_complete else None)
        else:
            result_label.config(text="Please check the box to complete the task", fg='red')
    
    btn = tk.Button(
        frame,
        text="Submit",
        font=('Arial', 14),
        command=validate_task
    )
    btn.pack(pady=10)
    
    return frame