import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

from time import sleep
from windowsDPI import set_dpi

set_dpi()


class Api(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scrape App")
        self.geometry("450x700")
        self.resizable(False, False)
        self.frames = dict()

        innerContainer = ttk.Frame(master=self)
        innerContainer.grid(row=0, column=0, sticky="ew")

        self.secondFrame = ScrapeFrame(innerContainer, self)
        self.secondFrame.grid(row=0, column=0, sticky="nswe")

        firstFrame = WelcomeFrame(innerContainer, self)
        firstFrame.grid(row=0, column=0, sticky="nswe")

        self.frames[WelcomeFrame] = firstFrame
        self.frames[ScrapeFrame] = self.secondFrame

    def show_frame(self, frameContainer):
        frame = self.frames[frameContainer]
        frame.tkraise()

    def open_new_loading_window(self, lista):
        newWindow = LoadingWindow(lista)
        newWindow.after(200, newWindow.get_data)


class LoadingWindow(tk.Tk):
    def __init__(self, dataOutput):
        super().__init__()

        self.title("Scrape App")
        self.geometry("400x200")
        self.resizable(False, False)
        self.output = dataOutput

        label = ttk.Label(master=self,
                          text="""Trwa pobieranie danych z stron deweloperów
                          Aktualny status:""")
        label.grid(row=0, column=0, rowspan=2)

        self.labelOutput = ttk.Label(master=self)
        self.labelOutput.grid(row=2, column=0)

        # quitButton = ttk.Button(master=self,
        #                         text="Przerwij",
        #                         command=self.destroy)
        # quitButton.grid(row=3, column=0)

    def get_data(self):
        for item in self.output:
            self.labelOutput['text'] = item
            self.update()
            sleep(2)

        self.destroy()
        f = asksaveasfile(initialfile="Untitled.xlsx",
                          defaultextension=".xlsx",
                          filetypes=[("All files", "*.*"), ("Excel files", "*.xlsx")])


class WelcomeFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        proceedButton = ttk.Button(master=self,
                                   text="Wyświetl listę deweloperów",
                                   padding=(20, 20, 20, 20),
                                   command=lambda: controller.show_frame(ScrapeFrame))
        proceedButton.grid(row=0, column=0, sticky="ew", padx=70, pady=50)

        quitButton = ttk.Button(master=self,
                                text="Wyjdź",
                                padding=(20, 20, 20, 20),
                                command=controller.destroy)
        quitButton.grid(row=1, column=0, sticky="ew", padx=70, pady=50)


class ScrapeFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.developerList = [f"Developer {x}" for x in range(20)]
        self.loadingInfo = tk.StringVar(value="testuujemy\ntroche\ntekstu")
        developers = tk.StringVar(value=self.developerList)

        label = ttk.Label(master=self,
                          text="Zaznacz deweloperów lub ")
        label.grid(row=0, column=0, sticky="w", padx=20, pady=15)

        selectAllButton = ttk.Button(master=self,
                                     text="Zaznacz wszystkich",
                                     command=lambda: listbox.select_set(0, "end"))
        selectAllButton.grid(row=0, column=1, pady=15)

        listbox = tk.Listbox(master=self,
                             height=20,
                             listvariable=developers,
                             selectmode="extended",
                             borderwidth=5)
        listbox.grid(row=1, column=0, rowspan=3, padx=20, pady=15)

        startButton = ttk.Button(master=self,
                                 text="Zacznij pobieranie danych",
                                 command=lambda: controller.open_new_loading_window(
                                     self.handle_listbox_selection(listbox)))
        startButton.grid(row=4, column=0)

        quitButton = ttk.Button(master=self,
                                text="Wyjdź",
                                command=controller.destroy)
        quitButton.grid(row=4, column=1, sticky="e")

    def handle_listbox_selection(self, listbox):
        return [listbox.get(i)
                for i in listbox.curselection()]


root = Api()

root.mainloop()
