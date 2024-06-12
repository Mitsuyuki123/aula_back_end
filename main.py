from menu import MenuPrincipal
from tarefa import Tarefas
from gerenciador_tarefas import GerenciadorTarefas


def main():
    gerenciador = GerenciadorTarefas()
    while True:
        opcao = MenuPrincipal.exibir_menu()

        if opcao == "1":  # adicionar
            nome = input("Digite o nome da tarefa: ")
            descricao = input("Descrição breve da tarefa: ")
            tarefa = Tarefas(nome, descricao)
            gerenciador.adicionar_tarefa(tarefa)

        elif opcao == "2":  # exibir
            gerenciador.exibir_tarefa()

        elif opcao == "3":  # buscar
            nome = input("Digite o nome da tarefa pra busca: ")
            tarefa_encontrada = gerenciador.localizar_tarefa(nome)
            if tarefa_encontrada:
                print(f"Nome: {tarefa_encontrada.nome}")
                print(f"Descrição: {tarefa_encontrada.descricao}")
                status = "concluida" if tarefa_encontrada.status else "pendente"
                print(f"Status: {status}")
            else:
                print(f"Tarefa '{nome}' não encontrada")


        elif opcao == "4":  # atualizar
            tarefa_att = input("Digite o nome da tarefa que deseja atualizar: ")
            tarefa = gerenciador.localizar_tarefa(tarefa_att)
            gerenciador.atualizar_tarefa(tarefa)

        elif opcao == "5":  # remover
            nome = input("Digite o nome da tarefa a ser removida: ")
            tarefa_encontrada = gerenciador.localizar_tarefa(nome)
            if tarefa_encontrada:
                gerenciador.remove_tarefa(tarefa_encontrada)
            else:
                print(f"Tarefa '{nome}' não encontrada")
        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
