from dati import dati

for vardnic in dati:
    print("Gramata", "<<",vardnic["name"], ">>", "<<(",vardnic["year_published"],")>>",",", "<<",vardnic["pages"], ">>", "lpp")

# Mainīgais ar lielālo vai vienu vērtību
# Cikls kas izxiet caur visām
#     salīdzinājums, vai jaunā ir mazāka

#var = [{}, {}, {}]
#maz = var[0]
#for x in var:
#    if maz > x:
#        maz = x
 
vecaka_gramata = dati[0]
kopejais_lapusu_skaits = 0
kopeja_cena = 0

for gramata in dati:
    if int(gramata["year_published"]) < int(vecaka_gramata["year_published"]):
        vecaka_gramata = gramata
print(vecaka_gramata["name"])

garakais_nosaukums = ""
for gramata in dati:
    kopejais_lapusu_skaits += int(gramata["pages"])
    kopeja_cena += int(gramata["price"])
    garakais_nosaukums = max([garakais_nosaukums, gramata["name"]], key=len)

videjais_aritmetiskais =  kopeja_cena / len(dati)
print(kopejais_lapusu_skaits)
print(videjais_aritmetiskais)
print(garakais_nosaukums)