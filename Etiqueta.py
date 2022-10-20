
class Etiqueta:
    
    def __init__ (self, identificador, colorLetra, texto, colorFondo):
        self.identificador = identificador
        self.colorLetra = colorLetra
        self.texto = texto
        self.colorFondo = colorFondo
        
        
    def setTexto(self, texto):
        self.texto = texto
        
    def setColorLetra(self, colorLetra):
        self.colorLetra = colorLetra