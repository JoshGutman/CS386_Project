import unittest
import tkinter as tk
import threading

from TCG_Manager import *
from card import Card
from game import Game
from collection import Collection

class TestEmptyCollectionFields(unittest.TestCase):

    root = tk.Tk()
    program = MainWindow(root)
    t = threading.Thread(target=program.mainloop)


    # Test to make sure the amount of collections remains the smae if the
    # name field has no text in it but the game field does
    def test_no_name(self):
        # Insert some text into the game field but not the name field
        length = len(TestEmptyCollectionFields.program.collections)
        TestEmptyCollectionFields.program.add_collection()
        TestEmptyCollectionFields.program.game_field.insert(0, "test")
        TestEmptyCollectionFields.program.submit_button.invoke()

        self.assertEqual(length, len(TestEmptyCollectionFields.program.collections))


    # Test to make sure the amount of collections remains the same if the
    # game field has no text in it but the name field does
    def test_no_game(self):
        # Insert some text into the name field but not the game field
        length = len(TestEmptyCollectionFields.program.collections)
        TestEmptyCollectionFields.program.add_collection()
        TestEmptyCollectionFields.program.name_field.insert(0, "test")
        TestEmptyCollectionFields.program.submit_button.invoke()

        self.assertEqual(length, len(TestEmptyCollectionFields.program.collections))


    # Test to make sure the amount of collections remains the same if both the
    # game and name fields have nothing in them
    def test_no_game_and_name(self):
        # Don't insert any text into any field
        length = len(TestEmptyCollectionFields.program.collections)
        TestEmptyCollectionFields.program.add_collection()
        TestEmptyCollectionFields.program.submit_button.invoke()
        
        self.assertEqual(length, len(TestEmptyCollectionFields.program.collections))


    # Test to make sure the amount of collections is 1 greater after correctly
    # inputting text into the name and game fields
    def test_correct_entry(self):
        # Insert text into both fields
        length = len(TestEmptyCollectionFields.program.collections)
        TestEmptyCollectionFields.program.add_collection()
        TestEmptyCollectionFields.program.name_field.insert(0, "testName")
        TestEmptyCollectionFields.program.game_field.insert(0, "testGame")
        TestEmptyCollectionFields.program.submit_button.invoke()
        
        self.assertEqual(length+1, len(TestEmptyCollectionFields.program.collections))



class TestAddingCards(unittest.TestCase):

    root = tk.Tk()
    program = MainWindow(root)
    t = threading.Thread(target=program.mainloop)     


    # Test to make sure the amount of cards in a collection is 1 greater
    # after pressing the add button with 1 card selected
    def test_adding_one_card(self):
        # Make sure there is at least one collection
        TestAddingCards.program.add_collection()
        TestAddingCards.program.name_field.insert(0, "testName")
        TestAddingCards.program.game_field.insert(0, "testGame")
        TestAddingCards.program.submit_button.invoke()

        c = TestAddingCards.program.collections[0]
        length = len(c.cards)
        TestAddingCards.program.view_collection(c)
        TestAddingCards.program.add_card_button.invoke()
        TestAddingCards.program.display_cards(TestAddingCards.program.cards, True)

        TestAddingCards.program.displayed_buttons[0].invoke()
        TestAddingCards.program.add_button.invoke()

        self.assertEqual(length+1, len(c.cards))


    # Test to make sure the amount of cards in a collection is 2 greater
    # after pressing the add button with 2 cards selected
    def test_adding_two_cards(self):

        c = TestAddingCards.program.collections[0]
        length = len(c.cards)
        TestAddingCards.program.view_collection(c)
        TestAddingCards.program.add_card_button.invoke()
        TestAddingCards.program.display_cards(TestAddingCards.program.cards, True)

        TestAddingCards.program.displayed_buttons[0].invoke()
        TestAddingCards.program.displayed_buttons[1].invoke()
        TestAddingCards.program.add_button.invoke()

        self.assertEqual(length+2, len(c.cards))


    # Test to make sure the amount of cards in a collection stays the same after
    # pressing the add button with no cards selected
    def test_adding_zero_cards(self):

        c = TestAddingCards.program.collections[0]
        length = len(c.cards)
        TestAddingCards.program.view_collection(c)
        TestAddingCards.program.add_card_button.invoke()
        TestAddingCards.program.display_cards(TestAddingCards.program.cards, True)

        TestAddingCards.program.add_button.invoke()
        
        self.assertEqual(length, len(c.cards))




class TestRemovingCards(unittest.TestCase):

    root = tk.Tk()
    program = MainWindow(root)
    t = threading.Thread(target=program.mainloop)


    # Test to make sure the length of the cards of one of the collections is
    # 1 less after pressing the remove card button
    def test_removing_card(self):
        # Make sure there is at least one collection
        TestRemovingCards.program.add_collection()
        TestRemovingCards.program.name_field.insert(0, "testName")
        TestRemovingCards.program.game_field.insert(0, "testGame")
        TestRemovingCards.program.submit_button.invoke()

        # Add a card to the collection
        c = TestRemovingCards.program.collections[0]
        TestRemovingCards.program.view_collection(c)
        TestRemovingCards.program.add_card_button.invoke()
        TestRemovingCards.program.display_cards(TestAddingCards.program.cards, True)
        TestRemovingCards.program.displayed_buttons[0].invoke()
        TestRemovingCards.program.add_button.invoke()

        length = len(c.cards)
        TestRemovingCards.program.remove_card(c.cards[0], None)
        self.assertEqual(length-1, len(c.cards))
        



class TestRemovingDecks(unittest.TestCase):

    root = tk.Tk()
    program = MainWindow(root)
    t = threading.Thread(target=program.mainloop)


    # Test to make sure the length of the currently displayed collections is
    # 1 less after pressing the delete button on one of the collections
    def Test_Removing_Deck(self):
        # Make sure there is at least one collection
        TestRemovingDecks.program.add_collection()
        TestRemovingDecks.program.name_field.insert(0, "testName")
        TestRemovingDecks.program.game_field.insert(0, "testGame")
        TestRemovingDecks.program.submit_button.invoke()

        length = len(TestRemovingDecks.program.current_display)
        TestRemovingDecks.program.delete_buttons[0].invoke()
        self.assertEqual(length-1, TestRemovingDecks.program.current_display)

    


if __name__ == "__main__":
    unittest.main()
