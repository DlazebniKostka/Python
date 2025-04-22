jmena = ["Petr", "Karel", "Franta", "Honza", "Lukáš", "Adam"]

delkaPole = len(jmena)
print(delkaPole)

for cyklus in jmena:
    print(cyklus)

dalsiJmena = input("Napiš jméno. ")
jmena.append(dalsiJmena)
print(jmena)

jmena.pop(0)

jmena.sort()

jmena.reverse()

print(jmena)