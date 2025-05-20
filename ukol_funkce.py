def pozdrav():
    print("ahoj")

pozdrav()

#ukol1
def soucet():
    print(3+2)

soucet()

#ukol2
def jmeno():
    jmeno = input()
    print(f"Ahoj {jmeno}.")

jmeno()

#ukol3
def znamky():
    znamky = [1,2,3,4,5]
    prumer = (znamky[0]+znamky[1]+znamky[2]+znamky[3]+znamky[4])/len(znamky)
    print(prumer)
znamky()

#ukol4
def nevimUz():
    print("Ahoj!")

for i in range (5):
    nevimUz()