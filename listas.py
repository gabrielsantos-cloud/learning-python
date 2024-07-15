programadores = ["Gabriel", "Carlos", "Savio", "Kleyton", "Ronaldo"]

print(programadores)

print(programadores[0])
print(programadores[1])
print(programadores[2])
print(programadores[3])
print(programadores[4])

print(programadores.__len__())
print(len(programadores))

programadores.append("Cristina")
print(programadores)
print(len(programadores))

programadores.insert(0, "Heloisa")
print(programadores)

programadores.remove("Gabriel")
print(programadores)

programadores.pop(0)
print(programadores)

print(type(programadores))

print(min(programadores))
print(max(programadores))