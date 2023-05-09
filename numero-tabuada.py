while True:
    numero_escolhido = int(input("Digite um número de 0 a 10 ="))

    if 0 <= numero_escolhido <= 10:
        for x in range (1,11):
            print(numero_escolhido, "x", x ,"=", numero_escolhido*x)
        break

    else:
        print("Número inválido!!")
