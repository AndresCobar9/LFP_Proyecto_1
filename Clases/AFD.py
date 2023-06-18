import random
from tkinter import messagebox

afd_registrados = []

class AFD:
    def __init__(self, nombre,  alfabeto, estados, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = {}
        self.transicionesN = transiciones
        for transicion in transiciones:
            origen, entrada, destino = transicion.split(',')
            self.transiciones.setdefault(origen, {})[entrada] = destino

    def __str__(self):
        estados_str = ", ".join(self.estados)
        alfabeto_str = ", ".join(self.alfabeto)
        estados_aceptacion_str = ", ".join(self.estados_aceptacion)
        transiciones_str = "\n".join([f"{origen},{entrada},{destino}" for origen, transiciones in self.transiciones.items() for entrada, destino in transiciones.items()])

        return f"Nombre: {self.nombre}\nEstados: {estados_str}\nAlfabeto: {alfabeto_str}\nEstado Inicial: {self.estado_inicial}\nEstados de Aceptación: {estados_aceptacion_str}\nTransiciones:\n{transiciones_str}"
    
   

    
def generar_cadena_ejemplo(afd):
    estado_actual = afd.estado_inicial
    cadena = ""

    while True:
        transiciones = afd.transiciones.get(estado_actual)
        if not transiciones:
            messagebox.showerror(title="Error", message="No hay transiciones disponibles desde el estado actual")
            break
        
        transicion = random.choice(list(transiciones.items()))
        entrada, destino = transicion
        cadena += entrada
        estado_actual = destino

        if estado_actual in afd.estados_aceptacion:
            return cadena
    messagebox.showerror(title="Error", message="No se pudo generar una cadena de ejemplo")
    return None

def verificar_alfabeto(alfabeto):
    if len(set(alfabeto)) != len(alfabeto):
        messagebox.showerror(title="Error", message="El alfabeto no puede tener símbolos repetidos")
        return False
    else:
        return True


def verificar_estado_inicial(estado_inicial, estados):
    if estado_inicial not in estados:
        messagebox.showerror(title="Error", message="El estado inicial no está en la lista de estados")
        return False
    else:
        return True


def estados_aceptacion(estados_aceptacion, estados):
    for estado in estados_aceptacion:
        if estado not in estados:
            messagebox.showerror(title="Error", message="Los estados de aceptación no están en la lista de estados")
            return False
    return True



def verificar_transiciones(transiciones, estados, alfabeto):
    for transicion in transiciones:
        
        elementos = transicion.split(",")
        if len(elementos) != 3:
            messagebox.showerror(title="Error", message="Las transiciones deben tener 3 elementos")
            return False
        origen, entrada, destino = transicion.split(',')

        if origen not in estados or destino not in estados:
            messagebox.showerror(title="Error", message="Los estados de origen y destino deben estar en la lista de estados")
            return False
        if entrada not in alfabeto:
            messagebox.showerror(title="Error", message="El símbolo de entrada no está en el alfabeto")
            return False

    return True


def Crear_AFD(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
    afd = AFD(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)
    afd_registrados.append(afd)


def listaAFD():
    return afd_registrados


def comprobar_cadena_afd(afd, cadena):

    estado_actual = afd.estado_inicial
    
    for caracter in cadena:
        if caracter not in afd.alfabeto:
            messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AFD '{afd.nombre}'")
            return False
        
        if estado_actual not in afd.transiciones or caracter not in afd.transiciones[estado_actual]:
            messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AFD '{afd.nombre}'")
            return False
        
        estado_actual = afd.transiciones[estado_actual][caracter]
    
    if estado_actual in afd.estados_aceptacion:
       
        return f"La cadena '{cadena}' es válida en el AFD '{afd.nombre}'"
    else:
        return f"La cadena '{cadena}' no es válida en el AFD '{afd.nombre}'"