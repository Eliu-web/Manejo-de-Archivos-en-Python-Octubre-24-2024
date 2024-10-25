print(" ")# Salto de linea
print("Velazquez Mares Jesus Eliu")
print(" ")# Salto de linea

t = open("Documento4.txt", "w")# Abrir el archivo 
p=input("ingresa la palabra a agregar:")#Ingresa una palabra al documento
t.write(p)# sobreescrivir
t.close()# Cerrar el archivo

f = open("Documento4.txt", "r")# Abrir el archivo 
print(f.read())
f.close()# Cerrar el archivo