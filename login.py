import tkinter as tk
import mysql.connector
from tkinter import messagebox
import subprocess
import messaging_pb2_grpc
import grpc
from ChatGUI import ChatGUI


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EmoSense Login")
        self.geometry("550x300")
        self.iconbitmap("chat.ico")
        self.configure(bg="#128C7E")
        self.resizable(False, False)
        
        # Create username label and entry
        self.username_label = tk.Label(self, text="Username:",font=("Arial", 18), fg="#FFFFFF", bg="#128C7E")
        self.username_label.grid(row=0, column=0, padx=50, pady=20)
        self.username_entry = tk.Entry(self, font=("Arial", 18),   highlightthickness=1, highlightcolor="#FFFFFF")
        self.username_entry.grid(row=0, column=1, padx=5, pady=20)
        
        # Create password label and entry
        self.password_label = tk.Label(self, text="Password:",font=("Arial", 18), fg="#FFFFFF", bg="#128C7E")
        self.password_label.grid(row=1, column=0, padx=5, pady=20)
        self.password_entry = tk.Entry(self, show="*", font=("Arial", 18),   highlightthickness=1, highlightcolor="#FFFFFF")
        self.password_entry.grid(row=1, column=1, padx=5, pady=20)
        
        # Create login button
        self.login_button = tk.Button(self, text="Login",font=("Arial", 18), fg="#FFFFFF", bg="#075E54",
                                       activebackground="#053C32", activeforeground="#EEEEEE", 
                                       relief="flat", padx=10, pady=10, command=self.login)
        self.login_button.grid(row=3, column=0, padx=5, pady=20, sticky=tk.E)
        
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
        if result[0] == password:
            messagebox.showinfo("Login Successful", "Username and password are correct.")

            # close the login window
            self.destroy()

            # start the client script with the entered username
            #subprocess.Popen(['python3', 'ChatGUI.py', username])

            # create a stub object using the gRPC channel
            channel = grpc.insecure_channel("localhost:50051")
            stub = messaging_pb2_grpc.ChatServiceStub(channel)

            # create a ChatGUI object and run it
            chat_gui = ChatGUI(stub, username)
            chat_gui.run()
        else:
            messagebox.showerror("Wrong Username or password.")
            return

        
if __name__ == '__main__':
    window = LoginWindow()
    window.mainloop()
