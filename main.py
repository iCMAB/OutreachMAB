from src.gui.app import App


def main():
    config_file = "config.json"
    app = App(config_file)
    app.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
