
class Error:
    
    def __init__(self, tipo, linea, columna, descripcion):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.descripcion = descripcion
        