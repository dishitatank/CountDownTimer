import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class CountdownTimerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Countdown Timer")
        self.geometry("400x200")

        self.time_left = None
        self.timer_running = False

        self.create_widgets()

    def create_widgets(self):
        self.duration_label = tk.Label(self, text="Enter Duration (HH:MM:SS):")
        self.duration_label.pack(pady=10)

        self.duration_entry = tk.Entry(self)
        self.duration_entry.pack(pady=5)

        self.start_button = tk.Button(self, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.time_left_label = tk.Label(self, text="", font=("Helvetica", 24))
        self.time_left_label.pack(pady=20)

    def start_timer(self):
        input_time = self.duration_entry.get()
        try:
            h, m, s = map(int, input_time.split(':'))
            self.time_left = timedelta(hours=h, minutes=m, seconds=s)
        except ValueError:
            try:
                now = datetime.now()
                target_time = datetime.strptime(input_time, "%H:%M:%S").time()
                target_datetime = datetime.combine(now.date(), target_time)
                if target_datetime < now:
                    target_datetime += timedelta(days=1)
                self.time_left = target_datetime - now
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter Time in HH:MM:SS Format")
                return

        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.timer_running:
            if self.time_left > timedelta(seconds=0):
                self.time_left -= timedelta(seconds=1)
                self.time_left_label.config(text=str(self.time_left))
                self.after(1000, self.update_timer)
            else:
                self.time_left_label.config(text="Time's up!")
                messagebox.showinfo("Countdown Timer", "Time's Up!")
                self.timer_running = False
                self.time_left = None

if __name__ == "__main__":
    app = CountdownTimerApp()
    app.mainloop()