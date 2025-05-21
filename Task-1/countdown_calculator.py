import tkinter as tk
from tkinter import ttk, messagebox

def start_countdown(entry, label):
    try:
        t = entry.get().strip().lower()
        seconds = int(t[:-1]) * 60 if t.endswith('m') else int(t[:-1]) if t.endswith('s') else int(t)
    except:
        messagebox.showerror("Error", "Enter time like 10s or 1m")
        return

    def countdown(secs):
        if secs >= 0:
            mins, s = divmod(secs, 60)
            label.config(text=f"{mins:02}:{s:02}")
            label.after(1000, countdown, secs - 1)
        else:
            label.config(text="Time's up!")
            messagebox.showinfo("Done", "⏰ Countdown Finished!")

    countdown(seconds)

def calculate(entry, result):
    try:
        result.config(text=f"Result: {eval(entry.get())}")
    except:
        messagebox.showerror("Error", "Invalid expression")

def main():
    root = tk.Tk()
    root.title("Countdown Timer & Calculator")
    root.geometry("400x300")
    tabs = ttk.Notebook(root)

    # Timer Tab
    timer_tab = tk.Frame(tabs)
    tk.Label(timer_tab, text="Enter Time (e.g., 10s, 1m):").pack(pady=10)
    t_entry = tk.Entry(timer_tab); t_entry.pack()
    t_label = tk.Label(timer_tab, font=("Helvetica", 24)); t_label.pack(pady=10)
    tk.Button(timer_tab, text="Start Countdown", command=lambda: start_countdown(t_entry, t_label)).pack()
    tabs.add(timer_tab, text="Countdown Timer")

    # Calculator Tab
    calc_tab = tk.Frame(tabs)
    tk.Label(calc_tab, text="Enter Expression (e.g., 5+3):").pack(pady=10)
    c_entry = tk.Entry(calc_tab); c_entry.pack()
    c_result = tk.Label(calc_tab, font=("Helvetica", 14)); c_result.pack(pady=10)
    tk.Button(calc_tab, text="Calculate", command=lambda: calculate(c_entry, c_result)).pack()
    tabs.add(calc_tab, text="Calculator")

    tabs.pack(expand=True, fill="both")
    root.mainloop()

if __name__ == "__main__":
    main()
