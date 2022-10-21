
class Check:
    
    def __init__ (self, identificador, texto, marcada, grupo, alineacion, colorLetra, colorFondo, x, y, ancho, alto):
        self.identificador = identificador
        self.texto = texto
        self.marcada = marcada
        self.grupo = grupo
        self.alineacion = alineacion
        self.colorLetra = colorLetra
        self.colorFondo = colorFondo
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        
    def setMarcada(self, marcada):
        if marcada.lower() == 'true':
            self.marcada = 'checked'
        else:
            self.marcada = ''
                    
    def setTexto(self, texto):
        self.texto = texto
        
    def setGrupo(self, grupo):
        self.grupo = grupo
        
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