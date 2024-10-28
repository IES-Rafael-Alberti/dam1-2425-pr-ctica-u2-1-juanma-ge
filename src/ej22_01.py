def pedir_nombre():
    return input("Introduce tu nombre: ")

def repeticion(nombre):
    for i in range(10):
        print(nombre)



def main():
    nombre = pedir_nombre()
    repetir = repeticion(nombre)


if __name__ == "__main__":
    main()
