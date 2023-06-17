from tkinter import END, Tk, Label, Button, Entry, Text
import tkinter
import Clases.AFN
from tkinter import messagebox
class AyudaAFN(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("880x700")
        self.configure(bg="#FFFFFF")
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (940/2)
        y = (screen_height/2) - (680/2)
        self.geometry("%dx%d+%d+%d" % (940, 680, x, y))
        self.overrideredirect(True)  # Turns off title bar and geometry
        self.wm_attributes("-topmost", 2)  # Forces tkinter window to be on top of all other windows
    
        def on_enter(event):
            event.widget.config(bg="gray", fg="white")

        def on_leave(event):
            event.widget.config(bg="lightgray", fg="black")

        self.label_1 = Label(
            self,
            text="Luis Andres Cobar Sandoval 202010097",
            bg="#FFFFFF",
            fg="#8B8B8B",
            font=("Happy Monkey", 10)
        )
        self.label_1.place(x=684.0, y=655.0, anchor="nw")

        self.label_2 = Label(
            self,
            text="Agregar AFN",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 48)
        )
        self.label_2.place(x=321.0, y=26.0, anchor="nw")

        self.label_3 = Label(
            self,
            text="Nombre",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.label_3.place(x=102.0, y=148.0, anchor="nw")

        self.entry_1 = Label(
             self,
            text="Cualquier Nombre que Desee",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.entry_1.place(x=265.0, y=146.0, width=621.0, height=34.0)

        self.label_4 = Label(
            self,
            text="Alfabeto",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.label_4.place(x=100.0, y=193.0, anchor="nw")

        self.entry_2 = Label(
             self,
            text="Formato: a,b,c,...",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.entry_2.place(x=265.0, y=195.0, width=621.0, height=34.0)

        self.label_5 = Label(
            self,
            text="Estados",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.label_5.place(x=101.0, y=242.0, anchor="nw")

        self.entry_3 = Label(
            self,
            text="Formato: q0,q1,q2,...",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.entry_3.place(x=265.0, y=244.0, width=621.0, height=34.0)

        self.label_6 = Label(
            self,
            text="Estado Inicial",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.label_6.place(x=71.0, y=294.0, anchor="nw")

        self.entry_4 = Label(
             self,
            text="Formato: q0  (Solamente 1 Estado Inicial)",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.entry_4.place(x=265.0, y=293.0, width=621.0, height=34.0)

        self.label_7 = Label(
            self,
            text="Estados Finales",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.label_7.place(x=52.0, y=343.0, anchor="nw")

        self.label_8 = Label(
            self,
            text="Transiciones",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.label_8.place(x=64.0, y=393.0, anchor="nw")

        self.entry_5 = Label(
            self,
            text="Formato: q0;q1;q2...",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.entry_5.place(x=265.0, y=342.0, width=621.0, height=34.0)

        self.text_1 = Label(
            self,
            text="---- Formato ----\nq0,a,q1\nq1,b,q2\nq2,c,q3\n...",
            bg="#FFFFFF",
            fg="#000000",
            font=("Happy Monkey", 18)
        )
        self.text_1.place(x=265.0, y=385.0, width=621.0, height=195.0)

    
        self.button_6 = Button(
            self,
            borderwidth=0,
            highlightthickness=0,
            bg="lightgray",
            relief="flat",
            text = "REGRESAR",
            command=lambda: self.destroy()
        )
        self.button_6.bind("<Enter>", on_enter)
        self.button_6.bind("<Leave>", on_leave)
        self.button_6.place(x=2.0, y=578, width=250.0, height=100.0)

        self.resizable(False, False)