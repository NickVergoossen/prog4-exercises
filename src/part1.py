# Your exercises should appear in this file.


def add(x, y):
    return x + y


def kwadraat(x):
    v = x ** 2
    return v


def oppervlakte_kubus(z):
    """Return de oppervlakte van een kubus met zijde z"""
    return z * z * 6


def seconds_in_days(days=1):
    """Geef het aantal seconden in het opgegeven aantal dagen

    Als er geen parameter doorgegeven wordt, geef dan het aantal
    seconden in 1 dag terug.
    """
    return 3600 * 24 * days


def seconds_in_weeks(weeks):
    """Return het aantal seconden in 'week' weken."""
    return 3600 * 24 * weeks * 7


def seconds_in_years(years):
    """Return het aantal seconden in 'years' jaren.

    Veronderstel dat ieder jaar uit exact 52 weken bestaat.
    """
    return 3600 * 24 * 7 * 52 * years


def seconds_remaining_in_life(age, is_female=False):
    """Return het aantal seconden dat overblijft in je leven.

    Ga uit van een maximale levensduur van 80 jaren voor mannen,
    en 84 jaren voor vrouwen.
    """
    if is_female == True:
        remaining = 3600 * 24 * 7 * 52 * (84 - age)
    else:
        remaining = 3600 * 24 * 7 * 52 * (80 - age)
    return remaining


def postcodes():
    """Return een dictionary met postcodes"""
    v = {
        "3650": "Dilsen-Stokkem",
        "3000": "Leuven",
    }
    return v


def oneven_getallen(x):
    """Return een lijst met de eerste 'x' oneven getallen."""
    lijst = []
    for i in range(1, 100, 2):

        if len(lijst) == x:
            return lijst
        else:
            lijst.append(i)
            len(lijst)
    return x