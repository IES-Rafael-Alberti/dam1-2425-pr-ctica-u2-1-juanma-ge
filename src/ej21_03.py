def pedir_num1():
    return float(input("Introduce un número:"))

def pedir_num2():
    return float(input("Introduce otro número:"))

def comprobar_division(num1, num2):
    if num2 == 0:
        return "**ERROR**"
    else:
        return num1/num2

def main():
    num1 = pedir_num1()
    num2 = pedir_num2()
    resultado = comprobar_division(num1, num2)
    print(resultado)


if __name__ == "__main__":
    main()