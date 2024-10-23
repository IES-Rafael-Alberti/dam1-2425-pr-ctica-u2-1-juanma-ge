def pedir_edad():
    return int(input("Introduce tu edad actual: "))
    
def comprobar_edad(edad):
    if edad < 18:
        return "Usted es menor de edad"
    else:
        return "Usted es mayor de edad"
   

def main():
    edad = pedir_edad()
    comprobacion = comprobar_edad(edad)
    print(comprobacion)
  

if __name__ == "__main__":
    main()