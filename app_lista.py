

#Etapa 1 Crie uma lista com os nomes de 5 objetos.
frutas = ['maça', 'banana', 'pera', 'maracuja', 'laranja']
print('Lista de Frutas criadas')
print("+", "-" * 30, "+")

#Etapa 2 Adicione mais um objeto ao final da lista.
frutas.append('pokan')
print("Adicionar pokan no final lista de frutas")
print("+", "-" * 30, "+")

#Etapa 3 Acesse o objeto que está na 2a posição.
frutas[2]
print('Acessa o elemento na posição 2 da lista')
print("+", "-" * 30, "+")

#Etapa 4 Remova um objeto da lista.
frutas.remove('banana')
print("Remover banana na lista de frutas")
print("+", "-" * 30, "+")

#Etapa 5 Exiba o tamanho da lista.
len(frutas)
print('Número de frutas da lista de frutas')
print("+", "-" * 30, "+")

#Etapa 6 Mostre todos os itens com um laço for.
for fruta in frutas:
    print(fruta)
    print('Percorre a lista, acessando um item por vez.')
print("+", "-" * 30, "+")

#Etapa 7 Verifique se 'cadeira' está na lista. Se sim remova-a, senão adicione.
if "banana" in frutas:
    frutas.remove("banana")
else:
    frutas.append("banana")
print('in: Verifique se banana está na lista. Se sim remova-a, senão adicione.')
print("+", "-" * 30, "+")

#Etapa 8. Ordene a lista em ordem alfabética.
frutas.sort()
print('Ordena os elementos da lista.')
print("+", "-" * 30, "+")

#Etapa 9 Exiba o primeiro e o último objeto.
frutas_um = frutas[0]
print('primeira fruta,', frutas_um)

frutas_ultimo = frutas[len(frutas)-1]
print('ultima fruta,', frutas_ultimo)

print('Exibir o primeiro e o ultimo elemento.')
print("+", "-" * 30, "+")

#Etapa 10 Limpe toda a lista
frutas.clear()
print("Remover todos os itens da lista")

