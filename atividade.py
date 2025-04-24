quantidadeAlunos = int(input("Digite a quantidade de alunos para ser cadastrada: "))
cadastro = []
maiorMediaFinal = 0
menorMediaFinal = 10
numeroAprovados = 0

for i in range(quantidadeAlunos):

    boletim = []

    nomeAluno = input(f"Digite o nome do aluno {i+1}: ")

    notaProvaT = []
    notaProjetoP = []

    for a in range(2):
        notaProvaT.append(float(input(f"Nota da prova teórica {a+1} do aluno {i+1}: " )))
    for a in range(2):
        notaProjetoP.append(float(input(f"Nota do projeto {a+1} do aluno {i+1}: ")))

    media = []
    media.append(0.4 * notaProvaT[0] + 0.6 * notaProvaT[1])
    media.append((notaProjetoP[0] + notaProjetoP[1]) / 2)

    if media[0] >= 5 and media[1] >= 5:
        mediaFinal = 0.3 * media[1] + 0.7 * media[0]
    else:
        if media[1] > media[0]:
            mediaFinal = media[0]
        else:
            mediaFinal = media[1]

    if maiorMediaFinal < mediaFinal:
        maiorMediaFinal = mediaFinal
    if menorMediaFinal > mediaFinal:
        menorMediaFinal = mediaFinal
        
    if mediaFinal >= 5:
        numeroAprovados +=1

    boletim.append(nomeAluno)
    boletim.append(notaProvaT)
    boletim.append(notaProjetoP)
    boletim.append(media)
    boletim.append(mediaFinal)
    
    cadastro.append(boletim)
    print()
    print(f"Cadastro do aluno {i+1} realizado")
    print()
#MENU

continuar = True

while continuar == True:

    print()
    print("------------------------------")
    print("             MENU             ")
    print("------------------------------")
    print("1- Boletins")
    print("2- Pesquisar pelo nome")
    print("3- Maior média final")
    print("4- Menor média final")
    print("5- Percentual de aprovados")
    print("------------------------------")
    print()

    menu = int(input("Escolha uma das opções: "))

    while 1 > menu or 5 < menu:

        print("Opção inválida")
        menu = int(input("Escolha uma das opções: "))

    print()

    if menu == 1:

        print("Boletins:")
        for x in cadastro:
            
            print("Nome: ",cadastro[i][1])
            print("Notas das provas teóricas: ",cadastro[i][2])
            print("Notas dos projetos: ",cadastro[i][3])
            print("Médias: ",cadastro[i][4])
            print("Média Final: ",cadastro[i][5])

    elif menu == 2:

        print("Pesquisando pelo nome:")
        pesquisarNome = input("Nome: ")
        for i in range(quantidadeAlunos):
            if cadastro[i][0] == pesquisarNome:
                print(cadastro[i])
                break

    elif menu == 3:

        print("Maior média final:",end=" ")
        print(maiorMediaFinal)

    elif menu == 4:

        print("Menor média final:",end=" ")
        print(menorMediaFinal)

    else:

        print("Percentual de aprovados:",end=" ")
        print((numeroAprovados / quantidadeAlunos)*100,"%")

    print()

    if input("Quer continuar? (s/n): ") == "s":
        continuar = True
    else:
        continuar = False