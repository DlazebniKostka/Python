#načtení od uživatele
#Pokud potřebujeme načíst nějakou hodnotu od uživatele, použijeme input.

i = input()

#vypsat
#Pokud potřebujeme cokoli vypsat pro uživatele, použijeme print. 

print("Hello world")

#přetypování
#pokud potřenujeme změnit typ proměnné, přetypujeme ji.

i = input()             #proměnná je typu string, potřebujeme integer

i = int (input())       #proměnná je už typu integer

#typů proměnných je více

#podmínky (if, elif, else)
#Pokud potřebujeme vytvořit podmínku, použijeme if, elif, else

if i == 1:
    print("Ahoj!")              #podmínka se skládá z podmínky if a else, pokud je podmínka splněna uskuteční se příkaz if, pokud se podmínka nesplní uskuteční se else

elif i == 2:
    print("Nazdar!")            #pokud potřebujeme zadat více než jednu podmínku použijeme elif, mužeme použít kolikrát chceme

else:
    print("Dobrý den.")

#důležité jsou tabulátory pod podmínkami, s jejich pomocí můžeme zadávat podmínky do podmínek  


#logické operátory (and, or, not)
#Používají se v podmínkách

if i == 4 or i == 5:
    print("Čau!")


#github příkazy
#Používáme pro propojení souboru s githubem

#git add *
#git commit -m "tot"
#git push

#Adam Říha