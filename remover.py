def remover_contato(contatos):
    if not contatos:
        print("Lista de contatos vazia.")
        return
    while True:
        print("para sair digite 'sair'")
        contato_remover = input("Informe o nome do contato a ser removido da lista : ")
        if contato_remover == "sair":
            return
        for indice, contato in enumerate(contatos):
            if contato['nome'] == contato_remover:
                contato_excluido = contatos.pop(indice)
                print(f"O contato '{contato_excluido['nome']}' foi removido.")
                return

        print(f"Contato '{contato_remover}' não encontrado.")
