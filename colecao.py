def adicionarFinal(vetor,quant,elemento): 
    ind = -1
    for i in vetor:
        if vetor[ind] == '0':
            vetor[ind] = elemento
            quant += 1
            print("Operação realizada!")
            break
        elif vetor[ind] != '0':
            ind -= 1
        else:
            print("Coleção cheia. Impossível realizar operação.")
    return quant

def adicionarPosicao(vetor,quant,elemento,posicao): 
    if vetor[posicao] == '0': 
        vetor[posicao] = elemento
        quant += 1
        print("Operação realizada!")
            
    elif vetor[posicao] != '0':
        print("Operação inválida. Posição ocupada.")
                
        
    return quant

def removerPosicao(vetor,quant,posicao):
    if vetor[posicao] == '0':
        print("Não há nenhum elemento nesta posição.")

    elif vetor[posicao] != '0':
        vetor[posicao] = '0'
        quant -= 1
        print("Operação realizada!")

    return quant

def removerPrimOcorr(vetor,quant,elemento):
    if elemento not in vetor:
        print("\nOperação inválida. Não existe tal elemento na coleção.")

    else:
        for i in range(len(vetor)):
            if vetor[i] == elemento:
                vetor[i] = '0'
                quant -= 1
                print("Operação realizada!")
                break
                
    return quant

def removerTodas(vetor,quant,elemento):
    if elemento not in vetor:
        print("\nOperação inválida. Não existe tal elemento na coleção.")
        
    else:
        for i in range(len(vetor)):
            if vetor[i] == elemento:
                vetor[i] = '0'
                quant -= 1
        print("Operação realizada!")
                
    return quant

def verifica(vetor,quant,elemento):
        if elemento in vetor:
            for i in range(len(vetor)):
                if vetor[i] == elemento:
                    print("Elemento no indície ",i)
            
        elif elemento not in vetor:
            print("-1")

def verificaSoma(vetor,quant,valor): 
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            resultado = int(vetor[i]) + int(vetor[j])
            if i == j:    #Para não somar o mesmo elemento, por estar no mesmo índice.
                pass
            else:
                if resultado == valor:
                    return True
                    break
    return False


def main():
    colecao = ['0'] * 100
    quantidade = 0
    while True:
        print("\n1. Adicionar um elemento no final da coleção.")
        print('2. Adicionar um elemento em uma posição da coleção.')
        print('3. Remover um elemento em uma posição na coleção.')
        print('4. Remover a primeira ocorrência do elemento na coleção.')
        print('5. Remover todas as ocorrências de um elemento na coleção.')
        print('6. Verificar se dado um elemento está contido na coleção.')
        print('7. Verificar se dado um elemento existem dois elementos na coleção que somados é igual a um valor informado.')
        print('8. Sair')

        opcao = int(input("\nInsira o número da opção que deseja utilizar: "))        

        while opcao < 1 or opcao > 8:
            print("\nOpção inválida. Tente novamente:")
            opcao = int(input())

        if opcao == 1:
            elemento = int(input("\nInsira qual elemento deseja adicionar: "))
            quantidade = adicionarFinal(colecao,quantidade,elemento)
            
            
        elif opcao == 2:
            elemento = int(input("\nInsira qual elemento deseja adicionar: "))
            posicao = int(input("Insira qual posição deseja inseri-lo: "))
            quantidade = adicionarPosicao(colecao,quantidade,elemento,posicao)
            

        elif opcao == 3:
            posicao = int(input("\nInsira de qual posição deseja remover o elemento: "))
            quantidade = removerPosicao(colecao,quantidade,posicao)
            

        elif opcao == 4:
            elemento = int(input("\nInsira qual elemento deseja remover a primeira ocorrência: "))
            quantidade = removerPrimOcorr(colecao,quantidade,elemento)
        

        elif opcao == 5:
            elemento = int(input("\nInsira qual elemento deseja remover todas as ocorrências: "))
            quantidade = removerTodas(colecao,quantidade,elemento)
            

        elif opcao == 6:
            elemento = int(input("\nInsira qual elemento deseja verificar se está contido na coleção: "))
            verifica(colecao,quantidade,elemento)

        elif opcao == 7:
            soma = int(input("\nInsira o valor da soma que deseja verificar: "))
            print(verificaSoma(colecao,quantidade,soma))

        elif opcao == 8:
            break


main()
