def pedir_numero():
    return int(input("Introduce un número entero: "))

def comprobar_numero(numero):
    if numero < 2:
        print("El número no es primo.")
    for i in range(2, numero):
        if numero%i == 0:
            return print("El número no es primo.")
        else: 
            return print("El número es primo.")

def main():
    numero = pedir_numero()
    comprobar_numero(numero)

if __name__ == "__main__":
    main()
