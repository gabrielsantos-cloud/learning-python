dados_cliente = {
    'Nome': "Gabriel",
    'Endereco': 'Rua cruzeiro do Sul',
    'Telefone': '987654321'
}

print(dados_cliente)

dados_cliente['Idade'] = 18

print(dados_cliente)

dados_cliente.pop('Telefone', None)

print(dados_cliente)

del dados_cliente['Nome']

print(dados_cliente)

print(len(dados_cliente))

print(type(dados_cliente))