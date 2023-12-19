import pandas as pd
import numpy as np

path = "/home/laamh/Documents/TravailPythonGit/Groupe-4/fao_2013/FAOSTAT_2013_population.csv"
df = pd.read_csv(path)

for x in range(len(df["Flag"])):
    if df["Flag"][x]:
        df.drop(x,inplace=True)

#print(df.iloc[-1])

somme = df['Value'].sum()*1000
print(f"La somme des valeurs est : {somme}")
 





#recherche = df.loc[df['Flag'].str.contains('A')]

#print(df.dtypes)


#print(df.loc[[174]])

#df_clear = df.drop(index=df.iloc[-1].name)
#df_total = df['Value'].sum()


#print(df_clear)
#print(f"Les humains étaient {df_total} sur terre en 2013")

#print(df_clear)
#print(df['Value'])
