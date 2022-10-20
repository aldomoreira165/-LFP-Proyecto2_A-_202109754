
class Etiqueta:
    
    def __init__ (self, identificador, colorLetra, texto, colorFondo, x, y, ancho, alto):
        self.identificador = identificador
        self.colorLetra = colorLetra
        self.texto = texto
        self.colorFondo = colorFondo
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        
    def setTexto(self, texto):
        self.texto = texto
        
    def setColorLetra(self, colorLetra):
        self.colorLetra = colorLetra
        
    def setColorFondo(self, colorFondo):
        self.colorFondo = colorFondo
        
    def setPosicion(self, x, y):
        self.x = x
        self.y = y
        
    def setAncho(self, ancho):
        self.ancho = ancho
        
    def setAlto(self, alto):
        self.alto = alto