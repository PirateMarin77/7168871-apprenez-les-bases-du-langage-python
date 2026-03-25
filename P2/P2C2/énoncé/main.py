# Ecrivez votre code ici !
nombres = (" 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ")
liste = nombres.split()
for element in liste :
  liste_entier = int (liste)
  print(liste_entier)
somme = sum(liste_entier)
print(somme)
somme = 0
for x in liste_entier :
  somme += x
  print(somme)
Moyenne = sum(liste_entier) // len(liste_entier)
nb_sup = sum(1 for x in liste_entier if x > Moyenne )
print('Moyenne : ', Moyenne)
print('Eléments supérieurs :', nb_sup)
