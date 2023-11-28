nota = input("Digite a nota do aluno: ")

nota = float(nota)

if nota >= 6:
    print("Aluno aprovado")
elif nota <= 4:
    print("Aluno reprovado")
else:
    print("O aluno esta de recuperação")

    ntrp = float(input("Digite a nota do trabalho recuperação: "))
    if ntrp >= 6:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

