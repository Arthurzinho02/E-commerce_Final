class Loja:
    def __init__(self, nome, end, CNPJ):
        self.nome = nome
        self.end = end
        self.CNPJ = CNPJ
        self.cliente = {}
        self.produto = []
        self.ADM = {}
        self.Master = ADM("Master", 123)
        
    def getMaster(self):
        return self.Master

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
    def add_produto(self, indice):

        #listar produtos aqq
        produto_escolhido = indice - 1
        # if self.produto[produto_escolhido] in self.produto:
            self.carrinho.append(produto_escolhido)
            print(f"Produto adicionado")
        else: 
            print("Esse produto não existe")
            

    def exc_produto(self,indice):
        pass

#####################################
# Arthur Matheus de Moura  
    def listar_produto(self):
        pass
    
    def listar_carrinho(self):
        pass

class Produtos:
    def __init__(self, nome_prod, desc, preco):
        self.nome_prod = nome_prod
        self.desc = desc
        self.preco = preco
        
        

class ADM (Cliente, Loja):
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.cliente = None

#########################################
#############    DUDA   #################
    def cadastrar_cliente(self, nome_cli, data, cpf, ende, senha):
        self.cliente[nome_cli] = {'Data de Nascimento': data, 'CPF': cpf, 'Endereço':ende, 'Senha': senha}
    
    def listar_clientes(self):
        pass

    def excluir_cliente(self):
        pass
    
#########################################
############   LETICIA   ################
    def cadastrar_produto (self, nomeprod, desc,preco):
        prod = Produtos(nomeprod,desc,preco)
        self.produto.append(prod)
        
        
    def excluir_produto(self,prodd):
        
        self.produto.pop(prodd)

#########################################
############   NATALIA   ################
    def cadastrar_adm(self, usuario, senha):
        self.ADM[usuario] = {'Senha': senha}

    def listar_adms(self):
        pass

    def excluir_adm(self):
        pass

