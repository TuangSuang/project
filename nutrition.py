import sqlite3
from tkinter import ttk, messagebox
import tkinter as tk

class NutritionInput(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app

        # Create the nutrition input screen
        ttk.Label(self, text="Nutrition Input", font=("Arial", 30, "bold")).grid(row=0, column=0, pady=20, columnspan=2)

        labels = ["Food Item:", "Calories:", "Protein:", "Carbs:", "Fat:"]
        self.entries = []
        for idx, label in enumerate(labels):
            ttk.Label(self, text=label, font=("Arial", 18)).grid(row=idx + 1, column=0, pady=10, padx=10, sticky="w")
            entry = ttk.Entry(self)
            entry.grid(row=idx + 1, column=1, pady=10, padx=10, sticky="ew")
            self.entries.append(entry)
            self.columnconfigure(1, weight=1)

        self.log_button = ttk.Button(self, text="Log Nutrition", command=self.log_nutrition)
        self.log_button.grid(row=6, column=0, columnspan=2, pady=20)

        back_button = ttk.Button(self, text="Back", command=lambda: self.main_app.show_frame(self.main_app.home_frame))
        back_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.init_database()

    def init_database(self):
        conn = sqlite3.connect("nutrition_logs.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS nutrition_logs (
                    food_item TEXT,
                    calories INTEGER,
                    protein INTEGER,
                    carbs INTEGER,
                    fat INTEGER
                    )""")
        conn.commit()
        conn.close()

    def log_nutrition(self):
        food_item, calories, protein, carbs, fat = [entry.get() for entry in self.entries]

        if not all([food_item, calories, protein, carbs, fat]):
            messagebox.showerror("Error", "Please enter all fields.")
            return

        # Add entry to database
        conn = sqlite3.connect("nutrition_logs.db")
        c = conn.cursor()
        c.execute("INSERT INTO nutrition_logs VALUES (?, ?, ?, ?, ?)",
                  (food_item, calories, protein, carbs, fat))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Nutrition logged successfully!")

        # Clear input fields
        for entry in self.entries:
            entry.delete(0, tk.END)
