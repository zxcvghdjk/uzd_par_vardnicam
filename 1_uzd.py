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

vecums = dati["year_published"]
maz = var[0]

for x in vecums:
    if maz> x:
        maz = x