def sumar(*entradas):
    resultado = sum(entradas)
    return resultado

def restar(*entradas):
    resultado = entradas[0]
    for num in entradas[1:]:
        resultado -= num
    return resultado

def multiplicar(*entradas):
    resultado = 1
    for num in entradas:
        resultado *= num
    return resultado

def dividir(*entradas):
    resultado = entradas[0]
    for num in entradas[1:]:
        if num == 0:
            return "Error: División por cero"
        resultado /= num
    return resultado

def modulo(*entradas):
    resultado = entradas[0]
    for num in entradas[1:]:
        if num == 0:
            return "Error: Módulo por cero"
        resultado %= num
    return resultado

# Ejecutamos la calculadora solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Expresión personalizada")
        print("7. Salir")
        
        opcion = input("Ingrese el número de la operación deseada: ")
        
        if opcion in ["1", "2", "3", "4", "5"]:
            entradas = list(map(float, input("Ingrese los números separados por espacio: ").split()))
            
            if len(entradas) < 2:
                print("Debe ingresar al menos dos números.")
                continue
            
            if opcion == "1":
                resultado = sumar(*entradas)
            elif opcion == "2":
                resultado = restar(*entradas)
            elif opcion == "3":
                resultado = multiplicar(*entradas)
            elif opcion == "4":
                resultado = dividir(*entradas)
            elif opcion == "5":
                resultado = modulo(*entradas)
            
            print("El resultado es:", resultado)
        elif opcion == "6":
            expresion = input("Ingrese la operación que desea realizar (ejemplo: 2 + 4 - 3, 4 * 5 + 1 / 3): ")
            try:
                resultado = eval(expresion)
                print("El resultado es:", resultado)
            except Exception as e:
                print("Error en la expresión:", e)
        elif opcion == "7":
            print("Saliendo de la calculadora.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
