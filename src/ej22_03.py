def pedir_numero():
    return int(input("Introduce un número entero positivo: "))

def sacar_impares(numero):
    impares = []
    for i in range(1, numero + 1):
        if i%2 != 0:
            impares.append(str(i))
    return ", ".join(impares)

def main():
    numero = pedir_numero()
    impares = sacar_impares(numero)
    print(impares)

if __name__ == "__main__":
    main()