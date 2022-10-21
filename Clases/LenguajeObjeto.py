
class LenguajeObjeto:
    
    def __init__ (self):
        self.nombre = None

    def generarHTML(self, contenedores, etiquetas, botones, textos, areasTexto, claves):
        with open('../Salida/index.html', 'w') as archivo:
            archivo.write('<html>\n')
            archivo.write('<head>\n')
            archivo.write('<link href="prueba.css" rel="stylesheet" type="text/css"/>\n')
            archivo.write('</head>\n')
            archivo.write('<body>\n')
            
            for contenedor in contenedores:
                #agregando al html los div externos
                if contenedor.enPagina == True:
                    archivo.write(f'    <div id="{contenedor.identificador}">\n')
                    if len(contenedor.contieneA) > 0:
                        for contenido in contenedor.contieneA:
                                archivo.write(f'        <div id="{contenido}">\n')  
                                archivo.write('         </div>\n')
                        archivo.write('     </div>\n')
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
        with open('../Salida/prueba.css', 'w') as archivo:
            
            for etiqueta in etiquetas:
                archivo.write(f'#{etiqueta.identificador}' + '{\n')
                archivo.write('position:absolute;\n')
                archivo.write(f'top:{etiqueta.y}px;\n')
                archivo.write(f'left:{etiqueta.x}px;\n')
                archivo.write(f'width:{etiqueta.ancho}px;\n')
                archivo.write(f'height:{etiqueta.alto}px;\n')
                archivo.write(f'color:rgb({etiqueta.colorLetra});\n')
                archivo.write(f'background-color:rgb({etiqueta.colorFondo});\n')
                archivo.write(f'font-size:12px;\n')
                archivo.write('}\n')
                
            for contenedor in contenedores:
                archivo.write(f'#{contenedor.identificador}' + '{\n')
                archivo.write('position:absolute;\n')
                archivo.write(f'top:{contenedor.y}px;\n')
                archivo.write(f'left:{contenedor.x}px;\n')
                archivo.write(f'width:{contenedor.ancho}px;\n')
                archivo.write(f'height:{contenedor.alto}px;\n')
                archivo.write(f'background-color:rgb({contenedor.colorFondo});\n')
                archivo.write(f'font-size:12px;\n')
                archivo.write('}\n')
                
            for texto in textos:
                archivo.write(f'#{texto.identificador}' + '{\n')
                archivo.write('position:absolute;\n')
                archivo.write(f'top:{texto.y}px;\n')
                archivo.write(f'left:{texto.x}px;\n')
                archivo.write(f'width:{texto.ancho}px;\n')
                archivo.write(f'height:{texto.alto}px;\n')
                archivo.write(f'color:rgb({texto.colorLetra});\n')
                archivo.write(f'background-color:rgb({texto.colorFondo});\n')
                archivo.write(f'font-size:12px;\n')
                archivo.write('}\n')
                
            for clave in claves:
                archivo.write(f'#{clave.identificador}' + '{\n')
                archivo.write('position:absolute;\n')
                archivo.write(f'top:{clave.y}px;\n')
                archivo.write(f'left:{clave.x}px;\n')
                archivo.write(f'width:{clave.ancho}px;\n')
                archivo.write(f'height:{clave.alto}px;\n')
                archivo.write(f'color:rgb({clave.colorLetra});\n')
                archivo.write(f'background-color:rgb({clave.colorFondo});\n')
                archivo.write(f'font-size:12px;\n')
                archivo.write('}\n')
                
            for boton in botones:
                archivo.write(f'#{boton.identificador}' + '{\n')
                archivo.write('position:absolute;\n')
                archivo.write(f'top:{boton.y}px;\n')
                archivo.write(f'left:{boton.x}px;\n')
                archivo.write(f'width:{boton.ancho}px;\n')
                archivo.write(f'height:{boton.alto}px;\n')
                archivo.write(f'color:rgb({boton.colorLetra});\n')
                archivo.write(f'background-color:rgb({boton.colorFondo});\n')
                archivo.write(f'font-size:12px;\n')
                archivo.write('}\n')
                
            for areaTexto in areasTexto:
                archivo.write(f'#{areaTexto.identificador}' + '{\n')
                archivo.write('position:absolute;\n')
                archivo.write(f'top:{areaTexto.y}px;\n')
                archivo.write(f'left:{areaTexto.x}px;\n')
                archivo.write(f'width:{areaTexto.ancho}px;\n')
                archivo.write(f'height:{areaTexto.alto}px;\n')
                archivo.write(f'color:rgb({areaTexto.colorLetra});\n')
                archivo.write(f'background-color:rgb({areaTexto.colorFondo});\n')
                archivo.write(f'font-size:12px;\n')
                archivo.write('}\n')
            
    