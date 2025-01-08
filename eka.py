# Se ihan ensimmäinen hei maailma esimerkki

print('Hello World')

print('Ja tämän sovelluksen koodasi Jakke Jäynä')

# ESIMERKKEJÄ MUUTTUIJEN KÄYTÖSTÄ
# ===============================

# YKSINKERTAISET MUUTTUJAT
# ------------------------

# Merkkijono string
etunimi = 'Jonne' # merkkijono string (str)
ika = 16 # kokonaisluku integer (int)
ytoaineiden_keskiarvo = 2.5 # liukuluku floating point number (float)
valmistunut = False # Totuusarvo boolean (bool)
print(etunimi, 'sai keskiarvoksi YTO-aineista', ytoaineiden_keskiarvo)
print(etunimi, 'on valmistunut', valmistunut)

# RAKENTEELLISET MUUTTUJAT
# ------------------------

nimilista = ['Jonne', 'Jasmiina', 'Aleksanteri'] # lista list
print('Listassa ensimmäisenä on', nimilista[0]) # indeksissä 0 oleva arvo
jasenia = len(nimilista) # listan jäsenten määrä selviää len- komennolla
print('nimilistassa on', jasenia, 'henkilöä')
nimilista.sort() # listan sort metodi aakkostaa sen  
print('Aakkostettu lista on', nimilista)

ryhmat = ('TiVi24A', 'TiVi24B', 'TiVi20oa') # Monikko tuple
print('Meidän ryhmä on', ryhmat[2])
# ryhmat[2] = 'Tivi20ka' # Yksittäistä jäsentä ei voi muuttaa
ryhmät = ('TiVi24A', 'TiVi24B', 'Tivi20ka') #koko monikon voi muuttaa
print('meidän uusi ryhmä on', ryhmat[2])

joukko = {'Tuittu', 'Assi', 'Calle'} # joukko set
print('ja joukkoon kuuluvat', joukko) #huomaa järjestys
# print(joukko[2]) ei toimi, koska jäseneen ei voi viitata indeksillä

#sanakirja dictionary (dict)
henkilotiedot = {'etunimi': 'Jonne', 'sukunimi': 'Janttari', 'ika': '16'}

print('Opiskelijan', henkilotiedot['etunimi'], 'ikä on', henkilotiedot['ika'])

opiskelija1 = {'etunimi': 'Jonne', 'sukunimi': 'Janttari', 'ika': '16'}
opiskelija2 = {'etunimi': 'Iina', 'sukunimi': 'Urpo', 'ika': '17'}
opiskelija3 = {'etunimi': 'Tuittu', 'sukunimi': 'Kiukkunen', 'ika': '16'}

# Lista sanakirjoista -> Taulukko
opiskelijalista = [opiskelija1, opiskelija2, opiskelija3]
print('Opiskelijalista on',opiskelijalista)

uusi_opiskelija = {'etunimi': 'Assi', 'sukunimi': 'Kalma', 'ika': '18'}

# Lisätään uusi arvo olemassa olevaan listaan
opiskelijalista.append(uusi_opiskelija)

# Tulostetaan opiskelijalistan ensimmäinen jäsen
print('Listassa ensimmäinen on', opiskelijalista.pop(0))
print('Ja viimeisenä on', opiskelijalista.pop())
