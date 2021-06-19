# recibir datos de usuario
def nombre_completo():
    print("Ingrese su nombre: ")
    nombre = input()

    apellido = input("ingrese su apellido: ")

    print("Su nombre es: ", nombre, apellido)

#precio
def peso_kilo_producto(peso_empacado, precio_empacado):
    PESO_KILO = 1000
    precio_kilo = (PESO_KILO * precio_empacado) / peso_empacado
    
peso_empacado = float(input("ingrese el peso empacado "))
precio_empacado = float(input("ingrese el pecio empacado " ))

#funciones
print("el precio por kilo es", precio_kilo)
peso_kilo_producto(peso_empacado, precio_empacado)