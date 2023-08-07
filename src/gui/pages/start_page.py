import customtkinter as ctk

from src.gui.standard_widgets.page import Page


class StartPage(Page):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # label of frame Layout 2
        label = ctk.CTkLabel(
            self,
            text="Hungry Hungry\nBandits",
            justify="center",
            text_color="black",
            font=ctk.CTkFont(size=36)
        )

        # putting the grid in its place by using
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=2, weight=1)
        # grid
        label.grid(row=0, column=1, padx=10, pady=50)

        button1 = ctk.CTkButton(self, text="Start",
                             command=lambda: self.app.set_page("bandits_explained"), font=ctk.CTkFont(size=24))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10, ipadx=50, ipady=20)


        ## button to show frame 2 with text layout2
        button2 = ctk.CTkButton(self, text="Settings", command=lambda: self.app.set_page("bandits_explained"), font=ctk.CTkFont(size=24))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10, ipadx=50, ipady=20)

        button3 = ctk.CTkButton(self, text="Quit", command=lambda: self.app.destroy(), font=ctk.CTkFont(size=24))
        button3.grid(row=3, column=1, padx=10, pady=10, ipadx=50, ipady=20)



