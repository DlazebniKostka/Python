cisla = [1,2,3,4,5,6,7,8,9,10,69,128,999,123456789]

praniUzivatele = int(input("Jaké číslo si přejete vyhledat? "))

if praniUzivatele in cisla:
    print("Ano, tato hodnota se zde nachází.")
else:
    print("Tato hodnota zde není.") 