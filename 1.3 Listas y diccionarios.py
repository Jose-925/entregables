# Lista de nombres de estudiantes
estudiantes = ["Juan", "Ana", "Luis"]
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")

# Diccionario de información de contacto
contactos = {
    "migue": "migue@ejemplo.com",
    "lucia": "lucia@ejemplo.com",
    "Luis": "luis@ejemplo.com"
}
for clave, valor in contactos.items():
    print(f"Nombre: {clave}, Correo: {valor}")

# Script para agregar elementos a una lista o actualizar un diccionario
nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ")
estudiantes.append(nuevo_estudiante)
print("Lista actualizada:", estudiantes)

nuevo_contacto = input("Ingresa un nombre para actualizar/agregar: ")
nuevo_correo = input("Ingresa el correo de contacto: ")
contactos[nuevo_contacto] = nuevo_correo
print("Contactos actualizados:", contactos)
