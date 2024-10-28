def pedir_sexo():
    return input("Introduce tu sexo (femenino/masculino):").lower()

def pedir_nombre():
    return input("Introduce tu nombre:").lower()

def comparar_nombre_sexo(nombre, sexo):
    primera_letra = nombre[0]
    n_ascii = ord(primera_letra)
    if sexo == "femenino":
        if n_ascii < 77:
            grupo = "A"
        else:
            grupo = "B"
    if sexo == "masculino":
        if n_ascii > 77:
            grupo = "A"
        else: 
            grupo = "B"
    return grupo

def main():
    sexo = pedir_sexo()
    nombre = pedir_nombre()
    grupo = comparar_nombre_sexo(nombre, sexo)
    print(f"Perteneces a la clase {grupo}")

if __name__ == "__main__":
    main()