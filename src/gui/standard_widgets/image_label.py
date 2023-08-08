from tkinter import ttk

from PIL import ImageTk, Image

from ..standard_widgets.tooltip import ToolTip


class ImageLabel(ttk.Label):
    def __init__(self, master, image_filepath, text, size, *args, **kwargs):
        self.size = size

        load = Image.open(image_filepath)
        load = load.resize(self.size)
        render = ImageTk.PhotoImage(load)
        super().__init__(master, text=text, image=render, *args, **kwargs)
        self.image = render
        self.tooltip = ToolTip(self, text)

    def change_image(self, image_filepath):
        load = Image.open(image_filepath)
        load = load.resize(self.size)
        render = ImageTk.PhotoImage(load)
        self.image = render
