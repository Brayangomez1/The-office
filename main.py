print "Brayan Eduardo Gomez Lopez 1651723"
import os
mi ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("la carpeta ya existe")
    else:
         os.mkdir(mi ubicacion + "\\modulos")
         archivo = open('./modulos/prueba.txt','w' )
         archivo.write('hola mundo')
         archivo.close()