import tkinter as tk
from tkinter import ttk

class VentanaErrores:
    
    def __init__(self, lista_errores):
        self.lista_errores = lista_errores
        self.ventana = tk.Tk()
        self.ventana.geometry('1000x400')
        self.generar_tabla_errores()
    
    def generar_tabla_errores(self):
        #creando encabezado de tabla
        tabla = ttk.Treeview(self.ventana, columns=('#0','#1', '#2', '#3'))
        tabla.grid(row=1, column=0, columnspan=2)
        tabla.heading('#0', text = 'Tipo')
        tabla.heading('#1', text = 'Línea')
        tabla.heading('#2', text = 'Columna')
        tabla.heading('#3', text = 'Componente lexico esperado')
        tabla.heading('#4', text = 'Descripción')
        
        #llenando la tabla
        for error in self.lista_errores:
            tabla.insert('', 0, text=error.tipo, values=(error.linea, error.columna, error.tokenEsperado, error.descripcion))