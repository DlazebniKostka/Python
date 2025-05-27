def pozdrav():
    print("Helou evryvan!!!")

def dnesni_den():
    print("Dnes je úterý bráško.")

def vypis_cisla():
    cisla = [1,2,3,4,5]
    velikost = len(cisla)
    for i in range (velikost):
        print (cisla[i])

def obdelnik():
    radek = "*****"
    for i in range (3):
        print(radek)

def nalada_dne():
    nalady = ["je to dobrý","kamo nedobrý","bych vsadil veškeré úspory"]
    import random
    print(f"dneska {random.choice(nalady)}.")

print("Zvlote funkci.")
funkce = ["1.Pozdrav","2.Dnešní den","3.Čísla 1 až 5","4.Obdélník z hvězdiček","5.Nálada dne","6.Konec"]
velikost = len(funkce)
for i in range (velikost):
    print (funkce[i])

volba = input()

if volba == "1":
    pozdrav()
elif volba == "2":
    dnesni_den()
elif volba == "3":
    vypis_cisla()
elif volba == "4":
    obdelnik()
elif volba == "5":
    nalada_dne()
else:
    print("konec")
