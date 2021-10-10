
#initialise A et B et effectuer des calculs
A = 15
B = 4
C = A + B
D = A * B
E = A ** B
F = A / B
G  = A // B
H = A % B

#Affichage

print(f"Le resultat de {A} plus {B} est {C}")
print(f"Le resultat de {A} multiplie par {B} est {D}")
print(f"Le resultat de {A} a la puissance {B} est {E}")
print(f"Le resultat de {A} / {B} est {F}")
print(f"La partie entiere de {A} divise par {B} est {G}")
print(f"La partie decimale de {A} divise par {B} est {H}")

#Creer un dictionnaire

dictionnaire = {
    "15+4":"19"
}

#intialise de A a H
dictionnaire['A'] = 15
dictionnaire['B'] = 4
dictionnaire['C'] = A + B
dictionnaire['D'] = A * B
dictionnaire['E'] = A ** B
dictionnaire['F'] = A / B
dictionnaire['G'] = A // B
dictionnaire['H'] = A % B

# Afficher
print(dictionnaire)

#Modifier A

dictionnaire['C'] = A

#pour acceder a C
print(dictionnaire['C'])

#Supprimer C et afficher voir

del(dictionnaire['C'])

print(dictionnaire)

#Afficher la liste des cles

for cle in dictionnaire.keys():
    print(cle)

#Afficher la liste des valeurs

for valeur in dictionnaire.values():
    print(valeur)

#Afficher la liste cle valeur

for cle,valeur in dictionnaire.items():
    print(cle,valeur)

#creer un tuple qui va contenir les valeurs de A, B et C

tuple = (15, 4, 15+4)

print(tuple)

#Ajouter la valeur de D

tuple = tuple + (15*4,)

print(tuple)

#Modifions la valeur de A par 16

lst = list(tuple)
lst[0] = 16

print(lst)

#Supprimer la valeur de A dans le tuple

del(lst[0])

print(lst)

#Creer une liste, liste 1 qui va contenir les lettres A, B, C et D.
liste1 = ["A", "B", "C"]
print(liste1)

#Creer une 2ieme liste, list 2 qui va contenir les valeurs A, B, C et D
liste2 = [15,4,15+4]
print(liste2)

#Creer une 3ieme liste qui va contenir les listes 1 et 2.

liste3 = liste1 + liste2
print(liste3)

#Vous ajouter a la liste 1, E et F: Vous supprimer B de la liste.

liste1.append("E")
liste1.append("F")
liste1.remove("B")

#Vous remplacez A par G
liste1[0]= "G"
print(liste1)


