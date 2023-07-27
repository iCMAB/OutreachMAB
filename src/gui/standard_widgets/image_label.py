from tkinter import ttk

from PIL import ImageTk, Image


class ImageLabel(ttk.Label):
    def __init__(self, master, image_filepath, text, size, *args, **kwargs):
        self.size = size

        load = Image.open(image_filepath)
        load = load.resize(self.size)
        render = ImageTk.PhotoImage(load)
        super().__init__(master, text=text, image=render, *args, **kwargs)
        self.image = render

    def change_image(self, image_filepath):
        load = Image.open(image_filepath)
        load = load.resize(self.size)
        render = ImageTk.PhotoImage(load)
        self.image = render
