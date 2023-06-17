import random
from tkinter import messagebox

afn_registrados = []

class AFN:
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
    
   

    
def generar_cadena_ejemplo(afn):
    estado_actual = afn.estado_inicial
    cadena = ""

    while True:
        transiciones = afn.transiciones.get(estado_actual)
        if not transiciones:
            messagebox.showerror(title="Error", message="No hay transiciones disponibles desde el estado actual")
            # No hay transiciones disponibles desde el estado actual
            break
        
        transicion = random.choice(list(transiciones.items()))
        entrada, destino = transicion
        cadena += entrada
        estado_actual = destino

        if estado_actual in afn.estados_aceptacion:
            # Se alcanzó un estado de aceptación, la cadena es válida
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


def Crear_AFN(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
    afn = AFN(nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones)
    afn_registrados.append(afn)


def listaAFN():
    return afn_registrados


def comprobar_cadena_afn(afn, cadena):
    # Verificar si la cadena es válida en el AFN utilizando el método de Thompson
    
    # Obtener el estado inicial del AFN
    estado_actual = afn.estado_inicial
    
    # Recorrer cada caracter de la cadena
    for caracter in cadena:
        # Verificar si el caracter está en el alfabeto del AFN
        if caracter not in afn.alfabeto:
            messagebox.showerror(title="Error", message=f"El caracter '{caracter}' no está en el alfabeto del AFN '{afn.nombre}'")
            return False
        
        # Verificar si existe una transición para el estado actual y el caracter actual
        if estado_actual not in afn.transiciones or caracter not in afn.transiciones[estado_actual]:
            messagebox.showerror(title="Error", message=f"No hay una transición definida para el estado '{estado_actual}' y el caracter '{caracter}' en el AFN '{afn.nombre}'")
            return False
        
        # Obtener el nuevo estado a partir de la transición
        estado_actual = afn.transiciones[estado_actual][caracter]
    
    # Verificar si el estado actual es un estado de aceptación
    if estado_actual in afn.estados_aceptacion:
       
        return f"La cadena '{cadena}' es válida en el AFN '{afn.nombre}'"
    else:
        return f"La cadena '{cadena}' no es válida en el AFN '{afn.nombre}'"