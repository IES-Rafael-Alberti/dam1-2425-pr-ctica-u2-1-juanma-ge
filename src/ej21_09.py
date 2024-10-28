def  pedir_edad():
    return int(input("Introduce tu edad: "))

def calcular_precio(edad):
    if edad < 4:
        return "Puede entrar gratis."
    if 4 <= edad <= 18:
        return "La entrada le costaría 5 euros."
    if edad > 18:
        return "La entrada le costaría 10 euros."


def main():
    edad = pedir_edad()
    cálculo = calcular_precio(edad)
    print(cálculo)

if __name__ == "__main__":
    main()