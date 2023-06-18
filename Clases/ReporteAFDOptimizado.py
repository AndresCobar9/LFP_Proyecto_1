import tkinter as tk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from PIL import Image
import Clases.AFDOptimizado

def generarDOT(estados, estados_aceptacion, transiciones, estado_inicial, nombre):
    dot = Digraph(nombre, filename=nombre, format='png')
    dot.attr(rankdir='LR', size='8,5')

    estados1 = set(estados).symmetric_difference(set(estados_aceptacion))
    estados2 = estados1.difference({estado_inicial})

    # Agregar estado inicial con triángulo
    dot.node(estado_inicial, shape='circle', color='red')

    for estado in estados2:
        dot.node(estado, shape='circle')

    for estado_aceptacion in estados_aceptacion:
        dot.node(estado_aceptacion, shape='doublecircle')

    for origen, transicion in transiciones.items():
        for etiqueta, destino in transicion.items():
            dot.edge(origen, destino, label=etiqueta)

    dot.render(view=False)


def generarPDF(estados, estados_aceptacion, transiciones, estado_inicial, nombre,afd):
    w, h = A4
    c = canvas.Canvas("ReporteAFDOptimizado_" + nombre + ".pdf", pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)

    # Calcular posición x para centrar el texto
    reporte_afd_text = "- Reporte Generado Sobre AFDOptimizado '" + nombre + "' -"
    reporte_afd_text_width = c.stringWidth(reporte_afd_text, "Helvetica", 22)
    reporte_afd_text_x = (w - reporte_afd_text_width) / 2

    c.drawString(reporte_afd_text_x, h - 30, reporte_afd_text)
    c.setFont('Helvetica', 12)
    c.drawString(30, h - 70, "Nombre del AFDOptimizado:  " + nombre)
    c.drawString(30, h - 90, "Estados:  " + str(estados))
    c.drawString(30, h - 110, "Estado inicial:  " + estado_inicial)
    c.drawString(30, h - 130, "Estados de aceptacion:  " + str(estados_aceptacion))
    # Generar una linea por cada elemento en el array de transiciones
    c.drawString(30, h - 150, "Listado de Transiciones:")
    x = 190  # Posición vertical inicial
    for transicion in transiciones:
        c.drawString(30, h - x + 20, "     - "+ transicion)
        x += 20  # Incrementar la posición vertical
        c.setFont('Helvetica', 12)

    image_path = nombre + ".png"
    image = Image.open(image_path)
    image_width, image_height = image.size
    image_x = (w - image_width) / 2
    image_y = 30  # Posición en el pie de la página

    Cadena = Clases.AFDOptimizado.generar_cadena_ejemplo(afd)
    print(Cadena)

    c.setFont('Helvetica', 12)

    # Ajustar las coordenadas para que las líneas de texto estén encima de la imagen
    c.drawString(30, image_y + image_height + 20, "------------------------------------------------------- Gráfica del AFDOptimizado -------------------------------------------------------")
    c.drawString(30, image_y + image_height + 40, "Cadena de ejemplo Generada Automaticamente: " + Cadena)

    # Dibujar la imagen en el pie de la página
    c.drawInlineImage(image_path, image_x, image_y, width=image_width, height=image_height)
    c.save()


def generarReporteAFDOptimizado(estados, estados_aceptacion, transiciones, transicionesN,estado_inicial, nombre,afd):
    print("test1")
    generarDOT(estados, estados_aceptacion, transiciones, estado_inicial,nombre)
    print("test2")
    generarPDF(estados, estados_aceptacion, transicionesN, estado_inicial, nombre,afd)
    return True
