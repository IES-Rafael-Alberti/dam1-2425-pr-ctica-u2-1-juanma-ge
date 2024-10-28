def pedir_numero():
    return int(input("Introduce un número: "))

def astersicos_calcular(numero):
    for i in range(1, numero + 1):
        print("*" * i)


def main():
    numero = pedir_numero()
    astersicos_calcular(numero)
    

if __name__ == "__main__":
    main()
