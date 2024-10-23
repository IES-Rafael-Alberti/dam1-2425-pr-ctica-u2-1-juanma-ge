def pedir_edad(): 
    edad_incorrecta = True
    
    while edad_incorrecta:
        try:
            edad = int(input("Introduce cuántos años tienes: "))
            if edad < 0:
                raise ValueError("La edad debe ser un número positivo.")
            if edad == 0:
                raise ValueError("La edad debe ser un número mayor que cero.")
                
                
                edad_incorrecta = False
        except ValueError:
            print
        except Exception as e:


                    return edad



def mostrar_anios_cumplidos(edad:int):
    serie = ""
    for i in range(1, edad + 1):
        if i == edad: 
            print(i)
        else:
            print(i, end = ", ")





def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años:")
    mostrar_anios_cumplidos(edad)