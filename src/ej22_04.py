def pedir_numero():
    return int(input("Introduce un número entero positivo: "))

def hacer_cuenta(numero):
    cuenta = []
    for i in range(numero, 0, -1):
        cuenta.append(str(i))
    return ", ".join(cuenta)

def main():
    numero = pedir_numero()
    cuenta = hacer_cuenta(numero)
    print(cuenta)

if __name__ == "__main__":
    main()
