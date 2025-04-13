#!/usr/bin/env python3

import random
import string
import sys

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Erro: Nenhum tipo de caractere selecionado."

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def ajuda():
    print("Uso: python3 phantom.py [tamanho] [opções]")
    print("Opções:")
    print("  --sem-maiusculas      Remove letras maiúsculas")
    print("  --sem-minusculas      Remove letras minúsculas")
    print("  --sem-numeros         Remove números")
    print("  --sem-simbolos        Remove símbolos")
    print("  -h, --help            Mostra esta mensagem")

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        ajuda()
        sys.exit()

    try:
        tamanho = int(sys.argv[1])
    except (IndexError, ValueError):
        tamanho = 12  # valor padrão

    usar_maiusculas = "--sem-maiusculas" not in sys.argv
    usar_minusculas = "--sem-minusculas" not in sys.argv
    usar_numeros = "--sem-numeros" not in sys.argv
    usar_simbolos = "--sem-simbolos" not in sys.argv

    senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
    print(senha)
