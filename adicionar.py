def adicionar_contato(contatos):
    nome = input("Nome: ")
    tel = input("Telefone: ")
    email = input("Email: ")

    contato = {
        "nome": nome,
        "telefone": tel,
        "email": email
    }
    contatos.append(contato)
    print(f"'{nome}' foi adicionado a lista de contatos.")
