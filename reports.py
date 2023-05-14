import sqlite3
import tkinter as tk
from tkinter import ttk

class ReportsDisplay(tk.Frame):
    def __init__(self, parent, main_app):
        super().__init__(parent)
        self.main_app = main_app

        ttk.Label(self, text="View Reports", font=("Arial", 24)).grid(row=0, column=0, pady=20)

        # Create Treeview widget
        self.tree = ttk.Treeview(self, columns=("Activity", "Value"), show="headings")
        self.tree.heading("Activity", text="Activity")
        self.tree.heading("Value", text="Value")
        self.tree.column("Activity", anchor="center", width=120)
        self.tree.column("Value", anchor="center", width=80)
        self.tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.load_data()

        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        back_button = ttk.Button(self, text="Back", command=lambda: self.main_app.show_frame(self.main_app.home_frame))
        back_button.grid(row=2, column=0, pady=10)

    def load_data(self):
        """Load data from SQLite databases and insert it into the Treeview."""
        # Load exercise data
        conn = sqlite3.connect("exercise_logs.db")
        c = conn.cursor()
        c.execute("SELECT * FROM exercise_logs")
        exercise_data = c.fetchall()
        conn.close()

        # Load nutrition data
        conn = sqlite3.connect("nutrition_logs.db")
        c = conn.cursor()
        c.execute("SELECT * FROM nutrition_logs")
        nutrition_data = c.fetchall()
        conn.close()

        # Insert data into Treeview
        for exercise in exercise_data:
            self.tree.insert("", "end", values=("Exercise", exercise[0]))
            self.tree.insert("", "end", values=("Duration (min)", exercise[1]))

        for nutrition in nutrition_data:
            self.tree.insert("", "end", values=("Food", nutrition[0]))
            self.tree.insert("", "end", values=("Calories", nutrition[1]))
            self.tree.insert("", "end", values=("Protein", nutrition[2]))
            self.tree.insert("", "end", values=("Carbs", nutrition[3]))
            self.tree.insert("", "end", values=("Fat", nutrition[4]))
