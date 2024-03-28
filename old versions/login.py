import tkinter as tk
import mysql.connector
from tkinter import messagebox
import subprocess


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        
        self.username_label = tk.Label(self, text='Username')
        self.username_label.pack()
        
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        
        self.password_label = tk.Label(self, text='Password')
        self.password_label.pack()
        
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()
        
        self.login_button = tk.Button(self, text='Login', command=self.login)
        self.login_button.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        # Validate username and password

        # Connect to MySQL database
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='grpcchat')

        # Create cursor
        cursor = db.cursor()
        query = "SELECT password FROM users WHERE username = %s"
        values = (username,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        print(result[0])
        if result[0]==password:
            messagebox.showinfo("Login Succesful","Username and password are correct.")
        else:
            messagebox.showerror("Wrong Username or password.")
            return

        # If valid, close the window
        self.destroy()

         # start the client script with the username as an argument
        subprocess.Popen(["python", "client.py", username])
        
if __name__ == '__main__':
    window = LoginWindow()
    window.mainloop()
