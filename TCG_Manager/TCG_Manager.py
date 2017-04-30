import tkinter as tk
import pickle

from card import Card
from game import Game
from collection import Collection

class MainWindow(tk.Frame):

    def __init__(self, master):

        super().__init__(master)
        self.master = master

        # Read collections from collections.txt
        self.collections = []
        f = open("collections.txt", "rb")
        while True:
            try:
                self.collections.append(pickle.load(f))
            except EOFError:
                break

        self.references = {}
            

        # This is the method that creates all the buttons, labels, etc.
        self.create_widgets()


    def create_widgets(self):

        # Top bar frame, including "TCG Manager" title and "New Collection" button
        top_bar = tk.Frame(self.master)
        top_bar.pack(side="top")

        # TCG Manager title label
        title = tk.Label(top_bar, text="TCG Manager", font=("courier", 20))
        title.pack(side="left")

        # New collection button
        new_collection_button = tk.Button(top_bar, height=2, text="New collection", command=self.add_collection)
        new_collection_button.pack(side="right")

        self.search_result_frame = tk.Frame(self.master)
        search_frame = tk.Frame(self.master)
        search_label = tk.Label(search_frame, height=2, text="Search:")
        search_label.pack(side="left")
        self.search = tk.Entry(search_frame)
        self.search.bind("<Key>", self.display_search)
        self.search.pack(side="right")
        search_frame.pack()

        # Collection frame that holds all the colleciton buttons
        self.collection_frame = tk.Frame(self.master)
        self.collection_frame.config(pady=5)
        self.collection_frame.pack()

        # Create buttons for all the collections stored in "collections.txt"
        for collection in self.collections:
            self.add_collection_button(collection, self.collection_frame)
        




    # Open up new window to allow user to enter name and game of new collections
    def add_collection(self):

        # Create new window
        new_window = tk.Toplevel(self.master)
        new_window.geometry("280x160")
        new_window.resizable(False, False)

        # Create Frame, Label, and Textfield for entering name of collection
        name_frame = tk.Frame(new_window, padx=10, pady=20)
        name_frame.pack()
        name_label = tk.Label(name_frame, text="Name: ")
        name_label.pack(side="left")
        name_field = tk.Entry(name_frame)
        name_field.pack(side="right")

        # Create Frame, Label, and Textfield for entering game of collection
        game_frame = tk.Frame(new_window, padx=10, pady=10)
        game_frame.pack()
        game_label = tk.Label(game_frame, text="Game: ")
        game_label.pack(side="left")
        game_field = tk.Entry(game_frame)
        game_field.pack(side="right")


        # Adds creates new Collection from values in textfields, pickles it, and
        # adds it to self.collections.
        def _create_new_collection():
            collection = Collection(name_field.get(), Game(game_field.get()))
            self.collections.append(collection)
            
            f = open("collections.txt", "wb")
            for c in self.collections:
                pickle.dump(c, f)
            f.close()

            self.add_collection_button(collection, self.collection_frame)
            new_window.destroy()

        # Frame and buttons for confirming the creation of new button or canceling
        button_frame = tk.Frame(new_window, pady=10)
        button_frame.pack()
        submit_button = tk.Button(button_frame, text="Create", width=3, padx=10, command=_create_new_collection)
        submit_button.pack(side="right")
        cancel_button = tk.Button(button_frame, text="Cancel", width=4, padx=10, command=lambda: new_window.destroy())
        cancel_button.pack(side="left")
        




    def add_collection_button(self, collection, frame):
        new_frame = tk.Frame(frame)
        
        new_button = tk.Button(new_frame, text=collection.name, command=lambda:print("view placeholder"))
        new_button.config(height=2)
        new_button.config(width=90)
        new_button.config(bg="light gray")
        new_button.config(font=("Courier", 14))
        new_button.pack(side="left")

        delete_button = tk.Button(new_frame, text="X", command=lambda x=collection, y=new_frame:self.delete_collection_button(x,y))
        delete_button.config(height=2)
        delete_button.config(width=6)
        delete_button.config(font=("Courier", 14))
        delete_button.config(bg="light gray")
        delete_button.pack(side="right")

        new_frame.pack(fill="x")

        self.references[new_frame] = collection



    
    def delete_collection_button(self, collection, frame):
        index = self.collections.index(collection)
                    
        frame.pack_forget()
        del self.references[frame]
        del self.collections[index]

        f = open("collections.txt", "wb")
        for c in self.collections:
            pickle.dump(c, f)
        f.close()
     



    # This method is called when a key is entered in the search bar
    def display_search(self, key):
        
        # Construct search term
        text = self.search.get().lower()
        if ord(key.char) == 8 and len(text) >= 1:
            text = text[0:len(text)-1]
        elif ord(key.char) != 8:
            text += key.char.lower()

        # Display all collections that contain the search bar text
        self.collection_frame.pack_forget()
        self.collection_frame.destroy()
        self.collection_frame = tk.Frame(self.master)
        to_display = []
        for collection in self.collections:
            if collection.name.lower().startswith(text):
                to_display.append(collection)
                
        for collection in to_display:
            self.add_collection_button(collection, self.collection_frame)

        self.collection_frame.pack()




if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("TCG Manager")
    root.geometry("1100x700")
    root.resizable(False, False)
    program = MainWindow(root)
    program.mainloop()
    
