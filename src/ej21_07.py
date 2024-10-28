def pedir_renta():
    return float(input("Introduce tu renta anual: "))

def calcular_renta(renta):
    if renta < 10000:
        impositivo = 5
    if 10000 >= renta <= 20000:
        impositivo = 15
    if 20000 >= renta <= 35000:
        impositivo = 20
    if 35000 >= renta <= 60000:
        impositivo = 30
    else: 
        impositivo = 45
    return impositivo   


def main():
    renta = pedir_renta()
    impositivo = calcular_renta(renta)
    print(f"Tu renta anual son {renta: .2f} euros, por lo que tu impositivo es del {impositivo}%.")

if __name__ == "__main__":
    main()