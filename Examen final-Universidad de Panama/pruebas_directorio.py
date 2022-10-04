import os
import zipfile
import shutil#para comprimir un directorio con archivos dentro.
#ruta=r'C:\Users\Angel\Desktoop'
ruta='Y:\\trabajito\\versionPython\\archivosPython'


def zipdir(ruta, ziph):
    for root, dirs, files in os.walk(ruta):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':


    archivo_zip = shutil.make_archive("viaje", "zip",ruta+ "\\eliminar2")
    print("Creado el archivo:", archivo_zip)