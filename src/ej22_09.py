def pedir_contraseña():
    contraseña_correcta = "contraseña"
    contraseña_ingresada = input("Introduce la contraseña: ")
    if contraseña_correcta == contraseña_ingresada:
        print("¡Contraseña correcta!, accediendo...")
    else: 
        print("Contraseña incorrecta, vuelve a intentarlo.")
    
def main(): 
    pedir_contraseña()

if __name__ == "__main__":
    main()