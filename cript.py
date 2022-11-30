# Add on Github 29/11/2022
# Codificador e decodificador de caracteres
def determinaOpcao():
    #Funcao que determina d ou f, e garante loop
    while True:
        opcao=input("Deseja criptograr ou decriptografar a mensagem\n").lower()
        
        if opcao in 'criptografar c decriptografar d'.split():
            return opcao
        else:
            print("Digite 'c' ou 'd'.")

def determinaChave():
    chave = 0
    while True:
        chave = int(input("Digite o valor da chave: [1 - 26]\n"))
        if 1 <= chave <= 26:
            return chave

def determinaMensagem(opcao, mensagem, chave):
    #Confere a opcao do usuario
    traduzido = ''
    if opcao[0] == 'd':
        chave *= -1
    #Ciptografia e Decriptografia
    for letra in mensagem:
        if letra.isalpha():
            num = ord(letra) #ASCII chr()
            num += chave
            if letra.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letra.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduzido += chr(num)
        else:
            traduzido += letra
    return traduzido

def main():
    opcao = determinaOpcao()
    mensagem = input("Entre com sua frase:\n")
    chave = determinaChave()
    print("Sua frase traduzida e: ")
    print(determinaMensagem(opcao, mensagem, chave))
main()

# END OF CODE !!!
