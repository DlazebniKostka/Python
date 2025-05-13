ovoce = ["jablko","banán","pomeranč","kiwi","hruška"]

print(ovoce[0])     # jablko
print(ovoce[2])     # pomeranč
print(ovoce[-1])    # hruška


jidlicka = ["svíčková","pizza","kebab"]

print(jidlicka)


znamecky = [1,1,1,3,2,2,1]


zviratka = ["pes","kočka","lev","slepice"]

print(zviratka[1],zviratka[3])


seznamek = []

seznamek.append(1)
seznamek.append(2)
seznamek.append(3)

print(seznamek)


filmy = ["Minecraft movie","Blbý a blbější","Drž hubu"]
velikost = len(filmy)

for i in range (velikost):
    print(filmy[i])


cisla = [69,55,1000000000]
cisla[1]=999
print(cisla)


soucticek = [1,2,3,1,2,3]
print(sum(soucticek))


lenNaPoli = [5,9,45,2,456,36,48,233,68]
print(len(lenNaPoli))


znamky = [1,2,2,1,1,1,3,3]
prumer = (znamky[0]+znamky[1]+znamky[2]+znamky[3]+znamky[4]+znamky[5]+znamky[6]+znamky[7])/len(znamky)

print(prumer)


ovocicko = ["jablko","mrdalinka","šestka","vodní mefloun","banán"]

if "banán" in ovocicko:
    print("Banán je tam!")
else:
    print("Vybral sis špatný pole ty neřáde!")


cisilinka = [1,6,95,100000,9,69,42,66,0]
cislaVetsi = []

if cisilinka[0]>10:

print(cislaVetsi)