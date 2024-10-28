#Hacer un programa que borre el términal, pedir un número del 1 al 100, control de errores para números negativos y para letras "inválidos"
#Si metes un número mayor a 20 (puede ser hasta 100 en algún momento), pedir uno dentro del intervalo, si pones un 0 su pirámide es 0=>0.
#Si es un 3=>3+2+1 = 6
#2=> 2+1 = 3
#1=> 1
#o=> 0
#Al final pregunta si quiere volver a hacer la pirámide (s/n)
from os import system
NUMERO_MAXIMO = 20

def pedir_numero():
    valor = input("Introduce un número de 1 a 20: ")
    return valor

def comprobar_numero(valor):
    try:
        valor = int(valor)
        if valor == 0 and valor <= NUMERO_MAXIMO:
            return True
        if valor < 0:
            return "negativo"
    except ValueError: 
     return "inválido"
    
def calcular_piramide(num):
    serie1=""
    serie2=""
    for i in range(num,0):
        serie1=f"{i}=>"
        for x in range(0,num):
            if x ==0:
                serie1+=f"{x}"
            else:
                serie1+=f"+{x}"
    for i in range(0,num):
        serie2=f"{i}=>"
        for x in range(num,0):
            if x == num:
                serie2+=f"{x}"
            else:
                serie2+=f"+{x}"
    print(serie1,serie2)

    


        
def main():
    system("clear")
    valor = pedir_numero()
    while comprobar_numero(valor) == "negativo":
        print("**ERROR** introduce un número positivo: ") 
        valor = pedir_numero()
    while comprobar_numero(valor) == "inválido":
        print("**ERROR NÚMERO INVÁLIDO** introduce un número: ")
        valor = pedir_numero()
    num = int(valor)
    calcular_piramide(num)


if __name__ == "__main__":
    main()
    

