# FUNKTIOT
# ========

# Funktio, joka ei palauta arvoa eikä käytä argumentteja

def tervehdys():
    """prints Hyvää huomenta! on the screen
    """
    print('Hyvää huomenta!')

tervehdys()

def toivotus(nimi, aika):
    """Greets user differently according to the day

    Args:
        nimi (str): user's name
        aika (int): hour in military format
    """
    if aika > 16:
        viesti = f'Hyvää iltaa{nimi}!'
    elif aika > 10:
        viesti = f'Hyvää päivää{nimi}!'
    else:
        viesti = f'Hyvää huomenta{nimi}!'

    print(viesti)
toivotus('Jonna', 9)

alkulitania = 'millon minä olisin työni tehnyt' 

def tyoMotivaatio(paiva: str) -> str:
    """Returns the motto of the day in Finnish

    Args:
        paiva (str): Weekday in Finnish

    Returns:
        str: The motto of the day
    """
    mottoDictionary = {'maanantai': 'na en malttanut',
             'tiistai': 'na en tietänyt',
             'keskiviikko': 'na en kerennyt',
             'torstai': 'na en tohtinut',
             'perjantai': 'on paha päivä',
             'lauantai': 'on pyhän aatto',
             'sunnuntai': 'on suurijuhla'}
    
    dailyMotto = f'{alkulitania} {paiva}{mottoDictionary[paiva]}'
    return dailyMotto

print(tyoMotivaatio('torstai'))

