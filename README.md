# E-commerce_Final

# Documentação do Projeto de E-commerce

O projeto de E-commerce desenvolvido pelo Grupo 5 utiliza todos os conceitos de Programação Orientada a Objetos adquiridos até o momento do curso. O objetivo do sistema é conter três telas, com a seguinte formatação:

## -> Utilização

### Tela Um - Login

Na Tela Um, encontra-se a área de login com ações que podem ser executadas pelo Cliente e pelo Administrador.

- Ao selecionar 1 no teclado, o usuário será direcionado para a área de login do Cliente, onde ele deve fornecer seu nome e sua senha. Se estas informações estiverem registradas, o cliente existe no sistema, desta forma, terá o acesso liberado e poderá realizar as ações do mesmo. Se o cliente ainda não existe, é necessário que o administrador o registre no sistema.

- Se os dados colocados pelo usuário estiverem incorretos e/ou não existirem, o acesso será negado e retornará ao menu.

- Ao selecionar 3 no teclado, o software fechará.

- Ao selecionar 2 no teclado, o usuário será direcionado para a área de login do Administrador, em que ele deverá fornecer as informações nome e senha como informações de login. Se estas informações estiverem registradas, logo, o Administrador existe no sistema, desta forma, terá o acesso liberado e poderá realizar as ações do mesmo. Se o administrador ainda não existe, é necessário que outro administrador ou o usuário Master o registre no sistema.

### Tela Dois - Ações Cliente

A Tela Dois é acessada a partir do login do Cliente, onde ele poderá realizar as seguintes ações:

- Ao selecionar 1 no teclado, o cliente visualizará os produtos disponíveis no E-commerce. Após essa ação, ele volta ao menu principal.

- Ao selecionar 2 no teclado, o cliente acessará a área de adicionar produtos ao carrinho, onde ele encontrará uma lista de produtos disponíveis na loja, podendo escolher o que deseja. O cliente realizará a ação de colocar o produto no carrinho a partir do input do índice do produto que ele quer. Depois de adicionar, voltará ao menu principal.

- Ao selecionar 3 no teclado, o Cliente visualizará os produtos adicionados em seu carrinho, vendo o índice, nome, descrição e valor dos produtos. Depois de visualizar, voltará ao menu principal.

- Ao selecionar 4 no teclado, o Cliente acessará a área do carrinho novamente, entretanto, com a ação de excluir um produto do mesmo. Ele escolherá o item a ser excluído a partir do input do índice que está sendo indicado na listagem do carrinho. Após realizar a exclusão, o cliente retornará ao menu.

- Ao selecionar 5 no teclado, o Cliente será direcionado para a finalização da compra, onde poderá visualizar quais e quantos produtos estão em seu carrinho. Ao selecionar 1, que corresponde a “SIM”, os valores dos produtos serão somados e mostrados para o cliente e a compra será finalizada.

- Ao selecionar 2, que corresponde a “NÃO”, a conta não será fechada e o Cliente ainda poderá realizar alterações no carrinho.

- Ao selecionar 6 no teclado, o usuário retornará para a Tela Um, onde estão os logins de Cliente e Usuário.

- Ao selecionar 7 no teclado, o sistema fechará.

### Tela Três - Ações Administrador

A Tela Três é acessada a partir do login do Administrador, onde ele poderá realizar as seguintes ações:

- Ao selecionar 1 no teclado, o administrador será direcionado para a área de cadastro de cliente, onde ele deve fornecer as informações de nome, nascimento, CPF, endereço e senha para criar um novo cliente na loja. Após a criação do cliente, o administrador retornará ao menu.

- Ao selecionar 2 no teclado, a lista de clientes existentes na loja será listada e visualizada pelo administrador. Após a visualização, o administrador retornará ao menu.

- Ao selecionar 3 no teclado, o administrador acessará a área de exclusão de cliente. Para realizar essa ação, ele deve fornecer o nome do cliente. Após a exclusão, ele retornará ao menu.

- Ao selecionar 4 no teclado, o ADM logado será direcionado para o cadastro de outro Administrador. Para cadastrar um novo Administrador, ele deverá fornecer o nome e a senha do mesmo. Após o cadastro, será direcionado para o menu.

- Ao selecionar 5 no teclado, o administrador logado poderá listar e visualizar todos os ADMs registrados no sistema.

- Ao selecionar 6 no teclado, o administrador logado será direcionado para a exclusão de administradores. Para realizar essa ação, ele deve visualizar a lista de ADMs existentes e excluir o que deseja a partir do input do índice do mesmo.

- Ao selecionar 7 no teclado, o Administrador será direcionado para a área de cadastro de produtos da loja. Para realizar essa ação, ele deve fornecer o nome, a descrição e o valor do produto. Após o cadastro, ele voltará ao menu.

- Ao selecionar 8 no teclado, o Administrador listará e visualizará todos os produtos cadastrados na loja. Após a visualização, ele retorna ao menu.

- Ao selecionar 9 no teclado, o Administrador acessará todos os produtos disponíveis na loja e poderá excluir quais desejar. Ele deve excluir um de cada vez a partir do input do índice do produto que é mostrado na listagem.

- Ao selecionar 10 no teclado, o Administrador será direcionado para a área de histórico de compras do Cliente. Após a listagem dos clientes existentes, o ADM deve escolher qual deseja consultar o histórico e realizar o input do nome do mesmo para acessar este histórico.

- Ao selecionar 11 no teclado, o Administrador consultará o histórico de compras da loja a partir da listagem e visualização dos produtos escolhidos e levados pelos Clientes.

- Ao selecionar 12 no teclado, o usuário retornará para a Tela Um, onde estão os logins de Cliente e Usuário.

- Ao selecionar 13, o Administrador fechará o sistema.

Atenção aos tipos de informações!

No sistema, utilizamos o Try except para tratar erros do software.

Caso o usuário coloque no input uma informação diferente do que sistema espera, por exemplo, caso digite “faca” em um input de int (número inteiro), o sistema informará que a Opção é inválida.

## → Classes

### **Loja**

#### Construtor (__init__):

- O construtor da classe Loja inclui os atributos "nome", "end" (endereço) e "CNPJ", necessários para criar uma loja. Também possui três listas: "self.clientes" (clientes), "self.produtos" (produtos disponíveis) e "self.ADM" (administradores), onde as informações respectivas são armazenadas, bem como um administrador Master, que é o root (quem tem acesso primário ao software) do sistema.

#### Métodos:

- `getCliente`:
    Método que tem o objetivo de permitir o acesso ao objeto cliente.

- `getADM`: 
    Método que tem o objetivo de permitir o acesso ao objeto administrador.

- `listarCliente`: 
    Essa função lista todos os clientes cadastrados na loja. (Só pode ser executada pelo administrador).

- `adicionarCliente`: 
    Esse método serve para continuar adicionando os clientes a lista “clientes”. Só pode ser executado pelo administrador.

- `excluirCliente`: 
    Este tem a função de excluir um cliente que tenha sido escolhido, pelo administrador, dentro da lista de “clientes”. Só pode ser executada pelo administrador.

- `loginCliente`: 
    Esse método é para que o cliente possa fazer login na loja. É necessário que ele informe seu nome e sua senha e então essa função irá checar se essas informações estão presentes em um algum cadastro dentro da lista “clientes”. Essa função só pode ser executada pelo próprio cliente.

- `listarAdm`: 
    Neste método, são listados os administradores, chamando a lista ADM. Este só pode ser executado pelo administrador.

- `adicionarAdm`:   
    Serve para que novos administradores cadastrados, sejam alocados junto de suas informações dentro da lista ADM.

- `excAdm`: 
    O método irá apagar o cadastro de algum administrador, conforme for informado seu usuário, somente o admin tem acesso a isso.

- `loginAdm`: 
    Esse método foi criado para que o administrador faça log in na loja. Para poder entrar, ele tem que informar seu usuário e sua senha, então a função irá verificar se o informado está presente em algum cadastro da lista de administradores.

- `cadastrarProd`: 
    Essa função foi criada para que os produtos continuem sendo adicionados a lista de produtos, conforme cadastrados.

- `excProd`: 
    Esse método usa do índice do produto na lista, para excluí-lo, conforme informado pelo administrador.

- `getListaProduto`: 
    Esse método “get” irá listar todos os produtos disponíveis na loja, conforme tenham sido cadastrados na lista de produtos, pelo administrador.

### **Clientes**

#### Construtor (__init__):

- O construtor da classe Clientes inclui atributos como "nome", "data" (data de nascimento), "cpf", "ende" (endereço) e "senha", necessários para criar um cliente. Também possui as listas "self.carrinho" e "self.compras", onde os itens do carrinho de cada cliente e o histórico de compras da loja são armazenados, respectivamente.

#### Métodos:

- `addProduto`: 
    Este método é para que o cliente possa adicionar qualquer produto que esteja cadastrado na lista de produtos ao seu carrinho (lista), conforme escolhido.

- `excProduto`: 
    Esse método será usado pelo cliente, para que ele possa excluir algum produto de seu carrinho, conforme escolhido por ele.

- `listarProduto`: 
    Esta função, quando chamada irá listar os produtos disponíveis na loja, apresentando seu nome, descrição e preço por unidade. e relacionando um índice a cada item em ordem crescente.

- `listarCarrinho`: 
    Esse método listará os produtos que o cliente tiver adicionado ao seu carrinho, apresentará seu nome, descrição e preço, e relacionará a um índice.

- `finalizarCompra`: 
    Finaliza a compra após a confirmação do cliente.
    
- `getCompras`: 
    Esse “get” irá retornar a lista “compras” (self.compras).

### **Produtos**

#### Construtor (__init__):

- O construtor da classe Produtos inclui atributos como "nome_prod" (nome do produto), "desc" (descrição) e "preco" (preço).

#### Métodos:

- `getNome_P`: 
    Retorna o nome do produto.
- `getDesc`: 
    Retorna a descrição do produto.
- `getPreco`: 
    Retorna o preço do produto.

### **ADM**

#### Construtor (__init__):

- O construtor da classe ADM inclui atributos como "usuário" e "senha", necessários para criar um administrador. Também possui um dicionário chamado "histórico", onde as compras dos clientes são armazenadas.

#### Métodos:

- Todos os métodos dentro dessa classe só podem ser acessados pelo administrador.
- `cadastrarCliente`: 
    Cria um novo cliente.
- `listarClientes`: 
    Lista todos os clientes cadastrados na loja.
- `excluirClientes`: 
    Exclui um cliente cadastrado.
- `cadastrarProduto`: 
    Adiciona produtos à lista de produtos disponíveis.
- `excluirProduto`: 
    Exclui um produto da lista de produtos disponíveis.
- `cadastrarAdm`: 
    'Cadastra novos administradores.
- `listarAdms`: 
    Lista todos os administradores cadastrados.
- `excluirAdm`: 
    Exclui o cadastro de um administrador.
- `historicoCompras`: 
    Mostra o histórico de compras de cada cliente.
- `vendasLoja`: 
    Mostra todas as vendas da loja.
