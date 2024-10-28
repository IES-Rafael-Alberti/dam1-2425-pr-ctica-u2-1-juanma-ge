def evaluar_empleado(puntuacion):
    beneficio_base = 2400  
    if puntuacion == 0.0:
        nivel = "Inaceptable"
        beneficio = beneficio_base * puntuacion
    elif puntuacion == 0.4:
        nivel = "Aceptable"
        beneficio = beneficio_base * puntuacion
    elif puntuacion >= 0.6:
        nivel = "Meritorio"
        beneficio = beneficio_base * puntuacion
    else:
        return "Puntuación no válida. Debe ser 0.0, 0.4, 0.6 o más."

    return f"Nivel: {nivel}, Beneficio: {beneficio:.2f}€"


def main():
    puntuacion = float(input("Introduce la puntuación del empleado (0.0, 0.4, 0.6 o más): "))
    evaluacion = evaluar_empleado(puntuacion)
    print(evaluacion)

if __name__ == "__main__":
    main()
