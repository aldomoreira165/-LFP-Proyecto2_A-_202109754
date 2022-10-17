from Token import Token
from Error import Error

class AnalizadorLexico():
    
    def __init__(self, contenido):
        self.contenido = contenido
        self.lista_tokens = []
        self.lista_errores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0
        self.reservadas = ['controles', 'propiedades', 'colocacion', 'colocación']
        self.controles = ['etiqueta', 'boton', 'check', 'radioboton', 'texto', 'areatexto', 'clave', 'contenedor']
        self.propiedades = ['id', 'setcolorletra', 'settexto', 'setalineacion', 'setcolorfondo', 'setmarcada', 'setgrupo', 'setancho', 'setalto']
        self.colocaciones = ['setposicion', 'add']         
        
    def agregar_token(self, numero, tipo, lexema):
        self.lista_tokens.append(Token(numero, tipo, lexema))
        self.buffer = ''
        
    def agregar_error(self, tipo, linea, columna, tokenEsperado, caracter):
        self.lista_errores.append(Error(tipo, linea, columna, tokenEsperado, f'Caracter {caracter}', ))
     
    #estados del dfa    
    def s0(self, caracter):
        #estado S0
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter == ';':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        elif caracter == '.':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        elif caracter == ',':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        elif caracter == '(':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        elif caracter == ')':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        elif caracter == '>':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        elif caracter == '<':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        elif caracter == '!':
            self.estado = 11
            self.buffer += caracter
            self.columna += 1
        elif caracter == '"':
            self.estado = 12
            self.buffer += caracter
            self.columna += 1
        elif caracter == '$':
            pass
        else:
            self.agregar_error('Léxico', self.linea, self.columna, '<, Letra, ;', caracter)
            self.columna += 1
            
    def s1(self, caracter):
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 13
            self.buffer += caracter
            self.columna += 1
        else:
            if self.buffer.lower() in self.reservadas:
                self.agregar_token(1, 'Reservada', self.buffer)
            elif self.buffer.lower() in self.propiedades:
                self.agregar_token(2, 'Propiedad', self.buffer)
            elif self.buffer.lower() in self.controles:
                self.agregar_token(3, 'Control', self.buffer)
            elif self.buffer.lower() in self.colocaciones:
                self.agregar_token(4, 'Posicion', self.buffer)
            else:
                self.agregar_token(14, 'Identificador', self.buffer)
            self.estado = 0
            self.i -= 1
            
    def s2(self, caracter):
        self.agregar_token(4, 'Punto y coma', self.buffer)
        self.estado = 0
        self.i -= 1
            
    def s3(self, caracter):
        if caracter.isdigit():
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(5, 'Valor', self.buffer)
            self.estado = 0
            self.i -= 1
            
    def s4(self, caracter):
        self.agregar_token(6, 'Punto', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s5(self, caracter):
        self.agregar_token(7, 'Coma', self.buffer)
        self.estado = 0
        self.i -= 1
    
    def s6(self, caracter):
        self.agregar_token(8, 'Paréntesis izquierdo', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s7(self, caracter):
        self.agregar_token(9, 'Paréntesis derecho', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s8(self, caracter):
        self.agregar_token(10, 'Mayor que', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s9(self, caracter):
        self.agregar_token(11, 'Menor que', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s10(self, caracter):
        self.agregar_token(12, 'Guion', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s11(self, caracter):
        self.agregar_token(13, 'Admiración', self.buffer)
        self.estado = 0
        self.i -= 1
        
    def s12(self, caracter):
        self.agregar_token(14, 'Comillas', self.buffer)
        self.estado = 0
        self.i -= 1
            
    def s13(self, caracter):
        if caracter.isalpha() or caracter.isdigit():
            self.estado = 13
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(14, 'Identificador', self.buffer)
            self.estado = 0
            self.i -= 1
     
    #analizando cadenas del archivo         
    def analizar(self):
        self.lista_errores = []
        self.lista_tokens = []
        lineas = self.contenido.split('\n')
        
        for linea in lineas:
            self.columna = 0
            #eliminando tabulaciones
            linea_tabulacion = linea.replace('\t', '')
            #eliminando espacios
            palabras = linea_tabulacion.split(' ')
            
            #recorriendo palabras de la linea
            for cadena in palabras:
                self.buffer = ''
                self.estado = 0
                self.i = 0
                cadena += '$'
                while self.i < len(cadena):
                    if self.estado == 0:
                        self.s0(cadena[self.i])
                    elif self.estado == 1:
                        self.s1(cadena[self.i])
                    elif self.estado == 2:
                        self.s2(cadena[self.i])
                    elif self.estado == 3:
                        self.s3(cadena[self.i])
                    elif self.estado == 4:
                        self.s4(cadena[self.i])
                    elif self.estado == 5:
                        self.s5(cadena[self.i])
                    elif self.estado == 6:
                        self.s6(cadena[self.i])
                    elif self.estado == 7:
                        self.s7(cadena[self.i])
                    elif self.estado == 8:
                        self.s8(cadena[self.i])
                    elif self.estado == 9:
                        self.s9(cadena[self.i])
                    elif self.estado == 10:
                        self.s10(cadena[self.i])
                    elif self.estado == 11:
                        self.s11(cadena[self.i])
                    elif self.estado == 12:
                        self.s12(cadena[self.i])
                    elif self.estado == 13:
                        self.s13(cadena[self.i])
                    self.i += 1
            self.linea += 1     
     
    #retornando lista de tokens y errores       
    def obtener_lista_tokens(self):
        return self.lista_tokens
        
    def obtener_lista_errores(self):
        return self.lista_errores
        
        
        