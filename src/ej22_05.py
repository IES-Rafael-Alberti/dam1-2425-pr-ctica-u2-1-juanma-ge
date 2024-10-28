def cantidad_a_invertir():
    return float(input("Introduce la cantidad a invertir: "))

def interes_anual():
    return float(input("Introduce el interés anual: "))

def num_años():
    return int(input("Introduce en número de años: "))

def calcular_capital(inversion, interes, años):
    capital = []
    for i in range(1, años + 1):
        inversion *= 1 + interes / 100
        capital.append(inversion)
    return capital

def main():
    inversion = cantidad_a_invertir()
    interes = interes_anual()
    años = num_años()
    capital = calcular_capital(años, inversion, interes)
    print(capital)
    
if __name__ == "__main__":
    main()
