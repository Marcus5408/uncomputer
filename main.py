from pynput.keyboard import Key, Listener
import tkinter as tk
from tasks import get_random_task
import random

def open_task():
    """open a random task deleting all other widgets from screen in the same window"""
    for widget in root.winfo_children():
        widget.destroy()
    task = get_random_task()
    task(root, on_complete=open_task)
        
        


def create_fullscreen_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True, '-topmost', True)
    root.configure(background='white')
    
    # Add the trapped text
    label = tk.Label(
        root,
        text="No work for you!",
        font=('Arial', 72, 'bold'),
        fg='red',
        bg='white'
    )
    label.place(relx=0.5, rely=0.1, anchor='center')
    
    label2 = tk.Label(
        root,
        text="do a task?",
        font=('Arial', 32, 'bold'),
        fg='black',
        bg='white'
    )
    label2.place(relx=0.5, rely=0.2, anchor='center')
    
    
    button = tk.Button(
        root,
        text="Yes, sure!",
        font=('Arial', 24, 'bold'),
        fg='white',
        bg='green',
        command=lambda: open_task()
    )
    button.place(relx=0.5, rely=0.5, anchor='center')
    
    button2 = tk.Button(
        root,
        text="No, I'm busy",
        font=('Arial', 24, 'bold'),
        fg='white',
        bg='red',
        #make go to random on hover
        
        
        #make button go to random pos button2.place(relx=random.random(), rely=random.random(), anchor='center')
        command=lambda: root.destroy()
    )
    
    button2.bind("<Enter>", lambda e: button2.place(relx=random.random(), rely=random.random(), anchor='center'))
    button2.place(relx=0.5, rely=0.6, anchor='center')
    
    # Disable alt-f4
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    # Disable window controls
    root.overrideredirect(True)
    root.lift()  # Raise above other windows
    root.focus_force()  # Force focus
    return root

def update_window():
    global root
    if root and root.winfo_exists():
        root.lift()  # Keep raising window
        root.focus_force()  # Keep forcing focus
        root.update()
        root.after(10, update_window)  # Reduced delay for more aggressive updates

root = None
window_created = False

def on_press(key):
    global root, window_created
    print(f"[KEY↓] {key} pressed")
    
    if not window_created:
        root = create_fullscreen_window()
        window_created = True
        update_window()  # Start the update loop

def on_release(key, root):
    print(f"[KEY↑] {key} release")
    if key == Key.esc:
        root.destroy()
        return False

# Start the keyboard listener in a non-blocking way
listener = Listener(on_press=on_press, on_release=lambda key: on_release(key, root))
listener.start()

# Start the tkinter event loop
root = create_fullscreen_window()
window_created = True
root.mainloop()