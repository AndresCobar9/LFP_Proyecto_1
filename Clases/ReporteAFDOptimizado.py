import tkinter as tk
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from PIL import Image
import Clases.AFDOptimizado

def generarDOT(afdsOptimizados):
    for afdOptimizado in afdsOptimizados:
        dot = Digraph(afdOptimizado.nombre, filename=afdOptimizado.nombre, format='png')
        dot.attr(rankdir='LR', size='8,5')

        estados1 = set(afdOptimizado.estados).symmetric_difference(set(afdOptimizado.estados_aceptacion))
        estados2 = estados1.difference({afdOptimizado.estado_inicial})

        # Agregar estado inicial con triángulo
        dot.node(afdOptimizado.estado_inicial, shape='circle', color='red')

        for estado in estados2:
            dot.node(estado, shape='circle')

        for estado_aceptacion in afdOptimizado.estados_aceptacion:
            dot.node(estado_aceptacion, shape='doublecircle')

        for origen, transicion in afdOptimizado.transiciones.items():
            for etiqueta, destino in transicion.items():
                dot.edge(origen, destino, label=etiqueta)

        dot.render(view=False)


def generarPDF(afdsOptimizados):
    w, h = A4
    c = canvas.Canvas("ReporteAFDOptimizado.pdf", pagesize=A4)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)

    for afdOptimizado in afdsOptimizados:
        c.addPageLabel(1)  # Nueva página para cada AFD optimizado
        c.setFont('Helvetica', 22)

        # Calcular posición x para centrar el texto
        reporte_afd_text = "- Reporte Generado Sobre AFDOptimizado '" + afdOptimizado.nombre + "' -"
        reporte_afd_text_width = c.stringWidth(reporte_afd_text, "Helvetica", 22)
        reporte_afd_text_x = (w - reporte_afd_text_width) / 2

        c.drawString(reporte_afd_text_x, h - 30, reporte_afd_text)
        c.setFont('Helvetica', 12)
        c.drawString(30, h - 70, "Nombre del AFDOptimizado:  " + afdOptimizado.nombre)
        c.drawString(30, h - 90, "Estados:  " + ", ".join(afdOptimizado.estados))
        c.drawString(30, h - 110, "Estado inicial:  " + afdOptimizado.estado_inicial)
        c.drawString(30, h - 130, "Estados de aceptacion:  " + ", ".join(afdOptimizado.estados_aceptacion))
        # Generar una línea por cada elemento en el diccionario de transiciones
        c.drawString(30, h - 150, "Listado de Transiciones:")
        x = 190  # Posición vertical inicial
        for origen, transiciones in afdOptimizado.transiciones.items():
            for entrada, destino in transiciones.items():
                transicion_str = f"{origen}, {entrada}, {destino}"
                c.drawString(30, h - x + 20, "     - " + transicion_str)
                x += 20  # Incrementar la posición vertical
                c.setFont('Helvetica', 12)

        image_path = afdOptimizado.nombre + ".png"
        image = Image.open(image_path)
        image_width, image_height = image.size
        image_x = (w - image_width) / 2
        image_y = 30  # Posición en el pie de la página

        c.setFont('Helvetica', 12)

        # Ajustar las coordenadas para que las líneas de texto estén encima de la imagen
        c.drawString(30, image_y + image_height + 20, "------------------------------------------------------- Gráfica del AFDOptimizado -------------------------------------------------------")

        # Dibujar la imagen en el pie de la página
        c.drawInlineImage(image_path, image_x, image_y, width=image_width, height=image_height)
        c.showPage()

    c.save()


def generarReporteAFDOptimizado(afdsOptimizados):
    generarDOT(afdsOptimizados)
    generarPDF(afdsOptimizados)
    return True
