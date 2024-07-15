idade = 18

if idade > 18: 
    print("Pode passar")
else:
    print("Não pode passar")

if idade >= 10 and idade < 20:
    print("Você é adolescente")
elif idade >= 20 and idade <= 30:
    print("Você é jovem")
elif idade >= 30 and idade <= 100:
    print("Você é adulto")
else:
    print("Valor encontrado")