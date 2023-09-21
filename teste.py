lista = ["arroz", "feijão", "macarrão"]

carrinho = []
indice = 1
for i in lista:
    if i == lista[indice - 1]:
        carrinho.append(i)
        print(carrinho)
        break

for produto in carrinho:
    if produto == carrinho[indice - 1]:
        carrinho.pop(indice - 1)
        print(carrinho)
        break
    else:
        print("Este produto não está no carrinho")