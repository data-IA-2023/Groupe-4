import pandas as pd 
df_animal = pd.read_csv("FAOSTAT_2013_animal.csv")
df_vegetal = pd.read_csv("FAOSTAT_2013_vegetal.csv")
df_animaletvegetal = pd.concat([df_animal[df_animal["Code Élément"].isin([664,674])],df_vegetal[df_vegetal["Code Élément"].isin([664,674])]], join = "inner")
for produit in set(df_animaletvegetal["Produit"]):
    for pays in set(df_animaletvegetal["Pays"]):
        df = df_animaletvegetal[df_animaletvegetal["Produit"] == str(produit)]
        df = df[df["Pays"] == str(pays)]
        resultat = (df[df["Code Élément"] == 664]) / (df[df["Code Élément"] == 674]) / 1000

print(df)
