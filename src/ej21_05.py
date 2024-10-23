def pedir_edad():
    return int(input("Introduce tu edad:"))

def pedir_ingresos():
    return float(input("Introduce tus ingresos mensuales:"))

def comprobar_edad_ing(edad, ingresos):
    if edad < 16:
        return "Afortunadamente por tí, no debes tributar, por ahora."
    if ingresos < 1000:
        return "Afortunadamente por tí, no debes tributar, por ahora."
    else:
        return "Lamentablemente por tí, debes tributar."


def main():
    edad = pedir_edad()
    ingresos = pedir_ingresos()
    comprobacion = comprobar_edad_ing(edad, ingresos)
    print(comprobacion)

if __name__ == "__main__":
    main()