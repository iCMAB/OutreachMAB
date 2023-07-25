from tkinter import ttk

from PIL import ImageTk, Image


class Page(ttk.Frame):
    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app

    def open(self):
        pass

    def close(self):
        pass


class Updatable:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subwidgets = []

    def update(self):
        for widget in self.subwidgets:
            widget.update()


def create_image_label(master, image_filepath, text, size, *args, **kwargs):
    load = Image.open(image_filepath)
    load = load.resize(size)
    render = ImageTk.PhotoImage(load)
    img = ttk.Label(master, text=text, image=render, *args, **kwargs)
    img.image = render
    return img
