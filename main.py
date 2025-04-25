print("------------------------------")
print(" CADASTRO DE NOTAS DE ALUNOS  ")
print("------------------------------")
print()
quantidadeAlunos = int(input("\nDigite a quantidade de alunos para cadastrar: "))
cadastro = []

maiorMediaFinal = 0
menorMediaFinal = 10

numeroAprovados = 0
for i in range(quantidadeAlunos):

    boletim = []
    nomeAluno = input(f"\nDigite o nome do aluno {i+1}: ")
    notaProvaT = []
    notaProjetoP = []

    for a in range(2):
        notaProvaT.append(float(input(f"Nota da prova teórica {a+1} do aluno(a) {nomeAluno}: ")))
    for a in range(2):
        notaProjetoP.append(float(input(f"Nota do projeto {a+1} do aluno(a) {nomeAluno}: ")))

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

continuar = True
while continuar == True:
    
    print("\n------------------------------")
    print("             MENU             ")
    print("------------------------------")
    print("1- Boletins")
    print("2- Pesquisar boletim pelo nome")
    print("3- Maior média final")
    print("4- Menor média final")
    print("5- Percentual de aprovados")
    print("6- Cadastrar novos alunos")
    print("------------------------------\n")

    menu = int(input("Escolha uma das opções: "))

    while menu < 1 or menu > 6:
        print("Escolha inválida")
        menu = int(input("Escolha uma das opções: "))

    print()

    if menu == 1:
        print("Boletins:")
        print()
        for x in cadastro:
            print("\nNome: ", x[0])
            print("Nota da prova teórica 1: ", x[1][0])
            print("Nota da prova teórica 2: ", x[1][1])
            print("Nota do projeto 1: ", x[2][0])
            print("Nota do projeto 2: ", x[2][1])
            print("Média das provas teóricas: ", x[3][0])
            print("Média dos projetos: ", x[3][1])
            print("Média Final: ", x[4])

    elif menu == 2:

        print("Pesquisar boletim pelo nome:")
        pesquisarNome = input("Nome: ")
        print()
        pesquisando = True
        while pesquisando == True:
            for x in range(quantidadeAlunos):
                if cadastro[x][0] == pesquisarNome:
                    print("Nota da prova teórica 1: ", cadastro[x][1][0])
                    print("Nota da prova teórica 2: ", cadastro[x][1][1])
                    print("Nota do projeto 1: ", cadastro[x][2][0])
                    print("Nota do projeto 2: ", cadastro[x][2][1])
                    print("Média das provas teóricas: ", cadastro[x][3][0])
                    print("Média dos projetos: ", cadastro[x][3][1])
                    print("Média Final: ", cadastro[x][4])
                    pesquisando = False
                    break
            if pesquisando:
                print("Nome inválido, insira um nome cadastrado")
                pesquisarNome = input("Nome: ")
                pesquisando = True

    elif menu == 3:

        print("Maior média final:",end="")
        print(maiorMediaFinal)

    elif menu == 4:

        print("Menor média final:",end="")
        print(menorMediaFinal)
        
    elif menu == 5:

        print("Percentual de aprovados:",end="")
        print((numeroAprovados / quantidadeAlunos)*100,"%")
    else:
        quantidadeAlunos = int(input("\nDigite a quantidade de alunos para cadastrar: "))
        for i in range(quantidadeAlunos):
            boletim = []
            nomeAluno = input(f"\nDigite o nome do aluno {i+1}: ")
            notaProvaT = []
            notaProjetoP = []

            for a in range(2):
                notaProvaT.append(float(input(f"Nota da prova teórica {a+1} do aluno(a) {nomeAluno}: ")))
            for a in range(2):
                notaProjetoP.append(float(input(f"Nota do projeto {a+1} do aluno(a) {nomeAluno}: ")))

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

    if input("Quer continuar no sistema? (s/n): ") == "s":
        continuar = True
    else:
        continuar = False