from pynput.keyboard import Key, Listener
import tkinter as tk

def create_fullscreen_window():
    root = tk.Tk()
    root.attributes('-fullscreen', True, '-topmost', True)
    root.configure(background='black')
    
    # Add the trapped text
    label = tk.Label(
        root,
        text="YOU ARE TRAPPED",
        font=('Arial', 72, 'bold'),
        fg='red',
        bg='black'
    )
    label.place(relx=0.5, rely=0.1, anchor='center')
    
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