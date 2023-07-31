import tkinter as tk
from tkinter import ttk


class BoundedEntry(ttk.Entry):
    def __init__(self, master, minimum: int, maximum: int, default: int = None, var: tk.StringVar = None, *args,
                 **kwargs):
        self.minimum = minimum
        self.maximum = maximum
        self.default = default or self.maximum
        self.string_var = var or tk.StringVar(master=self, value=str(self.default))

        validate_command = master.register(self._validate)
        super().__init__(
            master=master,
            textvariable=self.string_var,
            validate="key",
            validatecommand=(validate_command, "%P"),
            *args,
            **kwargs
        )

    def get(self) -> int:
        return int(self.string_var.get())

    def _validate(self, input):
        if input == "":
            return True

        if input.isdigit():
            value = int(input)
            if value < self.minimum:
                self.string_var.set(str(self.minimum))
            elif value > self.maximum:
                self.string_var.set(str(self.maximum))
            return True

        return False
