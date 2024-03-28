import tkinter as tk
from messaging_pb2 import ChatMessage
import messaging_pb2_grpc
import grpc
import sys
#from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


class ChatGUI:
    def __init__(self, stub, username):
        self.stub = stub
        self.username = username
        self.messages = []

        # create the main window
        self.window = tk.Tk()
        nm="EmoSense User : "+username
        self.window.title(nm)
        self.window.iconbitmap("chat.ico")
        self.window.configure(bg="#128C7E")

        # create the message listbox
        self.message_listbox = tk.Listbox(self.window, height=20, width=60, font=("Arial", 18),highlightthickness=1, highlightcolor="#FFFFFF")
        self.message_listbox.pack(padx=10, pady=10)

        # create the message entry field
        self.message_entry = tk.Entry(self.window, width=50, font=("Arial", 18),   highlightthickness=1, highlightcolor="#FFFFFF")
        self.message_entry.pack(padx=10, pady=5)

        # create the send button
        self.send_button = tk.Button(self.window, text="Send",font=("Arial", 18), fg="#FFFFFF", bg="#075E54",
                                       activebackground="#053C32", activeforeground="#EEEEEE", 
                                       relief="flat", padx=10, pady=10, command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

    def run(self):
        # start the GUI main loop
        self.update_messages()
        self.window.mainloop()

    def update_messages(self):
        # get new messages from the server
        self.messages = list(self.stub.ReceiveMessage(ChatMessage(username=self.username)))

        # clear the message listbox and insert the updated messages
        self.message_listbox.delete(0, tk.END)
        for message in self.messages:
            # split the message into separate lines for the original text and mood analysis
            lines = message.message.split("\n")
            self.message_listbox.insert(tk.END, f"{message.username}: {lines[0]}")
            for line in lines[1:]:
                self.message_listbox.insert(tk.END, f"{' ' * len(message.username)}{line}")


        # schedule the next update
        self.window.after(1000, self.update_messages)



    def send_message(self):
        # get the message text from the entry field
        message_text = self.message_entry.get().strip()


        """
        #Analyse the sentiment of text sent by user
        blob = TextBlob(message_text)
        if blob.sentiment.polarity > 0:
            print("You seem to be feeling positive!")
        elif blob.sentiment.polarity < 0:
            print("You seem to be feeling negative.")
        else:
            print("Your mood seems neutral.")
        """

        # initialize the sentiment analyzer
        sia = SentimentIntensityAnalyzer()

        # calculate sentiment scores for the text
        sentiment_scores = sia.polarity_scores(message_text)

        # determine the overall sentiment
        if sentiment_scores['compound'] > 0.5:
            message_text+="\n(Mood Analysis of above text:😀 Very positive!)"
        elif sentiment_scores['compound'] > 0:
            message_text+="\n(Mood Analysis of above text:🙂 Somewhat positive.)"
        elif sentiment_scores['compound'] == 0:
            message_text+="\n(Mood Analysis of above text:😐 Neutral.)"
        elif sentiment_scores['compound'] < -0.5:
            message_text+="\n(Mood Analysis of above text:😔 Very negative.)"
        else:
            message_text+="\n(Mood Analysis of above text:😕 Somewhat negative.)"

        if message_text:
            # create a new chat message and send it to the server
            chat_message = ChatMessage(username=self.username, message=message_text)
            self.stub.SendMessage(chat_message)

            # clear the message entry field
            self.message_entry.delete(0, tk.END)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ChatGUI.py <username>")
        sys.exit(1)
        
    username = sys.argv[1]

    # create a stub object using the gRPC channel
    channel = grpc.insecure_channel("localhost:50051")
    stub = messaging_pb2_grpc.ChatServiceStub(channel)

    # create a ChatGUI object and run it
    chat_gui = ChatGUI(stub, username)
    chat_gui.run()
