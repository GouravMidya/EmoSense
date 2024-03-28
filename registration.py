import tkinter as tk
from tkinter import messagebox
import mysql.connector

class RegistrationWindow:

    def __init__(self, master):
        self.master = master
        self.master.title("EmoSense Sign up")
        self.master.geometry("550x400")
        self.master.iconbitmap("chat.ico")
        self.master.configure(bg="#128C7E")
        self.master.resizable(False, False)

        # Create username label and entry
        self.username_label = tk.Label(self.master, text="Username:",font=("Arial", 18), fg="#FFFFFF", bg="#128C7E")
        self.username_label.grid(row=0, column=0, padx=50, pady=20)
        self.username_entry = tk.Entry(self.master, font=("Arial", 18),   highlightthickness=1, highlightcolor="#FFFFFF")
        self.username_entry.grid(row=0, column=1, padx=5, pady=20)

        # Create password label and entry
        self.password_label = tk.Label(self.master, text="Password:",font=("Arial", 18), fg="#FFFFFF", bg="#128C7E")
        self.password_label.grid(row=1, column=0, padx=5, pady=20)
        self.password_entry = tk.Entry(self.master, show="*", font=("Arial", 18),   highlightthickness=1, highlightcolor="#FFFFFF")
        self.password_entry.grid(row=1, column=1, padx=5, pady=20)

        # Create confirm password label and entry
        self.confirm_password_label = tk.Label(self.master, text="Confirm Password:",font=("Arial", 18), fg="#FFFFFF", bg="#128C7E")
        self.confirm_password_label.grid(row=2, column=0, padx=5, pady=20)
        self.confirm_password_entry = tk.Entry(self.master, show="*", font=("Arial", 18),   highlightthickness=1, highlightcolor="#FFFFFF")
        self.confirm_password_entry.grid(row=2, column=1, padx=5, pady=20)

        # Create register button
        self.register_button = tk.Button(self.master, text="Sign up",font=("Arial", 18), fg="#FFFFFF", bg="#075E54",
                                       activebackground="#053C32", activeforeground="#EEEEEE", 
                                       relief="flat", padx=10, pady=10, command=self.register)
        self.register_button.grid(row=3, column=0, padx=5, pady=20, sticky=tk.E)

        # Create cancel button
        self.cancel_button = tk.Button(self.master, text="Cancel" ,font=("Arial", 18), fg="#FFFFFF", bg="#075E54",
                                       activebackground="#053C32", activeforeground="#EEEEEE", 
                                       relief="flat", padx=10, pady=10, command=self.master.destroy)
        self.cancel_button.grid(row=3, column=1, padx=5, pady=20)

    def register(self):
        # Get username, password, and confirm password from entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Check if password and confirm password match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        # Connect to MySQL database
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='grpcchat')

        # Create cursor
        cursor = db.cursor()

        # Check if username already exists
        query = "SELECT * FROM users WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            messagebox.showerror("Error", "Username already exists.")
            return

        # Insert new user into database
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)
        db.commit()
        messagebox.showinfo("Success!", "User Registered!")

        # Close database connection and destroy window
        cursor.close()
        db.close()
        self.master.destroy()

# Create tkinter window
root = tk.Tk()

# Create registration window
registration_window = RegistrationWindow(root)

# Run tkinter main loop
root.mainloop()
