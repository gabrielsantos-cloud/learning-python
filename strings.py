nome = "Gabriel"
outroNome = "Gabriel"

if nome == outroNome:
    print("Iguais")

if nome is outroNome:
    print("Iguais também")

mensagem = "Meu nome é Gabriel e eu desejo uma otima semana para você"
novaMensagem = mensagem.split(" ")
print(novaMensagem)
print(id(nome))

print(mensagem.upper())
print(mensagem.lower())
print(nome.replace("a", "i"))
