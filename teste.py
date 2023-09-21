lista = ["arroz", "feijão", "macarrão"]

carrinho = []
indice = 2
for i in lista:
    if i == lista[indice - 1]:
        carrinho.append(i)
        print(carrinho)
        break