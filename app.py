import os 

restaurantes = [{"nome" : "Padaria", "categoria" : "Comercio", "contato" : "11 977155199", "cnpj" : "045627/0001-91", "ativo" : True}, 
                {"nome" : "Sushi", "categoria" : "Japones", "contato" : "21 9876555199", "cnpj" : "076543/0001-12", "ativo" : False}, 
                {"nome" : "Pizzaria", "categoria" : "pizza", "contato" : "44 409763129", "cnpj" : "3427/0001-89", "ativo" : False}]

def mensagem_inicial():
    """Função de mostragem da mensagem inicial do nosso app"""
    
    
    print("𝗦𝗲𝗷𝗮 𝗯𝗲𝗺-𝘃𝗶𝗻𝗱𝗼 𝗮𝗼 𝗦𝗮𝗯𝗼𝗿 𝗘𝘅𝗽𝗿𝗲𝘀𝘀❗\n")

def opcoes_de_uso():
    """Função responsável por mostrar o menu de opções para o usuário"""""
    
    print("1. Cadastrar restaudante")
    print("2. Listar restaudantes")
    print("3. Alterar o status do restaurante")
    print("4. Sair do aplicativo\n")

def encerrar_app():
    """Esta função faz o encerramento do aplicativo
    
    Output: 
    - Encerramento do programa
    """
    
    #print ("cls") - para uso no windows 
    os.system("clear")
    mensagens_subtitulos("𝗘𝗻𝗰𝗲𝗿𝗿𝗮𝗻𝗱𝗼 𝗼 𝗽𝗿𝗼𝗴𝗿𝗮𝗺𝗮...")

def retornar_menu_principal():
    """Essa função faz retornar ao menu principal do app, após uma escolha errada das opções ou quando o cliente já fez o que deseja e quer retornar
    
    Input:
    - Retonar ao menu principal do nosso aplicativo
    
    """
    
    input("\nPor favor clique em qualquer tecla para voltar ao menu principal")
    main()  

def opcao_invalida():
    """Esta função informa ao usuário que a opção escolhida no menu principal é inválido
    
    Output:
    - Informa ao usuário que a opção escolhida é inválida
    """
    
    mensagens_subtitulos("Você digitou uma opção inválida \n")
    retornar_menu_principal()

def mensagens_subtitulos(texto):
    """Função responsável por declarar a limpeza do terminal e mostrar a menasgem da opção escolhida anteriomente pelo user on app
    
    Output:
    - os.system para limpar nosso terminar 
    - Linha para adicionar "*" em nosso subtitulo
    
    """
    
    os.system("clear")
    linha = "*" * (len(texto))
    print(linha) 
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    """Essa função serve para cadastrar novos restaurantes
    
    Input:
    - Cadastro do restaurante com: nome, categoria, contato, cnpj
    
    Output:
    - Colocar o novo restaurante na lista de restaurantes
    
    """

    mensagens_subtitulos("Seja bem-vindo ao cadastro de restaurantes!\n")
   
    nome_do_restaurante = input(f"Por favor digite o nome do restaurante: ")
    
    categoria_restaurante = input(f"Por favor digite a categoria do restaurante {nome_do_restaurante}: ")
    
    telefone_contato = input(f"Por favor informe o número de contato do restaurante {nome_do_restaurante} com DD: ")
   
    cnpj_do_restaurante = input(f"Por favor digite o CNPJ do restaurante {nome_do_restaurante}: ")
    
    dados_do_resturante = {"nome":nome_do_restaurante , "categoria":categoria_restaurante , "contato":telefone_contato, "cnpj":cnpj_do_restaurante, "ativo": False }
    restaurantes.append(dados_do_resturante)
    
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    retornar_menu_principal()
   
def listar_restaurantes():
    """Função responsável por cadastrar todos os restaurantes da nossa lista
    
    Output:
    - Listagem dos restaurantes que contém na lista
    
    """
    
    mensagens_subtitulos("Você selecionou a listagem de restaurante, segue abaixo: \n")
    
    print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Contato".ljust(20)} | {"CNPJ".ljust(25)} | Status")
    
    for restaurante in restaurantes:
        
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        contato_restaurante = restaurante["contato"]
        cnpj_restaurante= restaurante["cnpj"] 
        ativo_restaurante = "ativo" if restaurante["ativo"] else "desativado"
       
        print(f"{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {contato_restaurante.ljust(20)} | {cnpj_restaurante.ljust(20)} | {ativo_restaurante}")    
    retornar_menu_principal() 

def alternar_status_restaurante():
    """Esta função faz com que conseguimos alternar o status do nosso restautante, para o que esta ativo se torna desativado e o desativado se torna ativo
    
    Input:
    - Nome do restaurante que deseja alterar status
    
    Output:
    - Mudar o status do restaurante
    """
    
    mensagens_subtitulos("Alterando stutus do restaurante")
    
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o status: ")
   
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi alterado o status com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            
            print(mensagem)
            
    if not restaurante_encontrado:
        print(f"O restaurante {nome_restaurante} não foi encontrado")
    
    retornar_menu_principal()
      
def opcoes_escolhidas():
    """Esta função faz uma tentativa de reconhecer o input do usuário para saber se é um int e se bate com as opções existentes, e caso existe segue o código, se não ele da a opção de retornar ao menu principal
    
    Input:
    - Informar a opção do menu principa
    
    """
    
    try:
        selecionar_opcao = int(input("Por favor, selecione a ação que deseja fazer (Basta digitar o número correspondente): ")) 
        
        if(selecionar_opcao == 1):
            cadastrar_novo_restaurante()
        elif(selecionar_opcao == 2):
            listar_restaurantes()
        elif(selecionar_opcao == 3):
            alternar_status_restaurante()
        elif(selecionar_opcao == 4):
            encerrar_app()
        else:
            opcao_invalida()        
    except: 
        opcao_invalida()

def main():
    """Função princiapl do app, onde ele armazena todas as principais funcionalidades do nosso programa"""
    
    os.system("clear")
    mensagem_inicial()
    opcoes_de_uso()
    opcoes_escolhidas()
      
if __name__ == "__main__":
    """Condição para rodar nosso app"""
    
    main()

 

    

