

class AreaTexto:
    
    def __init__ (self, identificador, texto, alineacion, colorLetra, colorFondo, x, y, ancho, alto):
        self.identificador = identificador
        self.texto = texto
        self.alineacion = alineacion
        self.colorLetra = colorLetra
        self.colorFondo = colorFondo
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        
    def setTexto(self, texto):
        self.texto = texto
        
        
    def setAlineacion(self, alineacion):
        if alineacion == 'Centro':
            alineacion = 'Center'
        elif alineacion == 'Derecho':
            alineacion = 'Right'
        elif alineacion == 'Izquierdo':
            alineacion == 'Left'
            
        self.alineacion = alineacion
        
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