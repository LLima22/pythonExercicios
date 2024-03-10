def valores_ate_n():
    while True:
        N = int(input("Digite um valor para N (maior que zero): "))
        if N > 0:
            break
        else:
            print("O valor de N deve ser maior que zero. Tente novamente.")
    for i in range(1, N + 1):
        print(i)

valores_ate_n()
