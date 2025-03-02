def sumar(primera_entrada, segunda_entrada):
    return primera_entrada + segunda_entrada

def restar(primera_entrada, segunda_entrada):
    return primera_entrada - segunda_entrada

def multiplicar(primera_entrada, segunda_entrada):
    return primera_entrada * segunda_entrada

def dividir(primera_entrada, segunda_entrada):
    if segunda_entrada != 0:
        return primera_entrada / segunda_entrada
    else:
        return "Error: División por cero"

def modulo(primera_entrada, segunda_entrada):
    if segunda_entrada != 0:
        return primera_entrada % segunda_entrada
    else:
        return "Error: Módulo por cero"

# Ejecutamos la calculadora solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Salir")
        
        opcion = input("Ingrese el número de la operación deseada: ")
        
        if opcion in ["1", "2", "3", "4", "5"]:
            primera_entrada = float(input("Ingresa el primer número: "))
            segunda_entrada = float(input("Ingresa el segundo número: "))
            
            if opcion == "1":
                resultado = sumar(primera_entrada, segunda_entrada)
            elif opcion == "2":
                resultado = restar(primera_entrada, segunda_entrada)
            elif opcion == "3":
                resultado = multiplicar(primera_entrada, segunda_entrada)
            elif opcion == "4":
                resultado = dividir(primera_entrada, segunda_entrada)
            elif opcion == "5":
                resultado = modulo(primera_entrada, segunda_entrada)
            
            print("El resultado es:", resultado)
        elif opcion == "6":
            print("Saliendo de la calculadora.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
