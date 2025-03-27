# Programa sencillo que calcula el área de un rectángulo y verifica si es un cuadrado

def calcular_area(base, altura):
    return base * altura

def es_cuadrado(base, altura):
    return base == altura

def main():
    print("Cálculo de área de un rectángulo")
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))

    area = calcular_area(base, altura)
    print(f"El área del rectángulo es: {area}")

    if es_cuadrado(base, altura):
        print("El rectángulo es un cuadrado.")
    else:
        print("El rectángulo no es un cuadrado.")

if __name__ == "__main__":
    main()