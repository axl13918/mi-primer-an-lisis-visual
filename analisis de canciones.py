import pandas as pd
import matplotlib.pyplot as plt

datos = [
{"Cancion":"Past Won't Last","Artista":"Joji","Reproducciones":420},
{"Cancion":"If It Only Mattered","Artista":"Joji","Reproducciones":390},
{"Cancion":"NITROUS","Artista":"Joji","Reproducciones":300},
{"Cancion":"Hush","Artista":"The Marías","Reproducciones":290},
{"Cancion":"Baby","Artista":"The Marías","Reproducciones":310},
{"Cancion":"All I Really Want Is You","Artista":"The Marías","Reproducciones":260},
{"Cancion":"Cariño","Artista":"The Marías","Reproducciones":340}
]

tabla = pd.DataFrame(datos)

tabla.to_csv("cancionesfinal.csv",index=False)

plt.bar(tabla.Cancion, tabla.Reproducciones)
plt.xticks(rotation=45)
plt.xlabel("canciones")
plt.ylabel("reproducciones")
plt.title("reproducciones joji y the marias")
plt.tight_layout()
plt.show()

maximo = 0
c = ""
a = ""
for i in range(len(tabla)):
    if tabla.Reproducciones[i] > maximo:
        maximo = tabla.Reproducciones[i]
        c = tabla.Cancion[i]
        a = tabla.Artista[i]

print("la que tiene mas es:",c,"de",a)
