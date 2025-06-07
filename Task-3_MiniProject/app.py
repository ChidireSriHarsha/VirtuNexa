import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from markdown2 import markdown
import pandas as pd
from datetime import datetime
import os

history = []

class SmartEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Markdown Converter + Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.theme = tk.StringVar(value="light")

        # Menu
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Markdown", command=self.open_md)
        filemenu.add_command(label="Save as HTML", command=self.save_html)
        filemenu.add_separator()
        filemenu.add_command(label="Export History", command=self.export_history)
        menubar.add_cascade(label="File", menu=filemenu)

        thememenu = tk.Menu(menubar, tearoff=0)
        thememenu.add_command(label="Toggle Theme", command=self.toggle_theme)
        menubar.add_cascade(label="Theme", menu=thememenu)

        self.root.config(menu=menubar)

        # Layout
        frame = ttk.Frame(self.root, padding="5")
        frame.pack(fill=tk.BOTH, expand=True)

        self.editor = tk.Text(frame, width=60)
        self.preview = tk.Text(frame, width=60, bg="#f4f4f4", state="disabled")
        self.calc_entry = tk.Entry(frame)
        self.calc_result = tk.Label(frame, text="Result: ")
        calc_button = tk.Button(frame, text="Calculate", command=self.calculate)

        self.editor.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=5, pady=5)
        self.preview.grid(row=0, column=1, rowspan=3, sticky="nsew", padx=5, pady=5)
        self.calc_entry.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        calc_button.grid(row=3, column=1, sticky="ew", padx=5)
        self.calc_result.grid(row=4, column=0, columnspan=2, sticky="w", padx=5)

        self.editor.bind("<KeyRelease>", self.update_preview)

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

    def update_preview(self, event=None):
        md_text = self.editor.get("1.0", tk.END)
        html = markdown(md_text)
        self.preview.config(state="normal")
        self.preview.delete("1.0", tk.END)
        self.preview.insert(tk.END, html)
        self.preview.config(state="disabled")

    def open_md(self):
        filepath = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
        if filepath:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                self.editor.delete("1.0", tk.END)
                self.editor.insert(tk.END, content)
            self.update_preview()

    def save_html(self):
        html = self.preview.get("1.0", tk.END)
        filepath = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
        if filepath:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            messagebox.showinfo("Saved", f"HTML saved to {filepath}")

    def calculate(self):
        expression = self.calc_entry.get()
        try:
            result = eval(expression)
            self.calc_result.config(text=f"Result: {result}")
            history.append({"Expression": expression, "Result": result, "Timestamp": datetime.now()})
        except Exception:
            self.calc_result.config(text="Error in calculation")

    def export_history(self):
        if history:
            df = pd.DataFrame(history)
            file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV File", "*.csv")])
            if file:
                df.to_csv(file, index=False)
                messagebox.showinfo("Exported", f"History exported to {file}")
        else:
            messagebox.showwarning("No History", "No history to export.")

    def toggle_theme(self):
        if self.theme.get() == "light":
            self.preview.config(bg="black", fg="white")
            self.theme.set("dark")
        else:
            self.preview.config(bg="#f4f4f4", fg="black")
            self.theme.set("light")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartEditor(root)
    root.mainloop()
