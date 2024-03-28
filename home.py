import tkinter as tk
import subprocess
import sys

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("EmoSense")
        self.master.iconbitmap("chat.ico")
        self.configure(bg="#128C7E")
        self.pack(fill="both", expand=True)

        # Create a label
        self.label = tk.Label(self, text="Welcome to EmoSense", font=("Arial", 28), fg="#FFFFFF", bg="#128C7E")
        self.label.pack(pady=50)

        # Create a button to go to login page
        self.login_button = tk.Button(self, text="Login", font=("Arial", 18), fg="#FFFFFF", bg="#075E54", 
                              activebackground="#053C32", activeforeground="#EEEEEE", 
                              relief="flat", padx=30, pady=10, bd=2, highlightcolor="#FFFFFF", 
                              command=self.open_login)
        self.login_button.pack(pady=20)

        # Create a button to go to signup page
        self.signup_button = tk.Button(self, text="Signup", font=("Arial", 18), fg="#FFFFFF", bg="#075E54",
                                       activebackground="#053C32", activeforeground="#EEEEEE", 
                                       relief="flat", padx=30, pady=10, command=self.open_signup)
        self.signup_button.pack(pady=20)

    # Function to open the login page
    def open_login(self):
        self.master.destroy()
        subprocess.run([sys.executable, "login.py"])

    # Function to open the signup page
    def open_signup(self):
        # You can replace this with your own code to open the signup page
        self.master.destroy()
        subprocess.run([sys.executable, "registration.py"])

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400") # Set default dimensions of the root window
    app = HomePage(master=root)
    app.mainloop()
