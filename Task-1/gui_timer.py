import tkinter as tk
from tkinter import messagebox

def start_timer():
    try:
        total_seconds = int(entry.get())
        countdown_gui(total_seconds)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter an integer.")

def countdown_gui(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timeformat)
        root.after(1000, lambda: countdown_gui(seconds - 1))
    else:
        messagebox.showinfo("Time's Up", "⏰ Countdown Finished!")

root = tk.Tk()
root.title("Countdown Timer")

entry = tk.Entry(root)
entry.pack(pady=10)
tk.Button(root, text="Start Timer", command=start_timer).pack()
label = tk.Label(root, font=("Helvetica", 32))
label.pack()
root.mainloop()
