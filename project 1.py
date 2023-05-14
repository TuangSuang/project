import tkinter as tk
from tkinter import ttk
from exercise import ExerciseInput
from nutrition import NutritionInput
from reports import ReportsDisplay

class FitnessTrackerApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.create_frames()

        for frame in (self.home_frame, self.exercise_frame, self.nutrition_frame, self.reports_frame):
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

        self.show_frame(self.home_frame)

    def create_frames(self):
        self.create_home_frame()
        self.create_exercise_frame()
        self.create_nutrition_frame()
        self.create_reports_frame()

    def create_home_frame(self):
        self.home_frame = tk.Frame(self.parent, bg="lightblue")

        title_label = ttk.Label(self.home_frame, text="Welcome to Fitness Tracker", font=("Arial", 30, "bold"), background="lightblue")
        title_label.pack(expand=True, pady=20)
        title_label.place(relx=0.5, rely=.1, anchor=tk.CENTER)

        exercise_button = ttk.Button(self.home_frame, text="Input Exercise", command=lambda: self.show_frame(self.exercise_frame))
        exercise_button.pack(pady=10)
        exercise_button.place(relx=0.5, rely=.3, anchor=tk.CENTER)

        nutrition_button = ttk.Button(self.home_frame, text="Input Nutrition", command=lambda: self.show_frame(self.nutrition_frame))
        nutrition_button.pack(pady=10)
        nutrition_button.place(relx=0.5, rely=.4, anchor=tk.CENTER)

        reports_button = ttk.Button(self.home_frame, text="View Reports", command=lambda: self.show_frame(self.reports_frame))
        reports_button.pack(pady=10)
        reports_button.place(relx=0.5, rely=.5, anchor=tk.CENTER)

        exit_button = ttk.Button(self.home_frame, text="Exit", command=self.parent.quit)
        exit_button.pack(pady=10)
        exit_button.place(relx=0.5, rely=.6, anchor=tk.CENTER)

    def create_exercise_frame(self):
        self.exercise_frame = ExerciseInput(self.parent, self)

    def create_nutrition_frame(self):
        self.nutrition_frame = NutritionInput(self.parent, self)

    def create_reports_frame(self):
        self.reports_frame = ReportsDisplay(self.parent, self)

    def show_frame(self, frame):
        frame.tkraise()

def main():
    app = tk.Tk()
    app.title("Fitness Tracker")
    app.geometry("800x600")
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    # Improve the look via ttk styles
    style = ttk.Style(app)
    style.theme_use('clam') # Change as per your choice
    style.configure("TButton", foreground="midnight blue", background="light gray", font=("Helvetica", 15, "bold"), borderwidth=2)
    style.configure("TLabel", foreground="midnight blue", background="light blue", font=("Helvetica", 20, "bold"), anchor="center")

    fitness_app = FitnessTrackerApp(app)
    fitness_app.grid(row=0, column=0, sticky="nsew")

    app.mainloop()

if __name__ == "__main__":
    main()
