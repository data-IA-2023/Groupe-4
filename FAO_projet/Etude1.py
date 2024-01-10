import pandas as pd
import numpy as np
import matplotlib as plt

"""
QUESTION 1: Nombre d'humains sur la planète

Calculez le nombre total d'humains sur la planète. Critiquez votre résultat. 
En cas d'anomalie, analysez et effectuer les corrections nécessaires. 
Donnez le résultat de votre calcul pour l'année 2013.

"""
# Lecture du CSV
csvfile = "FAOSTAT_2013_population.csv"
df_population = pd.read_csv(csvfile)

dimension = df_population.columns
nb_lignes, nb_colonnes = df_population.shape
print("\nLes données sont classées par :\n", dimension)
print ("\nNombre de lignes :", nb_lignes)
print ("Nombre de colonnes :", nb_colonnes)
print(df_population.dtypes)

#population de chaque pays
df_population['Value']

#calcul de la population mondiale

popSum = df_population['Value']
popSum.sum()*1000

#on recherche les répétitions du string 'China'
country = df_population['Country']
for i in range(len(country)):
    if 'China' in country[i]:
        print(country[i])

#recherche de l'anomalie
df_population.iloc[-1,[11,12,13]]

#iteration pour récupérer les 4 provinces et sommes de la population de ces dernières.
result = 0
for i in range(len(country)):
    if 'China' in country[i] and country[i] != 'China':
       result = result + popSum[i]
print(result)

#comparaison entre le résultat et l'anomalie
if result == popSum.iloc[-1]:
    print("il y a bien un doublon")

#paolo
for i in range(len(df_population["Flag"])):
    if not pd.isna(df_population["Flag"][i]):
        df_population.drop(i,inplace=True)

df_population.iloc[-1]

#Calcul de la population mondiale
NewSumPopMondiale = df_population['Value'].sum()*1000
print(f"La somme de la population mondiale en 2013 est de : {NewSumPopMondiale}")

"""
QUESTION 2: Redondances

Identifiez ces redondances, en donnant votre réponse sous forme de formule mathématique (pas besoin de coder ici).
C'est une équation à 3 termes de type (a_1 + a2 + [...] = b_1 + b_2 + [...] = c_1 + c_2 + [...]) ) faisant intervenir chacune des 11 quantités données ci dessus.
Illustrez cette équation avec l'exemple du blé en France.

"""
#lecture du CSV
csvfile2 = "FAOSTAT_2013_cereal.csv"
dfc = pd.read_csv(csvfile2)
dfcf = dfc.loc[dfc['Produit'].str.contains('Blé')].loc[dfc['Symbole'].str.contains('S')]
dfcf

valeurs = dfc['Valeur']

valeurs.dtypes
(valeurs)
type(valeurs)
valeurs

#production = exportation + disponibilité intérieur - importation - variation de stock = exportation + (Nourriture + autre + traitement + pertes + semences + Aliment pour animaux) - importation - variation de stock


#redondance = production et disponibilité intérieur
#38614+2055+1131=748+21502+20298=7822+358+1575+2824+6971

for pays in dfc['Pays'].unique():
    country                   = dfc.loc[dfc['Pays']==pays]
    ble                       = country.loc[country['Produit'].str.contains('Blé')]
    production                = ble.loc[dfc['Élément'].str.contains('Production')].Valeur
    importation               = ble.loc[dfc['Élément'].str.contains('Importations - Quantité')].Valeur
    exportation               = ble.loc[dfc['Élément'].str.contains('Exportations - Quantité')].Valeur
    varStock                  = ble.loc[dfc['Élément'].str.contains('Variation de stock')].Valeur
    dispoInterieur            = ble.loc[dfc['Élément'].str.contains('Disponibilité intérieure')].Valeur
    alimAnimaux               = ble.loc[dfc['Élément'].str.contains('Aliments pour animaux')].Valeur
    semences                  = ble.loc[dfc['Élément'].str.contains('Semences')].Valeur
    pertes                    = ble.loc[dfc['Élément'].str.contains('Pertes')].Valeur
    traitement                = ble.loc[dfc['Élément'].str.contains('Traitement')].Valeur
    autreUser                 = ble.loc[dfc['Élément'].str.contains('Autres Utilisations')].Valeur
    nourriture                = ble.loc[dfc['Élément'].str.contains('Nourriture')].Valeur
    


    #production    = production[0] if production.shape else 0
    try: 
        production = production.values[0]
    except IndexError:
        production = 0
    try:
        importation = importation.values[0]
    except IndexError:
        importation = 0
    try: 
        exportation = exportation.values[0]
    except IndexError:
        exportation = 0
    try:
        varStock = varStock.values[0]
    except IndexError:
        varStock = 0
    try: 
        dispoInterieur = dispoInterieur.values[0]
    except IndexError:
        dispoInterieur = 0
    try:
        alimAnimaux = alimAnimaux.values[0]
    except IndexError:
        alimAnimaux = 0
    
    try:
        semences = semences.values[0]
    except IndexError:
        semences = 0
    try:
        pertes = pertes.values[0]
    except IndexError:
        pertes = 0
    try:
        traitement = traitement.values[0]
    except IndexError:
        traitement = 0
    try: 
        autreUser = autreUser.values[0]
    except IndexError:
        autreUser = 0
    try:
        nourriture = nourriture.values[0]
    except IndexError:
        nourriture = 0
    
    if production != 0 :
      print(pays,'Production :',production)
    if importation != 0:
      print(pays,'importation :',importation)
    if exportation != 0:
      print(pays,'exportation :',exportation)
    if varStock != 0:
      print(pays,'variation du stock :',varStock)
    if dispoInterieur != 0:
      print(pays,'disponibilité interieur :',dispoInterieur)
    if alimAnimaux != 0:
      print(pays,'alimentation animale :',alimAnimaux)
    if semences != 0:
      print(pays,'semences :',semences)
    if pertes != 0:
      print(pays,'pertes :',pertes)
    if traitement != 0:
      print(pays,'traitement :',traitement)
    if autreUser != 0:
      print(pays,'autre utilisation :',autreUser)
    if nourriture != 0:
      print(pays,'nourriture :',nourriture)

    print("---------------------")
    print(int(production))
    print(int(exportation + dispoInterieur - importation - varStock))
    print(int(exportation + (nourriture + autreUser + traitement + pertes + semences + alimAnimaux) - importation - varStock))
     

#production = exportation + disponibilité intérieur - importation - variation de stock = exportation + (Nourriture + autre + traitement + pertes + semences + Aliment pour animaux) - importation - variation de stock

dflist = dfc['Valeur'].tolist()
type(dflist)

def locelement(a, b):
    test123 = dfc.loc[dfc[a].str.contains(b)].Valeur
    test123_zero = test123[test123 != 0]
    return test123_zero

print(locelement('Élément', 'Exportations - Quantité'))




#for pays in dfc['Pays'].unique():
#    cdt = dfc.loc[(dfc['Pays'] == pays) & (dfc['Produit'].str.contains('Blé'))]
#
#    production = cdt.loc[cdt['Élément'].str.contains('Production'), 'Valeur'].values
#   importation = cdt.loc[cdt['Élément'].str.contains('Importations - Quantité'), 'Valeur'].values
#    exportation = cdt.loc[cdt['Élément'].str.contains('Exportations - Quantité'), 'Valeur'].values
#
#    production = production[0] if production.size else 0
#    importation = importation[0] if importation.size else 0
#    
#    if production != 0:
#        print(pays, production, importation)

"""
QUESTION 3: Disponibilité alimentaire (calories, protéines)

Calculez (pour chaque pays et chaque produit) la disponibilité alimentaire en kcal puis en kg de protéines.
Vous ferez cela à partir de ces informations : 
- Population de chaque pays
- Disponibilité alimentaire donnée pour chaque produit et pour chaque pays en kcal/personne/jour, 
- Disponibilité alimentaire en protéines donnée pour chaque produit et pour chaque pays en g/personne/jour.
Pour cette étape vous avez besoin de constituer une seule et même table à partir des tables animaux et végétaux. 

"""
# Lecture du CSV
dfvegetal = pd.read_csv("FAOSTAT_2013_vegetal.csv")
dfvegetal.insert(14,'dfCode','Vegetal')
dfanimal  = pd.read_csv("FAOSTAT_2013_animal.csv")
dfanimal.insert(14,'dfCode','Animal')

# Input demande pays voulu

pays_voulu = 2 #int(input("Entrez un code pays : "))

# Les CSV étant en deux langues différentes on utilise une variable pour
# localiser les pays en fonction de leur code pays qui restent eux inchangés

traductionpays = str(dfanimal.loc[dfanimal['Code Pays'] == pays_voulu, 'Pays'].unique()).replace('[',' ').replace(']',' ').replace("'","")
 
# Codes voulus pour l'exercices

code_element_kcal = 664
code_element_proteine = 674
code_element_kg = 645

# Concat des CSV, le CSV cereal et vegetal contenant des lignes ou le code élément 664 et 674
# sont présents vont créer une nouvelle df 

dffinal = pd.concat([dfvegetal[dfvegetal["Code Élément"].isin([664,674, 645])],dfanimal[dfanimal["Code Élément"].isin([664,674,645])]], join = "inner")

# Résulat demandé avec le concat en fonction du code pays demandé

resultatdfdf = dffinal[dffinal['Code Pays'] == pays_voulu]

# Réponses
# Donc ici si un code pays correspond à un pays dans les CSV on affiche sa data frame triée
# en ordre alphabétique et par code produit croissant, dans le cas ou le code pays est éronné
# on affiche la nouvelle DataFrame au complet triée de la même façon

if pays_voulu in df_population['Country Code'].values:
    donnees_pays = df_population[df_population['Country Code'] == pays_voulu]['Value'].values[0]*1000
    print(f"Le nombre d'habitants en {traductionpays} est : {donnees_pays}")
    print(resultatdfdf.sort_values(by=['Code Élément','Pays']))
else:
    print(f"Le pays {pays_voulu} n'a pas été trouvé dans les données.")
    print(dffinal.sort_values(by=['Code Élément','Pays']))

"""
QUESTION 4 : Ratio énergie/poids

A partir de ces dernières informations, et à partir du poids de la disponibilité alimentaire (pour chaque pays et chaque produit), calculez pour chaque produit le ratio "énergie/poids", que vous donnerez en kcal/kg. 
Vous pouvez vérifier la cohérence de votre calcul en comparant ce ratio aux données disponibles sur internet, par exemple en cherchant la valeur calorique d'un oeuf.

"""
# Sélectionne les colonnes nécessaires

df_new = dffinal[['Pays', 'Produit', 'Code Élément', 'Code Produit', 'Valeur','dfCode']]

# Filtre les lignes où le Code Élément est égal à 664 et 674

df_664 = df_new[df_new['Code Élément'] == 664]
df_645 = df_new[df_new['Code Élément'] == 645]

# Filtre les lignes dont la valeur est zéro pour éviter une potentielle division par zéro
df_645 = df_645[df_645['Valeur'] != 0]
df_645['Valeur'] = df_645['Valeur']/365
# Fusionne les DataFrames df_664 et df_674 sur les colonnes 'Pays' et 'Produit'
df_merged = pd.merge(df_664, df_645, on=['Pays', 'Produit', 'Code Produit','dfCode'])
#Calcule le rapport entre les valeurs de la colonne 'Valeur_x' et 'Valeur_y'

df_merged['Kcal/Kg'] = df_merged['Valeur_x'] / df_merged['Valeur_y']

dfquestion4 = df_merged[['Pays', 'Produit', 'Code Produit', 'Kcal/Kg','dfCode']]
dfquestion4

"""
QUESTION 5 : Aliments les plus caloriques et protéiques

En considérant les aliments végétaux et animaux, citez 5 aliments parmi les 20 aliments les plus caloriques, en utilisant le ratio énergie/poids.
Citez 5 aliments parmi les 20 aliments les plus riches en protéines.

"""
#citez cinq aliments les plus caloriques
df_merged.dropna().sort_values(by=['Valeur_y'], ascending=False).head(5)
#citez cinq aliments les plus riches en protéines
df_merged.dropna().sort_values(by=['Valeur_x'], ascending=False).head(5)
# g/personne/jour
"""
QUESTION 6 : Dispo. intérieure mondiale des végétaux

Calculez, pour les produits végétaux uniquement, la disponibilité intérieure mondiale exprimée en kcal.

"""
dfvege = dfvegetal
dfvege

country = dfvege['Pays']
for i in range(len(country)):
    if dfvege["Code Pays"][i] == 351:
         dfvege.drop(i,inplace=True)

df_newveg = dfvege
df_newveg = df_newveg.drop(['Code Produit','Code Pays','Code Élément','Code Année'], axis = 1)


df_newveg['codeIndex'] = dfvege['Code Pays'].astype(str)+'_'+dfvege['Code Produit'].astype(str)+'_'+dfvege['Code Élément'].astype(str)
df_newveg

regex = '5301$'

dfdispoInterVeg = df_newveg.loc[df_newveg["codeIndex"].str.contains(regex)]


dfdispoInterVeg

SumVegDispoInter = dfdispoInterVeg["Valeur"].sum()*1000000


print(f'{SumVegDispoInter:.2e} Kg : Somme de la disponibilité intérieur mondiale')

dfdispoInterVegNewIndex = dfdispoInterVeg.reset_index(drop=True)
dfdispoInterVegNewIndex.drop(['dfCode'], axis=1)

dfdispoInterVegNewIndex

"""
QUESTION 7 : Potentiel alimentaire des végétaux
Combien d'humains pourraient être nourris si toute la disponibilité intérieure mondiale de produits végétaux était utilisée pour de la nourriture ? 
Donnez les résultats en termes de calories, puis de protéines, et exprimez ensuite ces 2 résultats en pourcentage de la population mondiale.

"""

""" En commentarie car ca functionne pas encore

dfrapport = dfquestion4.drop(dfquestion4.loc[dfquestion4['dfCode'] == " Animal"],axis = 1)

dfrapport

df_mergednew = dfquestion4.merge(dfdispoInterVegNewIndex, how='inner', on='Produit')

dfvege_dispoAlimKcal = dfvege.loc[dfvege['Élément'] == "Disponibilité alimentaire (Kcal/personne/jour)"]
dfvege_dispoAlimKcalSum = dfvege_dispoAlimKcal["Valeur"].sum()
NbHPNKcal = dispoInterVegSum / dfvege_dispoAlimKcalSum
dfvege_dispoAlimG = dfvege.loc[dfvege['Élément'] == "Disponibilité de protéines en quantité (g/personne/jour)"]
dfvege_dispoAlimGSum = dfvege_dispoAlimG["Valeur"].sum()
NbHPNKG = dispoInterVegSum / dfvege_dispoAlimGSum
print(NbHPNKcal)
print(NbHPNKG)
PercentMondeKcal = (NbHPNKcal/somme)*100
PercentMondeG    = (NbHPNKG/somme)*100
print(PercentMondeKcal)
print(PercentMondeG)

"""
"""
QUESTION 8: Potentiel alimentaire des végétaux (destinés aux animaux pertes)

Combien d'humains pourraient être nourris si toute la disponibilité alimentaire en produits végétaux la nourriture végétale destinée aux animaux et les pertes de produits végétaux étaient utilisés pour de la nourriture ? 
Donnez les résultats en termes de calories, puis de protéines, et exprimez ensuite ces 2 résultats en pourcentage de la population mondiale.

"""
dfpivot = pd.pivot_table(dfvege,index=['Code Pays'], columns=(contatenate) ['Code '])

dfq8 = dfvegetal[dfvegetal["Code Élément"].isin([645,5521,5123])]

totalq8 = dfq8['Valeur'].sum()
Resultq8Kcal =  totalq8/dfvege_dispoAlimKcalSum
Resultq8G    =  totalq8/dfvege_dispoAlimGSum
print(Resultq8Kcal)
print(Resultq8G)
PercentMondeQ8Kcal = (Resultq8Kcal/somme)*100
PercentMondeQ8G    = (Resultq8G/somme)*100
print(PercentMondeQ8Kcal)
print(PercentMondeQ8G)

"""
QUESTION 9: Potentiel alimentaire de la dispo mondiale

Combien d'humains pourraient être nourris avec la disponibilité alimentaire mondiale ? 
Donnez les résultats en termes de calories, puis de protéines, et exprimez ensuite ces 2 résultats en pourcentage de la population mondiale.

"""

dfvege_dispoAlimTotal = dfvege.loc[dfvege['Élément'] == "Disponibilité alimentaire en quantité (kg/personne/an)"]
dfvege_dispoAlimTotalSum = dfvege_dispoAlimTotal["Valeur"].sum()
NbHPNTotalKcal = dfvege_dispoAlimTotalSum / dfvege_dispoAlimKcalSum
NbHPNTotalG = dfvege_dispoAlimTotalSum / dfvege_dispoAlimGSum
print(NbHPNTotalKcal)
print(NbHPNTotalG)
PercentMondeQ9Kcal = (NbHPNTotalKcal/somme)*100
PercentMondeQ9G    = (NbHPNTotalG/somme)*100
print(PercentMondeQ9Kcal)
print(PercentMondeQ9G)

"""
QUESTION 10: Proportion de la sous-nutrition mondiale

A partir des données téléchargées qui concernent la sous-nutrition, répondez à cette question : 
Quelle proportion de la population mondiale est considérée comme étant en sous-nutrition ?

"""

df_pop = pd.read_csv("FAOSTAT_2013_population.csv")
df_sous_alim = pd.read_csv("FAOSTAT_2013_sous_alimentation.csv")
prop_sous_alim = df_sous_alim["Valeur"].sum()*1000000 / NewSumPopMondiale
print("La proportion des personnes sous alimentées est de:", prop_sous_alim)
df_sous_alim

"""
QUESTION 11: Céréales

Établissez la liste des produits (ainsi que leur code) considéré comme des céréales selon la FAO. 
En ne prenant en compte que les céréales destinées à l'alimentation (humaine et animale), quelle proportion (en termes de poids) est destinée à l'alimentation animale ?

"""

df_cereales = pd.read_csv("FAOSTAT_2013_cereal.csv")
df_cereales_animaux = df_cereales[df_cereales["Code Élément"].isin([5521])] 
df_cereales_total = df_cereales[df_cereales["Code Élément"].isin([5301])] 
proportion_animaux = df_cereales_animaux["Valeur"].sum() /df_cereales_total["Valeur"].sum()
df = df_cereales.groupby("Produit").mean()
print(df["Code Produit"])
print("La proportion des aliments pour les animaux est de:",proportion_animaux)

"""
QUESTION 12: Sous-nutrition

Sélectionnez parmi les données des bilans alimentaires les informations relatives aux pays dans lesquels la FAO recense des personnes en sous-nutrition.
Repérez les 15 produits les plus exportés par ce groupe de pays.Parmi les données des bilans alimentaires au niveau mondial, sélectionnez les 200 plus grandes importations de ces produits 
(1 importation = une quantité d'un produit donné importée par un pays donné).

Groupez ces importations par produit, afin d'avoir une table contenant 1 ligne pour chacun des 15 produits. 
Ensuite, calculez pour chaque produit les 2 quantités suivantes :
-le ratio entre la quantité destinés aux "Autres utilisations" (Other uses) et la disponibilité intérieure.
-le ratio entre la quantité destinée à la nourriture animale et la quantité destinée à la nourriture (animale + humaine)

Donnez les 3 produits qui ont la plus grande valeur pour chacun des 2 ratios (vous aurez donc 6 produits à citer)

"""
a = df_population["Country Code"].unique()
b = df_sous_alim["Code zone"].unique()
df_sous_alim = df_sous_alim[df_sous_alim["Code zone"].isin(a)] #nettoyage de base
df_sous_alim = df_sous_alim[df_sous_alim["Symbole"] == "F"] #on prend que les pays on il y a de malnutrition
pays_malnutri = df_sous_alim["Zone"].unique()
dftotal = df_animal.merge(df_vegetal)

"""
QUESTION 13: USA

Combien de tonnes de céréales pourraient être libérées si les USA diminuaient leur production de produits animaux de 10% ?

"""

df = df_cereales_animaux[df_cereales_animaux["Code Pays"] == 231] #USA CODE 2311
dix_pour = (df["Valeur"].sum()*1000) * 0.1 #milliers des tonnes á tonnes et 10pour
print(f"Les tonnes des produits animaux seraient {dix_pour} si on libére 10% ")

"""
QUESTION 14: Thaïlande

En Thaïlande, quelle proportion de manioc est exportée ?
Quelle est la proportion de personnes en sous-nutrition?

"""

df = df_cereales_animaux[df_cereales ["Code Pays"] == 216] # Thaïlande code 216
proportionthailande = (df["Valeur"])