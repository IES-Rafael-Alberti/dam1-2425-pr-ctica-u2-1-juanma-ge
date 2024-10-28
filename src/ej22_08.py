def pedir_numero():
    return int(input("Introduce un número entero: "))

def generar_fila(numero: int) -> str:
    fila = ""
    for i in range(numero, 0, -2):
        fila += f"{i} "
    return fila.strip() + "\n"


def hacer_escalera(numero: int) -> str:
    triangulo = ""
    for i in range(1, numero + 1, 2):
        triangulo += generar_fila(i)
    
    return triangulo
          
def main():
    numero = pedir_numero()
    print(hacer_escalera(numero))

if __name__ == "__main__":
    main()