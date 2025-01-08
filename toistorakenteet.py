# Toistorakenteet
# ===============

# While-silmukat
# --------------

# Ikuinen silmukka
while True:
    print('Pyörin ikuisesti')
    poistu = input('haluatko jatkaa? k/e ')
    if poistu == 'e':
        break # Poistutaan silmukasta

# Kierrosmääräinen silmukka
laskuri = 0
while laskuri < 10:
    print('Nyt on menossa kierros', laskuri)
    laskuri += 1 # Tai laskuri = laskuri + 1

# For-silmukat
# ------------

# Rakenteellisen muuttujan arvojen läpikäynti 
lista = ['Jonne', 'Tuittu', 'Jakke', 'Calle']
for jasen in lista:
    print(jasen, 'kuuluu listaan')

# Kierrosmääräinen simukka

teksti = 'X'
for laskuri in range(15):
    teksti +'X'
    print(teksti)

# Range- komento mahdollistaa alun, lopun ja askeleet

for parilliset_kymmenet in range(10,100,20):
    print(parilliset_kymmenet)