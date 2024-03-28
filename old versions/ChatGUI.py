import tkinter as tk
from messaging_pb2 import ChatMessage

class ChatGUI:
    def __init__(self, stub, username):
        self.stub = stub
        self.username = username
        self.messages = []

        # create the main window
        self.window = tk.Tk()
        self.window.title("Chat App")

        # create the message listbox
        self.message_listbox = tk.Listbox(self.window, height=20, width=60)
        self.message_listbox.pack(padx=10, pady=10)

        # create the message entry field
        self.message_entry = tk.Entry(self.window, width=50)
        self.message_entry.pack(padx=10, pady=5)

        # create the send button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

    def run(self):
        # start the GUI main loop
        self.update_messages()
        self.window.mainloop()

    def update_messages(self):
        # get new messages from the server
        for chat_message in self.stub.ReceiveMessage(ChatMessage(username=self.username)):
            self.messages.append(chat_message)

        # clear the message listbox and insert the updated messages
        self.message_listbox.delete(0, tk.END)
        for message in self.messages:
            self.message_listbox.insert(tk.END, f"{message.username}: {message.message}")

        # schedule the next update
        self.window.after(1000, self.update_messages)

    def send_message(self):
        # get the message text from the entry field
        message_text = self.message_entry.get().strip()

        if message_text:
            # create a new chat message and send it to the server
            chat_message = ChatMessage(username=self.username, message=message_text)
            self.stub.SendMessage(chat_message)

            # clear the message entry field
            self.message_entry.delete(0, tk.END)

username="gourav"
ChatGUI(username)
