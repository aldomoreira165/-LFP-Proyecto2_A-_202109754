import tkinter as tk
from tkinter import ttk

class VentanaTokens:
    
    def __init__(self, lista_tokens):
        self.lista_tokens = lista_tokens
        self.ventana = tk.Tk()
        self.ventana.geometry('595x400')
        self.generar_tabla_tokens()
    
    def generar_tabla_tokens(self):
        #creando encabezado de tabla
        tabla = ttk.Treeview(self.ventana, columns=('#0','#1'))
        tabla.grid(row=1, column=0, columnspan=2)
        tabla.heading('#0', text = 'Número')
        tabla.heading('#1', text = 'Tipo')
        tabla.heading('#2', text = 'Lexema')
        
        #llenando la tabla
        for token in self.lista_tokens:
            tabla.insert('', 0, text=token.numero, values=(token.tipo, token.lexema))