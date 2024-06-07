from menu import menu
from adicionar import cadastrar_tarefa
from exibir import exibir_tarefa
from marcar_concluida import concluida
from excluir import excluir_tarefa


def main():
    tarefas = []
    while True:
        escolha = menu()
        if escolha == "1":
            cadastrar_tarefa(tarefas)
        elif escolha == "2":
            exibir_tarefa(tarefas)
        elif escolha == "3":
            concluida(tarefas)
        elif escolha == "4":
            excluir_tarefa(tarefas)
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
