def preguntar_pizza():
    return input("¿Desea una pizza vegetariana o no vegetariana?:")

def elegir_ingredientes(pizza):
    if pizza == "vegetariana":
        ingrediente_adicional = input("¿Desea como ingrediente adicional pimiento o tofu?:")
        return ingrediente_adicional
    if pizza == "no vegetariana": 
        ingrediente_adicional2 = input("¿Desea como ingrediente adicional peperoni, jamón o salmón?:")
        return ingrediente_adicional2


def main():
    pizza = preguntar_pizza()
    ingrediente = elegir_ingredientes(pizza)
    print(f"Tu pizza es {pizza} y aparte de mozzarella y tomate lleva {ingrediente}.")


if __name__ == "__main__":
    main()