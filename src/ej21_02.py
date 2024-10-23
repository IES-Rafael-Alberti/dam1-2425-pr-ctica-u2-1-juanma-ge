def pedir_contraseña():
    return input("Introduce tu contraseña:")

def pedir_contraseña2():
    return input("Introduce de nuevo tu contraseña:")

def comparar_contraseñas():
    contreseña1 = pedir_contraseña()
    contraseña2 = pedir_contraseña2()
    if contreseña1.lower() == contraseña2.lower():
        return "Ambas contraseñas coinciden."
    else:
        return "Las contraseñas no coinciden."
    
def main():
    comprobacion = comparar_contraseñas()
    print(comprobacion)


if __name__ == "__main__":
    main()
