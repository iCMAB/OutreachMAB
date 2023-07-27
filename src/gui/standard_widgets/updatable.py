class Updatable:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subwidgets = []

    def update(self):
        for widget in self.subwidgets:
            widget.update()
