from pathlib import Path
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import Interfaz.MenuPrincipal
from PIL import Image
import Interfaz.AgregarAFD
import Interfaz.ValidarCadenaAFD
import Interfaz.AyudaAFD
import Interfaz.GenerarReporteAFD
import Clases.AFD
import Clases.AFN
import Interfaz.AgregarAFN
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CargaArchvios(tk.Toplevel):
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

        def cargar_afn():
            archivo = filedialog.askopenfilename(filetypes=[('AFN Files', '*.afn')])
            if archivo:
                cargar_archivo_afn(archivo)

        def cargar_afd():
            archivo = filedialog.askopenfilename(filetypes=[('AFD Files', '*.afd')])
            if archivo:
                cargar_archivo_afd(archivo)
                

        button_2 = Button(
            self,
            bg="#2CCCEF",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            text="Cargar AFD",
            font=("Helveltica", 16),
            command=cargar_afd  # Llama a la función cargar_afd al hacer clic en el botón
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
            relief="flat",
            font=("Helveltica", 16),
            text="Cargar AFN",
            command=cargar_afn  # Llama a la función cargar_afn al hacer clic en el botón
        )
        button_3.place(
            x=0.0,
            y=240.0,
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
            text="Cargar Archivos",
            font=("Happy Monkey", 48),
            fg="#000000",
            bg="#FFFFFF"
        )
        label4.place(x=460.0, y=240.0, anchor="nw")
        
        self.resizable(False, False)



def cargar_archivo_afd(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        i = 0
        while i < len(lineas):

            nombre = ""
            estados = []
            alfabeto = []
            estado_inicial = ""
            estados_aceptacion = []
            transiciones = []

            nombre= lineas[i] = lineas[i].strip()
            estados = lineas[i+1] = lineas[i+1].strip().split(',')
            alfabeto = lineas[i+2] = lineas[i+2].strip().split(',')
            for elemento in alfabeto:
                if elemento == "ε":
                    messagebox.showerror("Error", "El alfabeto no puede contener el símbolo ε")
                    break
                
            estado_inicial = lineas[i+3] = lineas[i+3].strip()
            estados_aceptacion = lineas[i+4] = lineas[i+4].strip().split(',')
            transiciones = []
            while True:
               
                if lineas[i+5].strip() == '%':
                    i+= 1
                    break
                else:
                    transiciones.append(lineas[i+5].strip().replace(';', ','))
                    i += 1
                
            i += 5
            print(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)
            transiciones.append('')
            Interfaz.AgregarAFD.agregarAFD(nombre, estados, alfabeto,  estado_inicial, estados_aceptacion, transiciones)
           
            
        
def cargar_archivo_afn(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        i = 0
        while i < len(lineas):

            nombre = ""
            estados = []
            alfabeto = []
            estado_inicial = ""
            estados_aceptacion = []
            transiciones = []

            nombre= lineas[i] = lineas[i].strip()
            estados = lineas[i+1] = lineas[i+1].strip().split(',')
            alfabeto = lineas[i+2] = lineas[i+2].strip().split(',')
            for elemento in alfabeto:
                if elemento == "ε":
                    messagebox.showerror("Error", "El alfabeto no puede contener el símbolo ε")
                    break
                
            estado_inicial = lineas[i+3] = lineas[i+3].strip()
            estados_aceptacion = lineas[i+4] = lineas[i+4].strip().split(',')
            transiciones = []
            while True:
               
                if lineas[i+5].strip() == '%':
                    i+= 1
                    break
                else:
                    transiciones.append(lineas[i+5].strip().replace(';', ',').replace('Îµ','ε'))
                    i += 1
                
            i += 5
            print(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)
            transiciones.append('')
            Interfaz.AgregarAFN.agregarAFN(nombre, estados, alfabeto,  estado_inicial, estados_aceptacion, transiciones)
           
            