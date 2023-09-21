class Loja:
    def __init__(self, nome, end, CNPJ):
        self.nome = nome
        self.end = end
        self.CNPJ = CNPJ
        self.clientes = []
        self.produto = []
        self.ADM = []
        self.Master = ADM("Master", 123)
        
    def getMaster(self):
        return self.Master  
    
    
    ##########################################
    #Cliente

    def listarCliente(self):
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome_cli}, Data de Nascimento: {cliente.data}, CPF: {cliente.cpf}, Endereço: {cliente.ende}")
    
    def adicionarCliente(self, cliente):
        self.clientes.append(cliente)
        
    def excluirCliente(self, cliente):
        self.clientes.pop(cliente)
    
    def loginCliente(self, nome_cli, senha):
        for cliente in self.clientes:
            if cliente.nome == nome_cli and cliente.senha == senha:
                return "ACESSO LIBERADO"
            else:
                return "ACESSO NEGADO. Digite os dados novamente ou faça seu cadastro."

    ##############################################
    #ADM

    def ListarAdm(self):
        for adm in self.ADM:
            print(f"Usuario: {adm.usuario}")

    def adicionarAdm(self, adm):
        self.ADM.append(adm)

    def loginAdm(self, usuario, senha):
        for adm in self.ADM:
            if adm.usuario == usuario and adm.senha == senha:
                return "ACESSO LIBERADO"
            else:
                return "ACESSO NEGADO. Digite novamente ou faça seu cadastro."
            
    def excAdms(self, excAdm):
        self.ADM.pop(excAdm)

    #################################################
    #Produtos
    
    def cadastrarProd(self,products):
        self.produto.append(products)
        
    def excluirProd(self,product):
        product =-1
        self.produto.pop(product)
        
    def getListaProduto(self):
        return self.produto
        

    
class Cliente:
    def __init__(self, nome_cli, data, cpf, ende, senha):
        self.nome_cli = nome_cli
        self.data = data
        self.cpf = cpf
        self.ende = ende
        self.senha = senha
        self.carrinho = []
    
   

######################################
# Ana Júlia

    def addProduto(self, indice):
        for produto in loja.getListaProduto():
            if produto == loja.getListaProduto()[indice - 1]:
                self.carrinho.append(produto)
                break
            else:
                ("Produto não disponível")             

    def excProduto(self,indice):
        for produto in self.carrinho:
            if produto == self.carrinho[indice - 1]:
                self.carrinho.pop(indice - 1)
                break
            else:
                print("Este produto não está no carrinho")

#####################################
# Arthur Matheus de Moura  
    def listarProduto(self):
        number = 0
        for i in loja.getListaProduto():
            number += 1
            print(f"{number}- Nome: {i.getNome_P()} | Descrição: {i.getDesc()} | Preço: R${i.getPreco()}") 
    
    def listarCarrinho(self):
        number = 0
        for i in self.carrinho:
            number += 0
            print(f"{number}- Nome: {i.getNome_P()} | Descrição: {i.getDesc()} | Preço: R${i.getPreco()}")

############################################
    def finalizarCompra(self):
        total = 0
        for i in self.carrinho:
            total += i.getPreco()
            return total
        self.compras = self.carrinho[:]
        del self.carrinho 


class Produtos:
    def __init__(self, nome_prod, desc, preco):
        self.nome_prod = nome_prod
        self.desc = desc
        self.preco = preco  
        
    def getNome_P(self):  
        return self.nome_prod
    
    def getDesc(self):
        return self.desc
    
    def getPreco(self):
        return self.preco

class ADM:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.cliente = None

#########################################
#############  CLIENTE   #################
    def cadastrarCliente(self, nome_cli, data, cpf, ende, senha):
        cliente = Cliente(nome_cli, data, cpf, ende, senha)
        loja.adicionarCliente(cliente)
    
    def listarClientes(self):
        loja.listarCliente()

    def excluirCliente(self, cliente):
        loja.excluirCliente(cliente)
    
#########################################
############   PRODUTO  ################
    def cadastrarProduto (self, nomeprod, desc,preco):
        prod = Produtos(nomeprod,desc,preco)
        loja.cadastrarProd(prod)
   
    def excluirProduto(self,exc):
        loja.excluirProd(exc)

#########################################
############   ADM   ################
    def cadastrarAdm(self, usuario, senha):
        adm = ADM(usuario, senha)
        loja.adicionarAdm(adm)
        
    def listarAdms(self):
        loja.ListarAdm()

    def excluirAdm(self, adm):
        loja.excAdms(adm)

    def comprasCliente(self):
        pass

    def vendasLoja(self):
        pass


loja = Loja("Dev5 ecommerce", "Av.Brasil, Itupeva, nº595", 134978740001-71)