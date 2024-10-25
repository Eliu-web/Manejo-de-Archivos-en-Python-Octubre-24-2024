print(" ")# Salto de linea
print("Velazquez Mares Jesus Eliu")
print(" ")# Salto de linea

r = open("Documento3.txt", "a")# Abre el archivo para anexar
p=input("Ingresa la palabra a agregar: ")#Ingresa una palabra al documento
r.write(p)
r.close()# Cerrar el archivo

f = open("Documento3.txt", "r")# Abrir el archivo
print(f.read())
f.close()# Cerrar el archivo 