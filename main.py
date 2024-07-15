for left in range(10):
    for right in range(left, 10):
        if(right == 9):
            print("[" + str(left) + "|" + str(right) + "]", end=" ")
        else:    
            print("[" + str(left) + "|" + str(right) + "]", end="-")
    print()

name = "Gabriel"

for index in name:
    if(index == "a" or index == "e"):
        index = "Capa Toma"
    print(index)

index = 10

while index > len(name):
    index = index - 1
    print(index)
    

print(name[1:4])
print(name[1:2])
print(name[1:3])
print(name[1:5])
print(name[::-1])

second_name = ["Santos"]
vazio = ""

print(name.join(second_name))
print(vazio.join(second_name))
for n in range(19):
    if n % 2 == 0:
        print(n)

print(True + 1)        


