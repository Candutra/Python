nota = input("Digite a nota do aluno: ")

nota = float(nota)

if nota >= 6:
    print("Aprovado")
elif nota <= 4:
    print("Aluno reprovado")
else:
    print("Recuperação")