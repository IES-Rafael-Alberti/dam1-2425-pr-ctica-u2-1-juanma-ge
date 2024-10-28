def pedir_edad():
    return int(input("Introduce tu edad: "))

def repetir(edad):
    for i in range(1, edad + 1):
        print(i)



def main():
    edad = pedir_edad()
    repeticion = repetir(edad)


if __name__ == "__main__":
    main()