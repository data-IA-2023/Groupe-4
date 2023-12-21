import pandas as pd
import numpy as np

csvfile_population = "FAOSTAT_2013_population.csv"
csvfile_cereal = "FAOSTAT_2013_cereal.csv"
df_population = pd.read_csv(csvfile_population)
df_cereal=pd.read_csv(csvfile_cereal)

def calculer_population(df):
    #Normalement, la population est simple de calculer
    #Additioner les valeur de tous les pays et voila
    population = 0
    for i in range(len(df["Country"])):
        population += df["Value"][i]*1000 #car la population est fois mil
    print(f"La population faux est: {population}")
    #Le problème viens de voir que la population est beaucoup plus grand, et on a une anomalie
    #dans la colonne flag

    #--> Pour trouver les annomalies
    for i in range(len(df["Flag"])):
        if df["Flag"][i]: #si la flag n'est pas vide
            anomalie = df["Country"][i]
    #on reconte la population
    population_vraie = 0
    for i in range(len(df["Country"])):
        population_vraie += df["Value"][i]*1000
        if df["Country"][i] == anomalie:
            population_vraie -= df["Value"][i]*1000 #on substrai le doublon de l'anomalie

    print(f"La population vraie sans l'anomalie est {population_vraie}")

#EXERCISE 2
#lecture du CSV
csvfile = "FAOSTAT_2013_cereal.csv"
dfc = pd.read_csv(csvfile)
dfc = dfc.loc[dfc['Pays'].str.contains('France',)].loc[dfc['Produit'].str.contains('Blé')].loc[dfc['Symbole'].str.contains('S')]




        
