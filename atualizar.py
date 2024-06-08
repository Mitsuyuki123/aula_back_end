def atualizar_contato(contatos):
    if not contatos:
        print("Lista de contatos vazia.")
        return
    while True:
        print("para sair digite 'sair'")
        contato_att = input("Digite o nome do contato a ser atualizado: ")
        if contato_att == "sair":
            return
        for indice, contato in enumerate(contatos):
            if contato_att in contato['nome']:
                index = indice
                while True:
                    print("para sair digite 'sair'")
                    dado_para_att = input("Digite o dado a ser atualizado (nome/telefone/email): ")
                    if dado_para_att == "sair":
                        return
                    elif dado_para_att not in ["nome", "telefone", "email"]:
                        print("Dado inválido. Digite 'nome', 'telefone' ou 'email'.")
                    else:
                        new_data = input(f"Digite o novo {dado_para_att} do contato: ")
                        contatos[index][f'{dado_para_att}'] = new_data
                        print(f"O {dado_para_att} foi atualizado com sucesso.")
                        return
        print(f"Contato '{contato_att}' não encontrado")
