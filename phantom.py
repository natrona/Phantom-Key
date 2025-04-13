import random
import string
import os
import sys

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return '[ERRO] Nenhum tipo de caractere selecionado.'

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def painel():
    tamanho = 12
    usar_maiusculas = True
    usar_minusculas = True
    usar_numeros = True
    usar_simbolos = True

    while True:
        try:
            limpar()
            print("======== Phantom Key - Painel =========")
            print(f"Tamanho da senha: {tamanho}")
            print(f"[{'X' if usar_maiusculas else ' '}] Letras maiúsculas")
            print(f"[{'X' if usar_minusculas else ' '}] Letras minúsculas")
            print(f"[{'X' if usar_numeros else ' '}] Números")
            print(f"[{'X' if usar_simbolos else ' '}] Símbolos")
            print("=======================================")
            print("1 - Gerar senha")
            print("2 - Alterar tamanho")
            print("3 - Alternar tipos de caracteres")
            print("4 - Ajuda")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
                print(f"\nSenha gerada: {senha}\n")
                input("Pressione Enter para voltar ao menu...")
            elif opcao == '2':
                try:
                    novo_tamanho = int(input("Novo tamanho da senha: "))
                    if novo_tamanho > 0:
                        tamanho = novo_tamanho
                    else:
                        print("Digite um número positivo.")
                        input("Pressione Enter para continuar...")
                except ValueError:
                    print("Valor inválido.")
                    input("Pressione Enter para continuar...")
            elif opcao == '3':
                print("\nAlternar:")
                print("1 - Maiúsculas")
                print("2 - Minúsculas")
                print("3 - Números")
                print("4 - Símbolos")
                sub = input("Escolha o tipo: ")
                if sub == '1':
                    usar_maiusculas = not usar_maiusculas
                elif sub == '2':
                    usar_minusculas = not usar_minusculas
                elif sub == '3':
                    usar_numeros = not usar_numeros
                elif sub == '4':
                    usar_simbolos = not usar_simbolos
            elif opcao == '4':
                print("\nEste é um gerador de senhas seguras com painel interativo no terminal.")
                print("Escolha os tipos de caracteres e o tamanho, e gere sua senha!\n")
                input("Pressione Enter para continuar...")
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")
        except EOFError:
            break

if __name__ == "__main__":
    painel()
