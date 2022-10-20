import tkinter as tk
import sys
from tkinter import scrolledtext as st
from tkinter.font import BOLD
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from VentanaTokens import VentanaTokens
from VentanaErrores import VentanaErrores
from LenguajeObjeto import LenguajeObjeto
from Contenedor import Contenedor
from Etiqueta import Etiqueta
from Check import Check
from Boton import Boton
from Texto import Texto
from AreaTexto import AreaTexto
from Clave import Clave

class VentanaPrincipal:
    
    def __init__(self):
        #creacion de ventana
        self.ventana = tk.Tk()
        self.agregar_menu()
        self.scrolledtext1 = st.ScrolledText(self.ventana, width=70, height=35)
        self.scrolledtext1.grid(column=0, row=0, padx=20, pady=20)
        tk.Wm.title(self.ventana, f'Creador de páginas web')
        self.ventana.mainloop()
        
        #variables para el manejo de archivos a nivel global
        self.lista_tokens = []
        self.lista_errores = []
        self.archivo = None
        self.nombre_archivo = None
        
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
        menu_analisis.add_command(label='Generar Página Web', command=self.generar_pagina_web)
        barra_menus.add_cascade(menu=menu_analisis, label='Análisis')
        
        #cascada de menu tokens
        menu_tokens = tk.Menu(barra_menus, tearoff=False)
        menu_tokens.add_cascade(label='Ver Tokens', command=self.abrir_ventana_tokens)
        barra_menus.add_cascade(menu=menu_tokens, label='Tokens')
        
        #cascada de menu errores
        menu_errores = tk.Menu(barra_menus, tearoff=False)
        menu_errores.add_cascade(label='Ver Errores', command=self.abrir_ventana_errores)
        barra_menus.add_cascade(menu=menu_errores, label='Errores')
        
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
            self.archivo = open(self.nombre_archivo, 'w', encoding='utf-8')
            self.archivo.write(self.scrolledtext1.get('1.0', tk.END))
            self.archivo.close()
            mb.showinfo('información', 'El archivo se guardó correctamente')
        
    def guardar(self):
        self.archivo = open(self.nombre_archivo, 'w', encoding='utf-8')
        self.archivo.write(self.scrolledtext1.get('1.0', tk.END))
        self.archivo.close()
        mb.showinfo('información', 'El archivo se guardó correctamente')
    
    def abrir(self):
        #inicializando listas
        self.lista_tokens = []
        self.lista_errores = []
        
        self.nombre_archivo = fd.askopenfilename(title='Seleccione el archivo', filetypes=(('gpw file', '*.gpw'), ('todos los arhivos', '*.*')))
        if self.nombre_archivo != '':
            self.archivo = open(self.nombre_archivo, 'r', encoding='utf-8')
            contenido = self.archivo.read()
            self.archivo.close()
            self.scrolledtext1.delete('1.0', tk.END)
            self.scrolledtext1.insert('1.0', contenido)
            
    def abrir_ventana_tokens(self):
        ventana_tokens = VentanaTokens(self.lista_tokens)
        
    def abrir_ventana_errores(self):
        ventana_errores = VentanaErrores(self.lista_errores)
                 
    def generar_pagina_web(self):
        self.lista_tokens.clear()
        self.lista_errores.clear()
        
        #obteniendo contenido del archivo abierto
        self.archivo = open(self.nombre_archivo, 'r', encoding='utf-8')
        contenido = self.archivo.read()
        self.archivo.close()
        
        #realizando analisis lexico
        analizador_lexico = AnalizadorLexico(contenido)
        analizador_lexico.analizar()
        
        #obteniendo lista de tokens del analisis lexico
        self.lista_tokens += analizador_lexico.obtener_lista_tokens()
        
        #obteniendo lista de errores del analisis léxico
        self.lista_errores += analizador_lexico.obtener_lista_errores()

        tokens = []
        for i in range (len(self.lista_tokens)):
            tokens.append(self.lista_tokens[i])
    
        #creando analizador sintáctico y enviandole la lista de tokens
        analizador_sintactico = AnalizadorSintactico(tokens)
        analizador_sintactico.analizar()
        self.lista_errores += analizador_sintactico.obtener_lista_errores()
        
        if len(self.lista_errores) == 0:
            tk.messagebox.showinfo(message="Archivo compilado correctamente.", title="Éxito")
            
            #creando archivos de salida
            lista_etiquetas = []
            lista_botones = []
            lista_checks = []
            lista_radioBotones = []
            lista_textos = []
            lista_areasTexto = []
            lista_claves = []
            lista_contenedores = []
            for i in range(len(self.lista_tokens)):
                token = self.lista_tokens[i]
                
                #contenedores
                if token.numero == 3 and (token.lexema == 'Contenedor' or token.lexema == 'contenedor'):
                    nuevo_contenedor = Contenedor(self.lista_tokens[i+1].lexema, None, None, None)
                    lista_contenedores.append(nuevo_contenedor)
                    
                #etiquetas
                elif token.numero == 3 and (token.lexema == 'Etiqueta' or token.lexema == 'etiqueta'):
                    nueva_etiqueta = Etiqueta(self.lista_tokens[i+1].lexema, None, None, None)
                    
                    #buscando texto de etiqueta
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_etiqueta.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nueva_etiqueta.setTexto(self.lista_tokens[j+5].lexema)
                            else:
                                pass
                        else:
                            pass
                        
                    #buscando color de letra de etiqueta
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_etiqueta.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_etiqueta.setColorLetra(color)
                            else:
                                pass
                        else:
                            pass
                    
                    lista_etiquetas.append(nueva_etiqueta)
                    
                #botones
                elif token.numero == 3 and (token.lexema == 'Boton' or token.lexema == 'boton'):
                    nuevo_boton = Boton(self.lista_tokens[i+1].lexema, None, None)
                    
                    #buscando texto de boton
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_boton.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nuevo_boton.setTexto(self.lista_tokens[j+5].lexema)
                            else:
                                pass
                        else:
                            pass 
                        
                    #buscando alineacion de boton
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_boton.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nuevo_boton.setAlineacion(self.lista_tokens[j+4].lexema)
                            else:
                                pass
                        else:
                            pass
                        
                    lista_botones.append(nuevo_boton)
                    
                #texto 
                elif token.numero == 3 and (token.lexema == 'Texto' or token.lexema == 'texto'):
                    nuevo_texto = Texto(self.lista_tokens[i+1].lexema, None, None)
                    
                    #buscando texto de texto
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_texto.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nuevo_texto.setTexto(self.lista_tokens[j+5].lexema)
                            else:
                                pass
                        else:
                            pass 
                        
                    #buscando alineacion de texto
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_texto.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nuevo_texto.setAlineacion(self.lista_tokens[j+4].lexema)
                            else:
                                pass
                        else:
                            pass
                    
                    lista_textos.append(nuevo_texto)
                    
                elif token.numero == 3 and (token.lexema == 'AreaTexto' or token.lexema == 'areatexto'):
                    nueva_areatexto = AreaTexto(self.lista_tokens[i+1].lexema, None)
                    
                    #buscando texto de texto
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_areatexto.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nueva_areatexto.setTexto(self.lista_tokens[j+5].lexema)
                            else:
                                pass
                        else:
                            pass
                        
                    lista_areasTexto.append(nueva_areatexto)
                    
                #claves
                elif token.numero == 3 and (token.lexema == 'Clave' or token.lexema == 'clave'):
                    nueva_clave = Clave(self.lista_tokens[i+1].lexema, None, None)
                    
                    #buscando texto de clave
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_clave.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nueva_clave.setTexto(self.lista_tokens[j+5].lexema)
                            else:
                                pass
                        else:
                            pass 
                        
                    #buscando alineacion de clave
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_clave.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nueva_clave.setAlineacion(self.lista_tokens[j+4].lexema)
                            else:
                                pass
                        else:
                            pass
                        
                    lista_claves.append(nueva_clave)
                        
            lenguaje_objeto = LenguajeObjeto()
            lenguaje_objeto.generarCSS(lista_contenedores, lista_etiquetas, lista_botones, lista_textos, lista_areasTexto, lista_claves)
            lenguaje_objeto.generarHTML(lista_contenedores, lista_etiquetas, lista_botones, lista_textos, lista_areasTexto, lista_claves)
        else:
            tk.messagebox.showerror(message="El archivo contiene errores.", title="Error")
            
ventana = VentanaPrincipal()