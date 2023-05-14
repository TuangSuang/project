import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ExerciseInput(tk.Frame):
    """A frame for logging exercise input."""

    # Constants for labels and button texts
    EXERCISE_INPUT_TITLE = "Exercise Input"
    EXERCISE_TYPE_LABEL = "Exercise Type:"
    DURATION_LABEL = "Duration (mins):"
    LOG_EXERCISE_BUTTON_TEXT = "Log Exercise"
    BACK_BUTTON_TEXT = "Back"

    def __init__(self, parent: tk.Widget, main_app: tk.Widget) -> None:
        super().__init__(parent)
        self.parent = parent
        self.main_app = main_app

        # Create the exercise input screen
        ttk.Label(self, text=self.EXERCISE_INPUT_TITLE, font=("Arial", 24, "bold")).pack(pady=20)

        # Exercise type input
        ttk.Label(self, text=self.EXERCISE_TYPE_LABEL, font=("Arial", 18)).pack(pady=10)
        self.exercise_type_entry = ttk.Entry(self)
        self.exercise_type_entry.pack(pady=10)

        # Duration input
        ttk.Label(self, text=self.DURATION_LABEL, font=("Arial", 18)).pack(pady=10)
        self.duration_entry = ttk.Entry(self)
        self.duration_entry.pack(pady=10)

        # Log exercise button
        self.log_exercise_button = ttk.Button(self, text=self.LOG_EXERCISE_BUTTON_TEXT, command=self.log_exercise)
        self.log_exercise_button.pack(pady=20)

        # Back button
        back_button = ttk.Button(self, text=self.BACK_BUTTON_TEXT, command=lambda: self.main_app.show_frame(self.main_app.home_frame))
        back_button.pack(pady=10)

        # Initialize database
        self.init_database()

    def init_database(self) -> None:
        """Initialize the SQLite3 database and create the table for exercise logs."""
        conn = sqlite3.connect("exercise_logs.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS exercise_logs (
                    exercise_type TEXT,
                    duration INTEGER
                    )""")

        conn.commit()
        conn.close()

    def log_exercise(self) -> None:
        """Logs exercise input."""

        exercise_type = self.exercise_type_entry.get()
        duration = self.duration_entry.get()

        # Validate input
        if not all([exercise_type, duration]):
            messagebox.showerror("Error", "Please enter all fields.")
            return

        # Log the exercise into the database
        conn = sqlite3.connect("exercise_logs.db")
        c = conn.cursor()

        c.execute("INSERT INTO exercise_logs VALUES (?, ?)", (exercise_type, duration))

        conn.commit()
        conn.close()

        # Clear the entry fields after logging
        self.exercise_type_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Exercise logged successfully!")
