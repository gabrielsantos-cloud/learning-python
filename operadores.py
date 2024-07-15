soma = 1 + 1
subtrcao = 1 - 1
multiplicacao = 2 * 2 
divisao = 10 / 2
divisao_inteira = 10 // 2
modulo = 10 % 2
exponenciacao = 2 ** 5

print(soma)
print(subtrcao)
print(multiplicacao)
print(divisao)
print(divisao_inteira)
print(modulo)
print(exponenciacao)

print((2 + 5) * 2)

print(1 + 5 ** 2)

numero_1 = 10
print(numero_1)
numero_1 += 5
print(numero_1) 
numero_1 -= 5
print(numero_1)
numero_1 *= 2
print(numero_1)
numero_1 /= 2
print(numero_1)
numero_1 %= 2
print(numero_1)

numero_2 = 10

print(numero_1 > numero_2)
print(numero_1 < numero_2)
print(numero_1 == numero_2)
print(numero_1 >= numero_2)
print(numero_1 <= numero_2)
print(numero_1 != numero_2)

print(numero_1 == 1 and numero_2 < 20)
print(numero_1 == 1 or numero_2 < 20)
print(not(numero_1 == 1 or numero_2 < 20))

time_brasil = "Brasil"
time_russia = "Russia"

print(time_brasil is time_russia)
print(time_brasil is not time_russia)

frutas = ["Banana", "Abacate", "Mamao", "Tomate"]

fruta_1 = "Banana"
fruta_2 = "Limao"

print(fruta_1 in frutas)
print(fruta_2 in frutas)

num1 = 0
num2 = 0

for sum in range(5):
    sum += sum
    print(sum)