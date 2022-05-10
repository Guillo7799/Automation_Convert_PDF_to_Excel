from re import A
import pdftables_api
import os

#Asignación de ruta para analziar
pdf_directory = 'Directory_Path'

#Listar carpetas y archivos del directorio declarado
archivos = os.listdir(pdf_directory)

archivos_convertibles=[]
for fichero in archivos:
    #Condicional para verificar que el archivo cumpla con el formato pdf
    if os.path.isfile(os.path.join(pdf_directory,fichero)) and fichero.endswith('.pdf'):
        archivos_convertibles.append(fichero)        
        
        #Uso de API de conversión de PDFTables
        conversion= pdftables_api.Client('APY KEY')

        #Asignación de ruta de archivo y nombre del archivo
        conversion.xlsx_multiple(fichero,fichero.join("_excel"))

        #Impresión de mensaje exitoso
        print("Documento -- "+fichero+"-- convertido exitosamente!!")
    else:
        #Impresión de mensaje de archivos no convertibles        
        print("Documento --"+fichero+"-- no convertible")

#Comprobación en consola de archivos escaneados y convertidos
print("Directorios/Ficheros escaneados: ")
print(archivos_convertibles)