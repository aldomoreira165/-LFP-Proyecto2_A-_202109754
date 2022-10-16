import tkinter as tk
import sys
from tkinter import scrolledtext as st
from tkinter.font import BOLD
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from AnalizadorLexico import AnalizadorLexico
from VentanaTokens import VentanaTokens

class VentanaPrincipal:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.agregar_menu()
        self.scrolledtext1 = st.ScrolledText(self.ventana, width=50, height=20)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        tk.Wm.title(self.ventana, f'Creador de páginas web')
        self.ventana.mainloop()
    
    def agregar_menu(self):
        barra_menus = tk.Menu(self.ventana)
        #cascada de menu archivo
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label='Nuevo', command=self.nuevo)
        menu_archivo.add_command(label='Abrir', command=self.abrir)
        menu_archivo.add_command(label='Guardar', command=self.guardar)
        menu_archivo.add_command(label='Guardar Como', command=self.guardar_como)
        menu_archivo.add_command(label='Salir', command=self.salir)
        barra_menus.add_cascade(menu=menu_archivo, label='Archivo')
        
        #cascada de menu analisis
        menu_analisis = tk.Menu(barra_menus, tearoff=False)
        menu_analisis.add_command(label='Generar Página Web', command=self.salir)
        barra_menus.add_cascade(menu=menu_analisis, label='Análisis')
        
        #cascada de menu tokens
        menu_tokens = tk.Menu(barra_menus, tearoff=False)
        menu_tokens.add_cascade(label='Ver Tokens', command=self.abrir_ventana_tokens)
        barra_menus.add_cascade(menu=menu_tokens, label='Tokens')
        
        #cascada de menu errores
        menu_errores = tk.Menu(barra_menus, tearoff=False)
        menu_errores.add_cascade(label='Ver Errores')
        
        self.ventana.config(menu=barra_menus, bg='#8FEBD6')

    def salir(self):
        sys.exit(0)
        
    def nuevo(self):
        respuesta = mb.askquestion(title='Guardar', message='¿Desea guardar el archivo?')
        
        if respuesta == 'yes':
            self.guardar_como()
        else:
            pass
        self.scrolledtext1.delete('1.0', tk.END)
        
        
    def guardar_como(self):
        self.nombre_archivo = fd.asksaveasfilename(title = 'Guardar como', filetypes=(('gpw file', '*.gpw'), ('todos los archivos', '*.*')))
        if self.nombre_archivo != '':
            archivo = open(self.nombre_archivo, 'w', encoding='utf-8')
            archivo.write(self.scrolledtext1.get('1.0', tk.END))
            archivo.close()
            mb.showinfo('información', 'El archivo se guardó correctamente')
        
    def guardar(self):
        archivo = open(self.nombre_archivo, 'w', encoding='utf-8')
        archivo.write(self.scrolledtext1.get('1.0', tk.END))
        archivo.close()
        mb.showinfo('información', 'El archivo se guardó correctamente')
    
    def abrir(self):
        self.nombre_archivo = fd.askopenfilename(title='Seleccione el archivo', filetypes=(('gpw file', '*.gpw'), ('todos los arhivos', '*.*')))
        if self.nombre_archivo != '':
            archivo = open(self.nombre_archivo, 'r', encoding='utf-8')
            global contenido
            contenido = archivo.read()
            archivo.close()
            self.scrolledtext1.delete('1.0', tk.END)
            self.scrolledtext1.insert('1.0', contenido)
            
    def abrir_ventana_tokens(self):
        ventana_tokens = VentanaTokens()
        
                 
    def generar_pagina_web(self):
        #realizando analisis lexico
        analizador_lexico = AnalizadorLexico(contenido)
        analizador_lexico.analizar()
        
        
        
        
ventana = VentanaPrincipal()