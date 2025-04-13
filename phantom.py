import random
import string

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
        return "Erro: deve-se selecionar pelo menos um tipo de caractere!"

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
tamanho = int(input("Comprimento da senha: "))
senha = gerar_senha(tamanho)
print(f"Senha gerada: {senha}")
