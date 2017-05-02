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
        try:
            f = open("collections.txt", "rb")
            while True:
                try:
                    self.collections.append(pickle.load(f))
                except EOFError:
                    break
        except FileNotFoundError:
            f = open("collections.txt", "w")
        f.close()


        self.references = {}
        self.page = 1
        self.current_display = self.collections

        self.cards = self.get_cards()
        self.cards_to_add = []
        self.current_collection = None
            

        # This is the method that creates all the buttons, labels, etc.
        self.create_widgets()


    def create_widgets(self):

        # Top bar frame, including "TCG Manager" title and "New Collection" button
        top_bar = tk.Frame(self.master, padx=5, pady=5)
        top_bar.pack(fill="x")

        # TCG Manager title label
        title = tk.Label(top_bar, text="TCG Manager", font=("courier", 20))
        title.pack()

        # New collection button
        new_collection_button = tk.Button(top_bar, height=2, text="New collection", command=self.add_collection)
        new_collection_button.pack(side="right")

        # Search bar
        search_frame = tk.Frame(self.master)
        search_label = tk.Label(search_frame, height=2, text="Search:")
        search_label.pack(side="left")
        self.search = tk.Entry(search_frame)
        self.search.bind("<Key>", self.display_search)
        self.search.pack(side="right")
        search_frame.pack()


        # Collection frame that holds all the colleciton buttons
        self.collection_frame = tk.Frame(self.master)
        self.collection_frame.pack()


        # Create buttons for all the collections stored in "collections.txt"
        if len(self.collections) <= 9:
            for collection in self.collections:
                self.add_collection_button(collection, self.collection_frame)
        else:
            self.change_page('x', self.collections)


        arrow_frame = tk.Frame(self.master, pady=5)
        arrow_frame.pack(side="bottom")
        
        self.left = tk.Button(arrow_frame, padx=5, height=2, width=5, text="<<", command=lambda:self.change_page('L', self.current_display))
        self.left.config(relief=tk.FLAT)
        
        self.right = tk.Button(arrow_frame, padx=5, height=2, width=5, text=">>", command=lambda:self.change_page('R', self.current_display))
        if len(self.collections) > 9:
            self.right.config(relief=tk.RAISED)
        else:
            self.right.config(relief=tk.FLAT)

        self.left.pack(side="left")
        self.right.pack(side="right")
        


    def change_page(self, direction, to_add):

        if direction == 'L':
            if self.page == 1:
                return
            self.page -= 1
            
        elif direction == 'R':
            if len(to_add) % (self.page*9) == len(to_add):
                return
            self.page += 1


        self.collection_frame.pack_forget()
        self.collection_frame.destroy()
        self.collection_frame = tk.Frame(self.master)
        self.collection_frame.pack()

        if direction == 'x':
            for i in range(9):
                if i >= len(to_add):
                    break
                self.add_collection_button(to_add[i], self.collection_frame)
            return

        
        for i in range((self.page-1)*9, self.page*9):
            if i >= len(to_add):
                self.right.config(relief=tk.FLAT)
                break
            self.add_collection_button(to_add[i], self.collection_frame)

        if self.page > 1:
            self.left.config(relief=tk.RAISED)
        else:
            self.left.config(relief=tk.FLAT)

        if len(self.to_add) <= self.page*9:
            self.right.config(relief=tk.FLAT)
        else:
            self.right.config(relief=tk.RAISED)



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
            
            self.save()

            if len(self.current_display) < 9:
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

        new_label = tk.Label(new_frame, text=str(collection.game))
        new_label.config(height=2)
        new_label.config(width=15)
        new_label.config(bg="light gray")
        new_label.config(font=("Courier", 14))
        new_label.pack(side="left")
        
        new_button = tk.Button(new_frame, text=collection.name, command=lambda x=collection: self.view_collection(x))
        new_button.config(height=2)
        new_button.config(width=75)
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
        #frame.insert(frame.size()+1, new_frame)

        self.references[new_frame] = collection



    
    def delete_collection_button(self, collection, frame):
        index = self.collections.index(collection)
                    
        frame.pack_forget()
        del self.references[frame]
        del self.collections[index]

        index = self.current_display.index(collection)
        del self.current_display[index]

        self.save()

        
     



    # This method is called when a key is entered in the search bar
    def display_search(self, key):
        
        # Construct search term
        text = self.search.get().lower()
        if key.char == "":
            pass
        elif ord(key.char) == 8 and len(text) >= 1:
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
            if str(collection.game).lower().startswith(text):
                if collection not in to_display:
                    to_display.append(collection)

        self.current_display = to_display
        self.change_page('x', to_display)

        self.collection_frame.pack()




    def view_collection(self, collection):
        self.current_collection = collection
        
        # Create new window
        self.collection_window = tk.Toplevel(self.master)
        self.collection_window.geometry("1100x700")
        self.collection_window.resizable(False, False)
        self.collection_window.wm_title("{} -- {}".format(str(collection.game), collection.name))

        # Top bar frame
        top_bar = tk.Frame(self.collection_window, pady=5)
        top_bar.pack(fill="x")

        # Collection title label
        title = tk.Label(top_bar, text=collection.name, font=("Courier", 20), padx=5)
        title.pack(side="left")

        # Add card button
        add_card_button = tk.Button(top_bar, height=2, text="Add card", padx=5, command=lambda x=collection: self.add_cards(x))
        add_card_button.pack(side="right")


        self.card_frame = tk.Frame(self.collection_window, pady=5)

        self.display_cards(collection.cards, False)




    def get_cards(self):
        cards = []
        f = open("images\\names.txt", "r")
        names = f.readlines()
        f.close()

        for i in range(101):
            cards.append(Card(names[i], "Pokemon", "images\\{}.jpg".format(i)))
        return cards



    def display_cards(self, to_add, adding):
        self.card_frame.pack_forget()
        self.card_frame.destroy()
        self.card_frame = tk.Frame(self.collection_window, pady=5)
        self.card_frame.pack()

        r = 0
        c = 0
        for card in to_add:
            if r >= 3:
                break
            frame = tk.Frame(self.card_frame)
            frame.grid(row=r, column=c)
            button = tk.Button(frame, image=card.image, width=100, height=160, padx=2)
            button.config(command=lambda x=adding, y=card, z=button: self.card_interact(x,y,z))
            button.pack()
            label = tk.Label(frame, text=card.name, font=("Courier", 10), width=11, height=1, pady=3)
            label.pack()
            
            c += 1
            if c%8 == 0:
                c = 0
                r += 1


    def add_cards(self, collection):

        self.card_frame.pack_forget()
        self.card_frame.destroy()

        # Search bar
        self.search_frame_c = tk.Frame(self.collection_window)
        search_label = tk.Label(self.search_frame_c, height=2, text="Search:")
        search_label.pack(side="left")
        self.search_c = tk.Entry(self.search_frame_c)
        self.search_c.bind("<Key>", self.display_search_c)
        self.search_c.pack(side="right")
        self.search_frame_c.pack(side="top")

        self.add_button = tk.Button(self.collection_window, text="Add", command=lambda x=collection: self.confirm_add(x))
        self.add_button.pack(side="bottom")


    def confirm_add(self, collection):
        i = self.collections.index(collection)
        for card in self.cards_to_add:
            self.collections[i].cards.append(card)
        self.cards_to_add = []

        self.search_frame_c.pack_forget()
        self.search_frame_c.destroy()
        self.add_button.pack_forget()
        self.add_button.destroy()        
        self.display_cards(collection.cards, False)



    def card_interact(self, adding, card, button):
        if adding:
            if card not in self.cards_to_add:
                self.cards_to_add.append(card)
                button.config(relief=tk.SUNKEN)
            else:
                i = self.cards_to_add.index(card)
                del self.cards_to_add[i]
                button.config(relief=tk.RAISED)

        else:
            self.card_zoom(card)


    def card_zoom(self, card):
        self.zoom = tk.Toplevel(self.card_frame)
        self.zoom.geometry("421x650")

        frame = tk.Frame(self.zoom)
        frame.pack(fill="both")

        image = tk.Label(frame, image=card.image_large)
        image.pack()

        remove_button = tk.Button(frame, text="Remove card", height=3, command=lambda x=card, y=self.current_collection: self.remove_card(x,y))
        remove_button.pack(fill="both")


    def remove_card(self, card, collection):
        i = self.current_collection.cards.index(card)
        del self.current_collection.cards[i]
        self.zoom.destroy()
        self.display_cards(self.current_collection.cards, False)
            


    def display_search_c(self, key):
        
        # Construct search term
        text = self.search_c.get().lower()
        if key.char == "":
            pass
        elif ord(key.char) == 8 and len(text) >= 1:
            text = text[0:len(text)-1]
        elif ord(key.char) != 8:
            text += key.char.lower()
            

        # Display all collections that contain the search bar text
        self.card_frame.pack_forget()
        self.card_frame.destroy()
        self.card_frame = tk.Frame(self.collection_window)
        to_display = []
        for card in self.cards:
            if card.name.lower().startswith(text):
                to_display.append(card)

        self.display_cards(to_display, True)
        self.card_frame.pack()


    def save(self):
        with open("collections.txt", "w") as f:
            for c in self.collections:
                try:
                    pickle.dump(c, f)
                except:
                    continue

        

        

        

        
        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("TCG Manager")
    root.geometry("1100x700")
    root.resizable(False, False)
    program = MainWindow(root)
    program.mainloop()
    
