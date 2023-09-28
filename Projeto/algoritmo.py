from classe import *
import os

def Main():

    while True:
        try:
            print("---Bem Vindo Dev Five Ecommerce---")
            print("Escolha uma opção \n [1] Login Cliente \n [2] Login ADM \n [3] Sair")
            escolha1 = int(input(">> "))
            match escolha1:
                case 1:
                    os.system("cls")
                    print("--Para fazer o login, preencha--")
                    nomee_cli = input("Nome: ")
                    senhha = int(input("Senha: "))

                    acesso = loja.loginCliente(nomee_cli, senhha)
                    print (acesso)
                    
                    m = 1
                    while m == 1:
                        
                        match acesso:
                            case 'ACESSO LIBERADO':
                                print("Página do cliente")
                                print("Escolha uma opção \n [1] Produtos disponiveis \n [2] Adicionar produto ao carrinho \n [3] Visualizar carrinho \n [4] Excluir produto \n [5] Finalizar compra \n [6] Retornar ao menu \n [7] Log Out" )
                                escolha2 = int(input(">> "))
                                match escolha2:
                                    case 1:
                                        os.system("cls")
                                        print("Estes são os produtos disponíveis na loja:")
                                        loja.listarProduto()
                                        os.system("pause")

                                    case 2:
                                        os.system("cls")
                                        loja.listarProduto()
                                        print (" ")
                                        print("Escolha o produto que deseja e digite seu índice para adiciona-lo ao carrinho")
                                        indice = int(input(">> "))
                                        loja.getCliente(nomee_cli, senhha).addProduto(indice)
                                        os.system("pause")
                                        # print ("Você deseja adcionar mais algum produto? \n [1] Sim \n [2] Não ")
                                        # sn = int(input(">> "))

                                        # c = 1
                                        # while c == 1:

                                        #     match sn:
                                        #         case 1:
                                        #             c = 0
                                        #         case 2:
                                        #             m = 0
                                        #             os.system("cls")

                                        # os.system ("pause")

                                    case 3:
                                        os.system("cls")
                                        print("Esse é seu carrinho: ")
                                        loja.getCliente(nomee_cli, senhha).listarCarrinho()
                                        os.system("pause")
                                    case 4:
                                        os.system("cls")
                                        exc = int (input("Digite o índice do produto que deseja excluir:"))
                                        loja.getCliente(nomee_cli, senhha).excProduto(exc)
                                        os.system("pause")
                                    case 5:
                                        os.system("cls")
                                        loja.getCliente(nomee_cli, senhha).listarCarrinho()
                                        print("Você deseja excluir algum produto do carrimho?\n [1] Sim \n [2] Não")
                                        eexc = int(input(">>"))
                                        match eexc:
                                            case 1:
                                                exc1 = int (input("Digite o índice do produto que deseja excluir:"))
                                                loja.getCliente(nomee_cli, senhha).excProduto(exc1)
                                                print("Você deseja finalizar sua compra?\n [1] Sim\n [2] Não")
                                                resFinalizar = int(input(">> "))
                                                match resFinalizar:
                                                    case 1:
                                                        loja.getCliente(nomee_cli, senhha).finalizarCompra()
                                                
                                                    case 2:
                                                        os.system("cls")
                                            case 2:
                                                print("Você deseja finalizar sua compra?\n [1] Sim\n [2] Não")
                                                resFinalizar = int(input(">> "))
                                                match resFinalizar:
                                                    case 1:
                                                        loja.getCliente(nomee_cli, senhha).finalizarCompra()
                                                
                                                    case 2:
                                                        os.system("cls")
                                        os.system ("pause")

                                    case 6:
                                        print("Retornar ao menu...")
                                        m = 0
                                        os.system("cls")
                                    case 7:
                                        print ("Saindo...")
                                        break
                                    case _:
                                        print("Opção Inexistente")
                                        
                            case _:
                                os.system("cls")
                            
                case 2:
                    os.system("cls")
                    print("--Para fazer o login como administrador, preencha--")
                    nomee_adm = input("Usuário: ")
                    senhha_adm = int(input("Senha: "))

                    acessoAdm = loja.loginAdm(nomee_adm, senhha_adm)

                    print(acessoAdm)
                    
                    n = 1
                    while n == 1:
                
                        match acessoAdm:
                            case 'ACESSO LIBERADO':
                                os.system ("cls")
                                print("Página do Administrador")
                                print("Escolha uma opção \n [1] Cadastrar cliente \n [2] Listar cliente \n [3] Excluir cliente \n [4] Cadastrar administrador \n [5] Listar administrador \n [6] Excluir administrador \n [7] Cadastrar produtos \n [8] Listar produtos \n [9] Excluir produtos \n [10] Visualizar historico de compras dos clientes \n [11] Visualizar historico de vendas da loja \n [12] Voltar ao menu \n [13] Log out")
                                escolha3 = int(input(">> "))
                                match escolha3:
                                    case 1:
                                        os.system ("cls")
                                        print("--Cadastrar novo cliente-- \n ")
                                        print("Para fazer o cadastro, preencha as informações abaixo: ")
                                        nome = input("Nome: ")
                                        data_nasc =input("Data de nascimento: ")
                                        cpf = int(input("CPF: "))
                                        endereco = input("Endereço: ")
                                        senha = int(input("Senha: "))
                                        loja.getADM(nomee_adm, senhha_adm).cadastrarCliente(nome,data_nasc,cpf,endereco,senha)
                                        print("Novo cliente cadastrado")
                                        os.system("pause")

                                    case 2:
                                        os.system ("cls")
                                        print("--Clientes cadastrados--")
                                        loja.getADM(nomee_adm, senhha_adm).listarClientes()
                                        os.system ("pause")

                                    case 3:
                                        os.system("cls")
                                        print("--Exclusão de clientes--")
                                        loja.listarCliente()
                                        print("------------------------")
                                        nomme = int(input("Informe o índice do cliente que deseja excluir: "))
                                        loja.getADM(nomee_adm, senhha_adm).excluirCliente(nomme)
                                        print("Cliente excluído com sucesso!")
                                        os.system ("pause")

                                    case 4:
                                        os.system("cls")
                                        print("--Cadastrar novo ADM--")
                                        print("Para fazer o cadastro, preencha as informações abaixo: ")
                                        usuario = input("Usuário: ")
                                        senh = int(input("Senha: "))
                                        loja.getADM(nomee_adm, senhha_adm).cadastrarAdm(usuario,senh)
                                        print("Novo administrador cadastrado com sucesso!")
                                        os.system("pause")

                                    case 5:
                                        os.system ("cls")
                                        print("--Administradores cadastrados--")
                                        loja.getADM(nomee_adm, senhha_adm).listarAdms()
                                        os.system("pause")

                                    case 6:
                                        os.system("cls")
                                        print("--Exclusão de administradores--")
                                        loja.ListarAdm()
                                        print("-------------------------------")
                                        user = int(input("Informe o índice do adm que deseja excluir: "))
                                        loja.getADM(nomee_adm, senhha_adm).excluirAdm(user)
                                        print("Cliente excluído com sucesso!")
                                        os.system("pause")

                                    case 7:
                                        os.system("cls")
                                        print("--Cadastro de produtos--")
                                        pro = input("Nome do produto: ")
                                        des = input("Descrição:")
                                        preco = float(input("Preço: "))
                                        loja.getADM(nomee_adm, senhha_adm).cadastrarProduto(pro,des,preco)
                                        print(" Produto cadastrado! ")
                                        os.system("pause")

                                    case 8:
                                        os.system("cls")
                                        print("--Lista de produtos cadastrados--")
                                        loja.listarProduto()
                                        os.system("pause")

                                    case 9:
                                        os.system("cls")
                                        print("--Exclusão de produtos--")
                                        loja.listarProduto()
                                        print("------------------------")
                                        proo = int(input("Informe o índice do produto que deseja excluir: "))
                                        loja.getADM(nomee_adm, senhha_adm).excluirProduto(proo)
                                        print("Produto excluído com sucesso!")
                                        os.system("pause")

                                    case 10:
                                        os.system("cls")
                                        print("--Clientes cadastrados--")
                                        loja.getADM(nomee_adm, senhha_adm).listarClientes()
                                        hiscli = input ("Qual o nome do cliente que você deseja olhar o histórico?")
                                        loja.historicoCompras(hiscli)
                                        os.system("pause")

                                    case 11:
                                        os.system("cls")
                                        print("--Vendas da Loja--")
                                        loja.vendasLoja()
                                        os.system("pause")
                                        
                                    case 12:
                                        n = 0
                                        os.system('cls')
                                    case 13:
                                        break
                                    case _:
                                        print("Opção Inexistente")
                            case _:
                                os.system("cls")
                case 3:
                    break

                case _:
                    print("Opção Inexistente")
                    
        except Exception as error:
            print("Opção Inválida")
            print(error.__class__.__name__)