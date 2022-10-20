
class Contenedor:
    
    def __init__ (self, identificador, ancho, alto, colorFondo, x, y):
        self.identificador = identificador
        self.ancho = ancho
        self.alto = alto
        self.colorFondo = colorFondo
        self.x = x
        self.y = y
        
    def setColorFondo(self, colorFondo):
        self.colorFondo = colorFondo
        
    def setPosicion(self, x, y):
        self.x = x
        self.y = y
        
    def setAncho(self, ancho):
        self.ancho = ancho
        
    def setAlto(self, alto):
        self.alto = alto
    