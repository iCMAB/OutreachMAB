import tkinter as tk
from tkinter import ttk


class BoundedEntry(ttk.Entry):
    def __init__(
            self,
            master,
            minimum: int,
            maximum: int,
            default: int = None,
            var: tk.StringVar = None,
            func=None,
            *args,
            **kwargs
    ):
        self.minimum = minimum
        self.maximum = maximum
        self.default = default if default is not None else self.maximum
        self.string_var = var or tk.StringVar(master=self, value=str(self.default))
        self.func = func

        validate_command = master.register(self._validate)
        super().__init__(
            master=master,
            textvariable=self.string_var,
            validate="key",
            validatecommand=(validate_command, "%P"),
            *args,
            **kwargs
        )
        self.bind(sequence="<FocusOut>", func=self.handle_input)
        self.bind(sequence="<Key-Return>", func=self.handle_input)

    def _validate(self, input):
        if input == "":
            return True

        if input.isdigit():
            return True

        return False

    def handle_input(self, *args):
        value = self.string_var.get()
        if value == "":
            value = self.default
            self.string_var.set(str(value))
        else:
            value = int(value)

        if value < self.minimum:
            value = self.minimum
            self.string_var.set(str(value))
        elif value > self.maximum:
            value = self.maximum
            self.string_var.set(str(value))

        if self.func:
            self.func(value)
