print(" ")# Salto de linea
print("Velazquez Mares Jesus Eliu")
print(" ")# Salto de linea

# Intentar eliminar la carpeta donde esta el archivo
import os
try:
    os.rmdir("E:/Manejo de archivos Practica")
    print("La carpeta ha sido eliminada.")
except FileNotFoundError:
    print("La carpeta no existe.")
except OSError:
    print("La carpeta no está vacía.")
except Exception as e:
    print(f"Error: {e}")