def exibir_contatos(contatos):
    if not contatos:
        print("Lista de contatos vazia.")
        return

    for contato in contatos:
        print(f"\nNome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}\n")
