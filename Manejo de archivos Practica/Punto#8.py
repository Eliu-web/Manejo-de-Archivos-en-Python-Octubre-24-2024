print(" ")# Salto de linea
print("Velazquez Mares Jesus Eliu")
print(" ")# Salto de linea

import os

if os.path.exists("Documento5.txt"):# Verifica si el documento existe
    os.remove("Documento5.txt")# si es asi lo elimina
    print("El archivo ha sido eliminado.")
else:
    print("El archivo no existe.")# Si no manda este mensaje