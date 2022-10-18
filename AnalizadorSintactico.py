from Error import Error

class AnalizadorSintactico:
    
    def __init__ (self, tokens):
        self.tokens = tokens
        self.lista_errores = []
           
    def agregar_error(self, tipo, linea, columna, tokenEsperado, descripcion):
        self.lista_errores.append(Error(tipo, linea, columna, tokenEsperado, descripcion))
        
    def sacar_token(self):
        #saca el primer token y lo quita de la lista
        try:
            return self.tokens.pop(0)
        except:
            return None
        
    def observar_token(self):
        #verifique el token más próximo
        try:
            return self.tokens[0]
        except:
            return None
        
    def analizar(self):
        self.S()
        
    def S(self):
        self.INICIO()
        
    def INICIO(self):
        #observar el primer elemento para decidir a donde ir 
        temporal = self.observar_token()
        if temporal is None:
            self.agregar_error('Sintáctico', 0, 0, 'Apertura', 'Fin de archivo')
        elif temporal.numero == 11:
            self.ABRIR_AREA()
        else:
            self.agregar_error('Sintáctico', 0, 0, 'Apertura', temporal.caracter)
            
    def ABRIR_AREA(self):
        #verifica que se abra un area (controles, propiedades, colocacion)
        token = self.sacar_token()
        if token.numero == 11:
            token = self.sacar_token()
            if token is None:
                self.agregar_error('Sintáctico', 0, 0, '!', 'Final de archivo')
                return
            elif token.numero == 13:
                token = self.sacar_token()
                if token is None:
                    self.agregar_error('Sintáctico', 0, 0, '-', 'Final de archivo')
                    return
                elif token.numero == 12:
                    token = self.sacar_token()
                    if token is None:
                        self.agregar_error('Sintáctico', 0, 0, '-', 'Final de archivo')
                        return
                    elif token.numero == 12:
                        token = self.sacar_token()
                        if token is None:
                            self.agregar_error('Sintáctico', 0, 0, 'Reservada', 'Final de archivo')
                            return
                        elif token.numero == 1:
                            #variable global para indicar al analizador dentro de que etiqueta está
                            global etiqueta
                            etiqueta = token.lexema
                            self.INSTRUCCION()
                        else:
                            self.agregar_error('Sintáctico', 0, 0, 'Reservada', token.lexema)
                    else:
                        self.agregar_error('Sintáctico', 0, 0, '-', token.lexema)
                else:
                    self.agregar_error('Sintáctico', 0, 0, '-', token.lexema)
            else:
                self.agregar_error('Sintáctico', 0, 0, '!', token.lexema)
        else:
            self.agregar_error('Sintáctico', 0, 0, '<', token.lexema)
             
    def INSTRUCCION(self):
        temporal = self.observar_token()
        if temporal is None:
            self.agregar_error('Sintáctico', 0, 0, 'Cierre | Instrucción', 'Fin de archivo')
        elif temporal.numero == 3:
            self.INSTRUCCION_CONTROLES()
        elif temporal.numero == 14 and etiqueta == 'propiedades':
            self.INSTRUCCION_PROPIEDADES()
        elif temporal.numero == 14 and etiqueta == 'colocacion':
            print('Estás dentro de la etiqueta colocacion')
            #self.INSTRUCCION_COLOCACION() 
        elif temporal.numero == 1:
            self.CERRAR_AREA()
        else:
            self.agregar_error('Sintáctico', 0, 0, 'Cierre | Instrucción', temporal.lexema)
          
    def INSTRUCCION_CONTROLES(self):
        token = self.sacar_token()
        if token.numero == 3:
            token = self.sacar_token()
            if token is None:
                self.agregar_error('Sintáctico', 0, 0, ID, 'Final de archivo')
            elif token.numero == 14:
                token = self.sacar_token()
                if token is None:
                    self.agregar_error('Sintáctico', 0, 0, ';', 'Final de archivo')
                elif token.numero == 4:
                    self.INSTRUCCION()
                else:
                    self.agregar_error('Sintáctico', 0, 0, ';', token.lexema)
            else:
                self.agregar_error('Sintáctico', 0, 0, 'ID', token.lexema)
        else:
            self.agregar_error('Sintáctico', 0, 0, 'Control', token.lexema)
            
    def INSTRUCCION_PROPIEDADES(self):
        pass
            
    def INSTRUCCION_COLOCACION(self):
        pass
    
    def CERRAR_AREA(self):
        token = self.sacar_token()
        if token.numero == 1:
            token = self.sacar_token()
            if token is None:
                self.agregar_error('Sintáctico', 0, 0, '-', 'Final de archivo')
            elif token.numero == 12:
                token = self.sacar_token()
                if token is None:
                    self.agregar_error('Sintáctico', 0, 0, '-', 'Final de archivo')
                elif token.numero == 12:
                    token = self.sacar_token()
                    if token is None:
                        self.agregar_error('Sintáctico', 0, 0, '>', 'Final de archivo')
                    elif token.numero == 10:
                        token = self.observar_token()
                        if token is None:
                            print('Archivo correcto')
                        else:
                            self.INICIO()
                    else: 
                       self.agregar_error('Sintáctico', 0, 0, '>', token.lexema) 
                else:
                    self.agregar_error('Sintáctico', 0, 0, '-', token.lexema)
            else:
                self.agregar_error('Sintáctico', 0, 0, '-', token.lexema)
        else:
            self.agregar_error('Sintáctico', 0, 0, 'Reservada', token.lexema)
                 
    def obtener_lista_errores(self):
        return self.lista_errores