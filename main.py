import tkinter as tk

ingredients = {'Bloodgrass': 0, 'ChromusSlime': 0, ' DriedEphedra': 0, 'EmeticWax': 0, 'FennelSilk': 0,
               'GengkoBrush': 0, 'HyancinthNectar': 0, 'LavenderSprig': 0, 'MadrakeRoot': 0,
               'MilkweedSeeds': 0, 'WildSageroot': 0}
ingredientsValues = ingredients.values()
r = 0
v = 0


class AlchemyApp(tk.Tk):                #Self is 'tk'
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('900x600')
        self.config(bg='#9FD996')
        self.title("D&D Alchemy")

        self.label1 = tk.Label(text="Helloworld").grid(column=0, row=0)
        self.entrythingy = tk.Entry()
        #self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

    def on_button(self):
        print(self.entry.get())



app = AlchemyApp()
app.mainloop()