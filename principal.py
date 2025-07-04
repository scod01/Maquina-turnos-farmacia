from numeros import decorador_turno, turno_perfumeria, turno_farmacia, turno_cosmetica

# Funciones que obtienen el siguiente turno decoradas
@decorador_turno
def turno_perfume():
    return next(turno_perfumeria)

@decorador_turno
def turno_medicamento():
    return next(turno_farmacia)

@decorador_turno
def turno_cosmetico():
    return next(turno_cosmetica)

def menu():
    while True:
        print("Bienvenido")
        print("Seleccione la seccion que desea visitar:")
        print("1. Perfumería")
        print("2. Farmacia")
        print("3. Cosmética")
        print("4. Salir")

        opcion = input("Ingrese una opción (1-4): ")

        if opcion == "1":
            turno_perfume()
        elif opcion == "2":
            turno_medicamento()
        elif opcion == "3":
            turno_cosmetico()
        elif opcion == "4":
            print("Gracias por su visita. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()