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

    def ejecutar(self):
        #definiendo el lenguaje 
        palabras_reservadas = {'controles':'reservada', 'propiedades':'reservada', 'colocacion':'reservada'}
        controles = {'etiqueta':'control', 'boton':'control', 'check':'control', 'radioboton':'control', 'texto':'control', 'areatexto':'control', 'clave':'control', 'contenedor':'contro'}
        
        #contador de lineas en el contenido del archivo
        contador_lineas = 0
        
        lineas_contenido = self.contenido.split('\n')
        for linea_contenido in lineas_contenido:
            contador_lineas += 1
            linea_contenido.replace('\t', '')
            
            print('Linea', contador_lineas, linea_contenido)
            linea_sin_tabulacion = linea_contenido.replace('\t','')
            tokens = linea_sin_tabulacion.split(' ')
            print('Los tokens son ', tokens)
            print(' ')
            
        