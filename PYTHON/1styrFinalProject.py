import tkinter as tk
from tkinter import messagebox

class Appointment:
    def __init__(self, name, date, time, description):
        self.name = name
        self.date = date
        self.time = time
        self.description = description

class AppointmentSchedulingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Scheduling System")
        self.appointments = []

        # Create GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root, width=20)
        self.name_entry.grid(row=0, column=1)

        self.date_label = tk.Label(root, text="Date:")
        self.date_label.grid(row=1, column=0)
        self.date_entry = tk.Entry(root, width=20)
        self.date_entry.grid(row=1, column=1)

        self.time_label = tk.Label(root, text="Time:")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(root, width=20)
        self.time_entry.grid(row=2, column=1)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.grid(row=3, column=0)
        self.description_text = tk.Text(root, width=20, height=5)
        self.description_text.grid(row=3, column=1)

        self.schedule_button = tk.Button(root, text="Schedule Appointment", command=self.schedule_appointment)
        self.schedule_button.grid(row=4, column=0, columnspan=2)

        self.appointment_listbox = tk.Listbox(root, width=40)
        self.appointment_listbox.grid(row=5, column=0, columnspan=2)

    def schedule_appointment(self):
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.description_text.get("1.0", "end-1c")

        if name and date and time and description:
            appointment = Appointment(name, date, time, description)
            self.appointments.append(appointment)
            self.appointment_listbox.insert(tk.END, f"{name} - {date} {time} - {description}")
            self.name_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.description_text.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentSchedulingSystem(root)
    app.run()