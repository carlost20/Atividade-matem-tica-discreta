##validação do menu
def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio<= valor <= fim:
                return(valor)
            else:
                print("\nValor inválido, favor digitar entre %d e %d" %(inicio,fim))
                
        except ValueError:
                continue
##Menu
def menu():
        print("""\n----------Menu Principal----------\n
    Qual questão você deseja solucionar:\n
    1 - Questão 1 (Números Pseudo-Aleatórios) 
    2 - Questão 2 (Código ISBN)
    3 - Questão 5 (Mdc a,b)
    4 - Questão 6 (A conjectura de Collatriz)
    0 - sair
    
""")

        return valida_faixa_inteiro("Escolha uma opção: ",0,4)






##questão 1
def Numeros_Pseudo_Aleatórios():
    while True:
        numeros = []
        x0 = int(input("\nDigite o número inteiro x0:\n"))
        numeros.append(x0)
        a = int(input("\nDigite o número inteiro a:\n"))
        b = int(input("\nDigite o número inteiro b:\n"))
        m = int(input("\nDigite o número inteiro m:\n"))
            
        while len(numeros) < 11:
            x1 = (a*x0+b)%m
            numeros.append(x1)
            x0 = x1
        print(numeros)
        continua = input("\nDeseja fazer outra sequência?(sim/não)\n")
        if continua == "sim":
            continue
        else:
            break
##questão 2
def ISBN():
    while True:
        digito = list(input("\nDigite os 12 números inteiros do seu código ISBN:\n"))

        digito[0] = int(digito[0])
        digito[1] = int(digito[1])
        digito[2] = int(digito[2])
        digito[3] = int(digito[3])
        digito[4] = int(digito[4])
        digito[5] = int(digito[5])
        digito[6] = int(digito[6])
        digito[7] = int(digito[7])
        digito[8] = int(digito[8])
        digito[9] = int(digito[9])
        digito[10] = int(digito[10])
        digito[11] = int(digito[11])

        total = digito[0] + digito[1] + digito[2] + digito[3] + digito[4] + digito[5] + digito[6] + digito[7] + digito[8] + digito[9] + digito[10] + digito[11]

        d_verificador = 10 - (total%10)

        print(d_verificador)
        continua = input("\nDeseja checar outro número?(sim/não)\n")
        if continua == "sim":
            continue
        else:
            break
##questão 5
def Mdc():
    while True:
        a = int(input("\nDigite o número inteiro a:\n"))
        b = int(input("\nDigite o número inteiro b:\n"))
        if b == 0:
            print("O mdc de a e b é %d"%a)
        elif a == 0:
            print("O mdc de a e b é %d"%b)
        elif a != 0 and b != 0:
            while b != 0:
                r = a%b
                a = b
                b = r
            print("O Mdc de a e b é %d"%a)
        continua = input("\nDeseja fazer outro Mdc?(sim/não)\n")
        if continua == "sim":
            continue
        else:
            break
##questão 6
def collatriz():
    while True:
        x = int(input("\nDigite um número inteiro:\n"))
        c = 0
        while True:
            if x%2 == 0:
                x = x/2
                c += 1
            elif x == 1:
                print("O número 1 foi obtido em %d passos"%c)
                break
            elif x%2 != 0:
                x = 3*x + 1
                c += 1
        continua = input("\nDeseja checar mais algum número inteiro?(sim/não)\n")
        if continua == "sim":
            continue
        else:
            break
            
while True:
    opção = menu()

    if opção == 0:
        break
    elif opção == 1:
        Numeros_Pseudo_Aleatórios()
    elif opção == 2:
        ISBN()
    elif opção == 3:
        Mdc()
    elif opção == 4:
        collatriz()

        
    
    



    
    
    




