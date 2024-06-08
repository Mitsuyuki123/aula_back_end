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
                    if dado_para_att == "nome":
                        novo_nome = input("Digite o novo nome do contato: ")
                        contatos[index]['nome'] = novo_nome
                        print(f"Nome atualizado com sucesso! O novo nome é '{contatos[index]['nome']}'")
                        return
                    elif dado_para_att == "telefone":
                        novo_tel = input("Digite o novo número do contato: ")
                        contatos[index]['telefone'] = novo_tel
                        print(f"Telefone atualizado com sucesso! O novo número é '{contatos[index]['telefone']}'")
                        return
                    elif dado_para_att == "email":
                        novo_mail = input("Digite o novo email do contato: ")
                        contatos[index]['email'] = novo_mail
                        print(f"E-mail atualizado com sucesso! O novo email é '{contatos[index]['email']}'")
                        return
                    else:
                        print("Dado inválido.")
        print(f"Contato '{contato_att}' não encontrado")
