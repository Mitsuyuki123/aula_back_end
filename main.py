from menu import menu
from adicionar import adicionar_contato
from visualizar import exibir_contatos
from atualizar import atualizar_contato
from remover import remover_contato


def main():
    contatos = []
    while True:
        escolha = menu()
        if escolha == '1':
            adicionar_contato(contatos)
        elif escolha == '2':
            exibir_contatos(contatos)
        elif escolha == '3':
            atualizar_contato(contatos)
        elif escolha == '4':
            remover_contato(contatos)
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
