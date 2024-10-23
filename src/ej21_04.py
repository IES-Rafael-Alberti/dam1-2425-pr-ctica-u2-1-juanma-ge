def pedir_num():
    return float(input("Introduce un número"))

def division_num(num):
    if num%2 == 0:
        return "El número introducido es par."
    else:
        return "El número introducido es impar."
    

def main():
    num = pedir_num()
    resultado = division_num(num)
    print(resultado)

if __name__ == "__main__":
    main()
