from pathlib import Path
from tkinter import *
import tkinter as tk
import Interfaz.MenuPrincipal
from PIL import Image
import Interfaz.AgregarAFN
import Interfaz.ValidarCadena
import Interfaz.GenerarReporteAFN
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class moduloAFN(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (1115/2)
        y = (screen_height/2) - (600/2)
        self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))
        self.overrideredirect(True)  # Turns off title bar and geometry
        self.wm_attributes("-topmost", 1)  # Forces tkinter window to be on top of all other windows

        self.geometry("1115x600")
        self.configure(bg="#FFFFFF")
        def on_enter(event):
            event.widget.config(bg="#288AC0", fg="white")

        def on_leave(event):
            event.widget.config(bg="#2CCCEF", fg="black")

        def abrir_menu_principal():
            self.destroy()

        button_1 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helvetica", 16),
            text="Crear AFN",
            command=lambda: Interfaz.AgregarAFN.AgregarAFN()
        )
        button_1.bind("<Enter>", on_enter)
        button_1.bind("<Leave>", on_leave)
        button_1.place(x=0.0, y=0.0, width=327.0, height=120.0)

        button_2 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Interfaz.ValidarCadena.ValidarCadena(),
            relief="flat",
            text="Evaluar Cadena",
            font=("Helveltica", 16),
        )
        button_2.place(
            x=0.0,
            y=120.0,
            width=327.0,
            height=120.0
        )
        button_2.bind("<Enter>", on_enter)
        button_2.bind("<Leave>", on_leave)

        button_3 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
            font=("Helveltica", 16),
            text="Ayuda"
        )
        button_3.place(
            x=0.0,
            y=360.0,
            width=327.0,
            height=120.0
        )
        button_3.bind("<Enter>", on_enter)
        button_3.bind("<Leave>", on_leave)
        button_4 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Helveltica", 16),
            command=abrir_menu_principal,
            text="Regresar"
        )
        button_4.place(
            x=0.0,
            y=480.0,
            width=327.0,
            height=120.0
        )
        button_4.bind("<Enter>", on_enter)
        button_4.bind("<Leave>", on_leave)
        button_5 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Interfaz.GenerarReporteAFN.GenerarReporteAFN(),
            relief="flat",
            font=("Helveltica", 16),
            text="Generar Reporte AFN"
        )
        button_5.place(
            x=0.0,
            y=240.0,
            width=327.0,
            height=120.0
        )
        button_5.bind("<Enter>", on_enter)
        button_5.bind("<Leave>", on_leave)

        label1 = Label(
        self,
        text="Lenguajes Formales y de Programacion",
        font=("Happy Monkey", 28),
        bg="#FFFFFF",
        )
        label1.place(x=350.0, y=45.0, anchor="nw")

        label2 = Label(
            self,
            text="Seccion P",
            font=("Happy Monkey", 12),
            fg="#000000",
            bg="#FFFFFF"
        )
        label2.place(x=983.0, y=98.0, anchor="nw")

        label3 = Label(
            self,
            text="Luis Andres Cobar Sandoval 202010097",
            font=("Happy Monkey", 9),
            fg="#8B8B8B",
            bg="#FFFFFF"
        )
        label3.place(x=865.0, y=575.0, anchor="nw")

        label4 = Label(
            self,
            text="MODULO AFN",
            font=("Happy Monkey", 48),
            fg="#000000",
            bg="#FFFFFF"
        )
        label4.place(x=543.0, y=280.0, anchor="nw")
        
        self.resizable(False, False)

