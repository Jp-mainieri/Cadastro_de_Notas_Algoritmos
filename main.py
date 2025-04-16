quantidadeAlunos = int(input("Digite a quantidade de alunos"))
cadastro = []

for i in range(quantidadeAlunos):
    boletim = []
    nomeAluno = input(f"Digite o nome do aluno {i+1}")
    notaProvaT = []
    notaProjetoP = []
    for a in range(2):
        notaProvaT.append(float(input(f"Nota da prova teórica {a+1} do aluno {i+1}")))
    for a in range(2):
        notaProjetoP.append(float(input(f"Nota do projeto {a+1} do aluno {i+1}")))

    media = []
    media.append(0.4 * notaProvaT[0] + 0.6 * notaProvaT[1])
    media.append((notaProjetoP[0] + notaProjetoP[1]) / 2)

    if media[0] == 5 and media[1] == 5:
        mediaFinal = 0.3 * media[1] + 0.7 * media[0]
    else:
        if media[1] > media[0]:
            mediaFinal = media[0]
        else:
            mediaFinal = media[1]

    boletim.append(nomeAluno)
    boletim.append(notaProvaT)
    boletim.append(notaProjetoP)
    boletim.append(media)
    boletim.append(mediaFinal)
    
    cadastro.append(boletim)
print(cadastro)