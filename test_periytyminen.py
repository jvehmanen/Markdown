# PYTEST-TESTAUSFUNKTIOT
# =====================

# MODUULIEN JA KIRJASTOJEN LATAUKSET
# ----------------------------------

# Käyttöjärjestelmän virheilmoitusten testaus vaatii pytest:n lataamista
import pytest # Jos et testaa virheilmoituksia, voi jättää pois

# Ladataan testattava moduuli
import periytyminen

# Luodaan testiolioita eri luokista testausta varten

person = periytyminen.Person('Assi' , 'Kalma')

student = periytyminen.RasekoStudent('Jonne', 'Janttari', '53467')

# TESTAUSFUNKTIOT ELI YKSIKKÖTESTIT
# ---------------------------------

def test_person():
    assert person.givenName == 'Assi'
    assert person.surName == 'Kalma'

def test_person_age3():
    assert round(person.calculateAge3('2008-12-31')) == 16