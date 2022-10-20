
class Clave:
    
    def __init__ (self, identificador, texto, alineacion):
        self.identificador = identificador
        self.texto = texto
        self.alineacion = alineacion
        
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