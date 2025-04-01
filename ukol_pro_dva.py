#úkol A: Adam Říha

print ("Napište 3 jídla, které jste snědl/a a kolik měla tato jídla přibližně kalorií.")

jidlo1 = input ("první jídlo ")
kalorie1 = int (input ("kalorie prvního jídla "))

jidlo2 = input ("druhé jídlo ")
kalorie2 = int (input ("kalorie druhého jídla "))

jidlo3 = input ("třetí jídlo ")
kalorie3 = int (input ("kalorie třetího jídla "))

celkove_kalorie = kalorie1 + kalorie2 + kalorie3


print("Napiš sportovní aktivity,které jsi dnes dělal a jak dlouho (v minutách).") 


#úkol B: Lukáš Voráček

aktivitaA= input ("První aktivita ") 

cas1 = int (input ("Čas první aktivity ")) 

kcal1 =cas1*5 

 

aktivitaB = input ("Druhá aktivita ") 

cas2 =int (input ("Čas druhé aktivity ")) 

kcal2=cas2*5 

 

vsechnykcal= kcal1+kcal2 


# společné: Adam Říha, Lukáš Voráček

prebytek = celkove_kalorie - vsechnykcal

print (f"Snědl/a jste {celkove_kalorie} kcal a spálil/a jste {vsechnykcal} kcal. Celkem: {prebytek} kcal.")