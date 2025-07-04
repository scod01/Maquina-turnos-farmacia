# Decorador para mostrar el mensaje completo al cliente


def decorador_turno(funcion):
    def turno():
        print("Gracias por utilizar nuestro sistema de turnos.")
        print("Su turno es:")
        print(funcion())
        print("Aguarde y será atendido.\n")
    return turno

# Generadores de turnos por área
def generador_turnos(prefijo):
    numero = 1
    while True:
        yield f"{prefijo}-{numero}"
        numero += 1

# Instancias de generadores
turno_perfumeria = generador_turnos("P")
turno_farmacia = generador_turnos("F")
turno_cosmetica = generador_turnos("C")