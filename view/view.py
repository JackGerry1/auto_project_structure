import tkinter as tk
from tkinter import ttk, messagebox 

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text='Choose Max Length:').grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.max_length = tk.IntVar()
        self.max_entry = ttk.Entry(self, textvariable=self.max_length, width=20)
        self.max_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        ttk.Label(self, text="Project Path:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.current_path_label = ttk.Label(self, text="No path selected")
        self.current_path_label.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.select_button = ttk.Button(self, text='Choose Path')
        self.select_button.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        self.generate_button = ttk.Button(self, text='Generate Structure')
        self.generate_button.grid(row=2, column=0, columnspan=3, pady=10)

        ttk.Label(self, text='Output:').grid(row=3, column=0, sticky="nw", padx=5, pady=(10, 0))

        self.output_text_box = tk.Text(self, height=20, width=70)
        self.output_text_box.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller
        self.select_button.config(command=self.controller.select_path)
        self.generate_button.config(command=self.controller.generate_clicked)

    def get_path(self):
        return self.current_path_label.cget("text")

    def get_max_length(self):
        if self.max_length.get() < 0:
            messagebox.showerror("Invalid Input", "Max length cannot be negative.")
            return    
        
        return self.max_length.get()


    def update_path_label(self, path):
        self.current_path_label.config(text=path)

    def display_structure(self, structure: str):
        self.output_text_box.config(state=tk.NORMAL)
        self.output_text_box.delete("1.0", tk.END)
        self.output_text_box.insert(tk.END, structure)
        self.output_text_box.config(state=tk.DISABLED)
