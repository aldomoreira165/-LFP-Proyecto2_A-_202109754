from distutils.log import error
from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexico():
    
    def __init__(self):
        self.lista_tokens = []
        self.lista_errores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0
        
    def agregar_token(self, caracter, linea, columna, token):
        self.lista_tokens.append(Token(caracter, linea, columna, token))
        self.buffer = ''
        
    def agregar_error(self, caracter, linea, columna):
        self.lista_errores.append(Error(f'Caracter {caracter} no reconocido en el lenguaje.', linea, columna))
        
    def s0(self, caracter):
        #estado S0
        if caracter == '<':
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isalpha():
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == ';':
            self.estado = 3
            self.buffer += caracter 
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s1(self, caracter):
        if caracter == '!':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s2(self, caracter):
        if caracter.isalpha():
            self.estado = 2
            self.buffer += caracter
            self.columna += 1
        elif caracter == '-':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(2, 'Componente/ID', self.buffer)
            self.estado = 0
            self.i -= 1
            
    def s3(self, caracter):
        self.agregar_token(3, 'Punto y coma', self.buffer)
        self.estado = 0
            
    def s4(self, caracter):
        if caracter == '-':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s5(self, caracter):
        if caracter == '-':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s6(self, caracter):
        if caracter == '-':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s7(self, caracter):
        if caracter == '>':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s8(self, caracter):
        if caracter.isalpha():
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_error(caracter, self.linea, self.columna)
            self.i -= 1
            
    def s9(self, caracter):
        self.agregar_token(4, 'Cierre', self.buffer)
        self.estado = 0
            
    def s10(self, caracter):
        if caracter.isalpha():
            self.estado = 10
            self.buffer += caracter
            self.columna += 1
        else:
            self.agregar_token(1, 'Apertura', self.buffer)
            self.estado = 0
            self.i -= 1
            
    def analizar(self, cadena):
        self.lista_errores = []
        self.lista_tokens = []
        self.i = 0
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
            
            self.i += 1
            
    def imprimir_tokens(self):
        x = PrettyTable()
        x.field_names = ['Numero', 'Tipo', 'Lexema']
        for token in self.lista_tokens:
            x.add_row([token.numero, token.tipo, token.lexema])
        print(x)
        
    def imprimir_errores(self):
        x = PrettyTable()
        x.field_names = ['Descripcion', 'Linea', 'Columna']
        for error_ in self.lista_errores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)
        
        
        