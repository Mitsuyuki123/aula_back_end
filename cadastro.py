def cadastrar_aluno(alunos):
    nome = input('Nome do aluno: ')
    idade = input('Idade: ')
    cidade = input('Cidade: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'nota1': nota1,
        'nota2': nota2,
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")