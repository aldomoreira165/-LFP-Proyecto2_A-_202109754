
class LenguajeObjeto:
    
    def __init__ (self):
        self.nombre = None

    def generarHTML(self, contenedores, etiquetas, botones, textos, areasTexto, claves):
        with open('Salida/index.html', 'w') as archivo:
            archivo.write('<html>\n')
            archivo.write('<head>\n')
            archivo.write('<link href="prueba.css" rel="stylesheet" type="text/css"/>\n')
            archivo.write('</head>\n')
            archivo.write('<body>\n')
            
            for contenedor in contenedores:
                archivo.write(f'    <div id="{contenedor.identificador}">\n')
                archivo.write('     </div>\n')
                
            for etiqueta in etiquetas:
                archivo.write(f'    <label id="{etiqueta.identificador}">{etiqueta.texto}</label>\n')
                
            for boton in botones:
                archivo.write(f'    <input type="submit" id="{boton.identificador}" value="{boton.texto}" style="text-align:{boton.alineacion}"/>\n')
                
            for texto in textos:
                archivo.write(f'    <input type="text" id="{texto.identificador}" value="{texto.texto}" style="text-align:{texto.alineacion}"/>\n')
                
            for areaTexto in areasTexto:
                archivo.write(f'    <TEXTAREA id="{areaTexto.identificador}">{areaTexto.texto}</TEXTAREA>\n')
                
            for clave in claves:
                archivo.write(f'    <input type="password" id="{clave.identificador}" value="{clave.texto}" style="text-align:{clave.alineacion}"/>\n')
                
            archivo.write('</body>\n')
            archivo.write('</html\n')
            
    def generarCSS(self, contenedores, etiquetas, botones, textos, areasTexto, claves):
        with open('Salida/prueba.css', 'w') as archivo:
            
            for etiqueta in etiquetas:
                archivo.write(f'#{etiqueta.identificador}' + '{\n')
                archivo.write(f'color:rgb({etiqueta.colorLetra});\n')
                archivo.write('}\n')
            
    