from game import Game
import tkinter as tk
from PIL import Image, ImageTk


class Card:

    def __init__(self, name, game, path):
        self.name = name
        self.game = game
        self.image = self.format_image(path)
        self.image_large = ImageTk.PhotoImage(Image.open(path))

    def format_image(self, path):
        img = Image.open(path)
        img = img.resize((100,160))
        return ImageTk.PhotoImage(img)
