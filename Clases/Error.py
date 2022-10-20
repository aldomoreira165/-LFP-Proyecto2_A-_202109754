
class Error:
    
    def __init__(self, tipo, linea, columna, tokenEsperado, descripcion):
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.tokenEsperado = tokenEsperado
        self.descripcion = descripcion
        