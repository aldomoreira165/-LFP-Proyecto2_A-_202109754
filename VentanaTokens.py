import tkinter as tk
from tkinter import ttk

class VentanaTokens:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('450x400')
        self.generar_tabla()
    
    def generar_tabla(self):
        #creando encabezado de tabla
        tabla = ttk.Treeview(self.ventana, columns=('#0','#1','#2'))
        tabla.grid(row=1, column=0, columnspan=2)
        tabla.heading('#0', text = 'Número')
        tabla.heading('#1', text = 'Tipo')
        tabla.heading('#2', text = 'Lexema')
        