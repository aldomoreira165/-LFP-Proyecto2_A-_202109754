import tkinter as tk
import sys
import webbrowser
from tkinter import scrolledtext as st
from tkinter.font import BOLD
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from VentanaTokens import VentanaTokens
from VentanaErrores import VentanaErrores
from LenguajeObjeto import LenguajeObjeto
from Elementos.Contenedor import Contenedor
from Elementos.Etiqueta import Etiqueta
from Elementos.Check import Check
from Elementos.Boton import Boton
from Elementos.Texto import Texto
from Elementos.AreaTexto import AreaTexto
from Elementos.Clave import Clave
from Elementos.RadioBoton import RadioBoton

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

        #lista de tokens secundaria para enviar al analizador sintactico
        tokens = []
        for i in range (len(self.lista_tokens)):
            tokens.append(self.lista_tokens[i])
    
        #creando analizador sintáctico y enviandole la lista de tokens
        analizador_sintactico = AnalizadorSintactico(tokens)
        analizador_sintactico.analizar()
        self.lista_errores += analizador_sintactico.obtener_lista_errores() 
        
        if len(self.lista_errores) == 0:
            tk.messagebox.showinfo(message="Archivo compilado correctamente.", title="Éxito")
            #creando listas de los diferentes controles en el archivo de entrada
            lista_etiquetas = []
            lista_botones = []
            lista_checks = []
            lista_radioBotones = []
            lista_textos = []
            lista_areasTexto = []
            lista_claves = []
            lista_contenedores = []
            
            #analizando la lista de tokens para identificar sus propiedades y posicion para html y css
            for i in range(len(self.lista_tokens)):
                token = self.lista_tokens[i]
                #contenedores
                if token.numero == 3 and (token.lexema == 'Contenedor' or token.lexema == 'contenedor'):
                    nuevo_contenedor = Contenedor(self.lista_tokens[i+1].lexema, None, None, None, None, None, False)
                    
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_contenedor.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_contenedor.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nuevo_contenedor.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nuevo_contenedor.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nuevo_contenedor.setAncho(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'add' or self.lista_tokens[j+2].lexema == 'Add'):
                                #buscando elemento
                                nuevo_contenedor.setContenido(self.lista_tokens[j+4].lexema)

                    lista_contenedores.append(nuevo_contenedor)
                    
                #etiquetas
                elif token.numero == 3 and (token.lexema == 'Etiqueta' or token.lexema == 'etiqueta'):
                    nueva_etiqueta = Etiqueta(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None)
                    
                    #buscando texto de etiqueta
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_etiqueta.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nueva_etiqueta.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_etiqueta.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_etiqueta.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nueva_etiqueta.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nueva_etiqueta.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nueva_etiqueta.setAncho(self.lista_tokens[j+4].lexema)
                                  
                    lista_etiquetas.append(nueva_etiqueta)
                    
                #botones
                elif token.numero == 3 and (token.lexema == 'Boton' or token.lexema == 'boton'):
                    nuevo_boton = Boton(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None, None)
                    
                    #buscando texto de boton
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_boton.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nuevo_boton.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nuevo_boton.setAlineacion(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_boton.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_boton.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nuevo_boton.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nuevo_boton.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nuevo_boton.setAncho(self.lista_tokens[j+4].lexema)

                    lista_botones.append(nuevo_boton)
                    
                #texto 
                elif token.numero == 3 and (token.lexema == 'Texto' or token.lexema == 'texto'):
                    nuevo_texto = Texto(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None, None)
                    
                    #buscando texto de texto
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_texto.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nuevo_texto.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nuevo_texto.setAlineacion(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_texto.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_texto.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nuevo_texto.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nuevo_texto.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nuevo_texto.setAncho(self.lista_tokens[j+4].lexema)
                    
                    lista_textos.append(nuevo_texto)
                 
                #area de texto    
                elif token.numero == 3 and (token.lexema == 'AreaTexto' or token.lexema == 'areatexto'):
                    nueva_areatexto = AreaTexto(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None, None)
                    
                    #buscando texto de texto
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_areatexto.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nueva_areatexto.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nueva_areatexto.setAlineacion(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_areatexto.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_areatexto.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nueva_areatexto.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nueva_areatexto.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nueva_areatexto.setAncho(self.lista_tokens[j+4].lexema)
                                
                    lista_areasTexto.append(nueva_areatexto)
                    
                #claves
                elif token.numero == 3 and (token.lexema == 'Clave' or token.lexema == 'clave'):
                    nueva_clave = Clave(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None, None)
                    
                    #buscando texto de clave
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nueva_clave.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nueva_clave.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nueva_clave.setAlineacion(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_clave.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nueva_clave.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nueva_clave.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nueva_clave.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nueva_clave.setAncho(self.lista_tokens[j+4].lexema)

                    lista_claves.append(nueva_clave)
                    
                #check
                elif token.numero == 3 and (token.lexema == 'Check' or token.lexema == 'check'):
                    nuevo_check = Check(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None, None, None, None)
                    
                    #buscando propiedades
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_check.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nuevo_check.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nuevo_check.setAlineacion(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_check.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_check.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nuevo_check.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nuevo_check.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nuevo_check.setAncho(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setMarcada' or self.lista_tokens[j+2].lexema == 'setmarcada'):
                                nuevo_check.setMarcada(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setGrupo' or self.lista_tokens[j+2].lexema == 'setgrupo'):
                                nuevo_check.setGrupo(self.lista_tokens[j+4].lexema)

                    lista_checks.append(nuevo_check)
                    
                #radioboton
                elif token.numero == 3 and (token.lexema == 'RadioBoton' or token.lexema == 'radioboton'):
                    nuevo_radio = RadioBoton(self.lista_tokens[i+1].lexema, None, None, None, None, None, None, None, None, None, None)
                    
                    #buscando propiedades
                    for j in range(len(self.lista_tokens)):
                        token = self.lista_tokens[j]
                        if token.lexema == nuevo_radio.identificador:
                            if self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setTexto' or self.lista_tokens[j+2].lexema == 'settexto'):
                                nuevo_radio.setTexto(self.lista_tokens[j+5].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlineacion' or self.lista_tokens[j+2].lexema == 'setalineacion'):
                                nuevo_radio.setAlineacion(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorLetra' or self.lista_tokens[j+2].lexema == 'setcolorletra'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_radio.setColorLetra(color)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setColorFondo' or self.lista_tokens[j+2].lexema == 'setcolorfondo'):
                                color = self.lista_tokens[j+4].lexema + self.lista_tokens[j+5].lexema + self.lista_tokens[j+6].lexema + self.lista_tokens[j+7].lexema + self.lista_tokens[j+8].lexema
                                nuevo_radio.setColorFondo(color)
                            elif self.lista_tokens[j+2].tipo == 'Posicion' and (self.lista_tokens[j+2].lexema == 'setPosicion' or self.lista_tokens[j+2].lexema == 'setPosicion'):
                                nuevo_check.setPosicion(self.lista_tokens[j+4].lexema, self.lista_tokens[j+6].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAlto' or self.lista_tokens[j+2].lexema == 'setalto'):
                                nuevo_radio.setAlto(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setAncho' or self.lista_tokens[j+2].lexema == 'setancho'):
                                nuevo_radio.setAncho(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setMarcada' or self.lista_tokens[j+2].lexema == 'setmarcada'):
                                nuevo_radio.setMarcada(self.lista_tokens[j+4].lexema)
                            elif self.lista_tokens[j+2].tipo == 'Propiedad' and (self.lista_tokens[j+2].lexema == 'setGrupo' or self.lista_tokens[j+2].lexema == 'setgrupo'):
                                nuevo_radio.setGrupo(self.lista_tokens[j+4].lexema)

                    lista_radioBotones.append(nuevo_radio)
         
            #verificando los controles que estan en la pagina principal --this.add(ID)   
            for i in range(len(self.lista_tokens)):
                token = self.lista_tokens[i]
                if token.lexema == 'this' or token.lexema == 'This': 
                    if self.lista_tokens[i+2].lexema == 'add' or self.lista_tokens[i+2].lexema == 'Add':
                        nombre = self.lista_tokens[i+4].lexema
                        #buscando componente
                        #contenedores
                        for con in lista_contenedores:
                            if con.identificador == nombre:
                                con.setPagina()
                                
            for lista in lista_contenedores:
                print(lista.identificador, lista.contieneA)
                
            #asignando objetos contenidos dentro de contenedor
            for c in lista_contenedores:
                if len(c.contieneA) > 0:
                    for idControl in c.contieneA:
                        for i in range(len(lista_contenedores)):
                            if lista_contenedores[i].identificador == idControl:
                                idControl = lista_contenedores[i]
                                break
                        """for i in range(len(lista_botones)):
                            if lista_botones[i].identificador == idControl:
                                idControl = lista_botones[i]
                                break"""
                  
            lenguaje_objeto = LenguajeObjeto()
            lenguaje_objeto.generarCSS(lista_contenedores, lista_etiquetas, lista_botones, lista_textos, lista_areasTexto, lista_claves, lista_checks, lista_radioBotones)
            lenguaje_objeto.generarHTML(lista_contenedores, lista_etiquetas, lista_botones, lista_textos, lista_areasTexto, lista_claves, lista_checks, lista_radioBotones)
        else:
            tk.messagebox.showerror(message="El archivo contiene errores.", title="Error")
              
ventana = VentanaPrincipal()