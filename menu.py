class MenuPrincipal:
    @staticmethod
    def exibir_menu():
        print('\nMenu')
        print('1 - Adicionar tarefa')
        print('2 - Exibir tarefas')
        print('3 - Buscar tarefa')
        print('4 - Atualizar tarefa')
        print('5 - Excluir tarefa')
        print('0 - Sair')

        opcao = input("Escolha uma opção: ")
        return opcao
