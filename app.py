import tkinter as tk
from tkinter import ttk
from csv_generator import generate_csv

class CSVGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CSV Generator")
        self.geometry("400x200")

        self.setup_ui()

    def setup_ui(self):
        self.link_label = ttk.Label(self, text="Link:")
        self.link_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.link_entry = ttk.Entry(self, width=30)
        self.link_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.class_name_label = ttk.Label(self, text="Class Name:")
        self.class_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.class_name_entry = ttk.Entry(self, width=30)
        self.class_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.generate_button = ttk.Button(self, text="Generate CSV", command=self.generate_csv)
        self.generate_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def generate_csv(self):
        link = self.link_entry.get()
        class_name = self.class_name_entry.get()

        # Call the function from csv_generator.py
        success = generate_csv(link, class_name)
        if success:
            print("CSV generated successfully!")
        else:
            print("Failed to generate CSV. Check your link.")

if __name__ == "__main__":
    app = CSVGeneratorApp()
    app.mainloop()
