def soma_dois_maiores(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    return numeros[1] + numeros[2]

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))
print("A soma dos dois maiores números é:", soma_dois_maiores(numero1, numero2, numero3))
