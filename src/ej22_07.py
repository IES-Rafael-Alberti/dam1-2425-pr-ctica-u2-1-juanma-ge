def tabla1():
    for i in range(1, 11):
        print(f"La tabla del {i}: ")
        for i2 in range(1, 11):
            resultado = i * i2
            print(resultado)


def main():
    tabla1()

if __name__ == "__main__":
    main()