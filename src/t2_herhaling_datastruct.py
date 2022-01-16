def maak_videokaart_dict(merk, naam, architectuur, geheugen, busbreedte, diesize, jaar):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.

    Bijvoorbeeld:
    >>> maak_videokaart_dict("NVIDIA", "RTX 3080", "Ampere", 10, 320, 628, 2020)
    {'merk': 'NVIDIA', 'naam': "RTX 3080", 'architectuur': "Ampere", 'geheugen': 10, 'busbreedte': 320, 'diesize': 628, "jaar": 2020}
    """
    gegevens = {
        "merk": merk,
        "naam": naam,
        "architectuur": architectuur,
        "geheugen": geheugen,
        "busbreedte": busbreedte,
        "diesize": diesize,
        "jaar": jaar,
    }
    return gegevens


def tel_videokaarten(lijst_videokaarten):
    """Geef het totaal aantal videokaarten in de lijst van videokaarten terug."""
    aantal = len(lijst_videokaarten)
    return aantal




def tel_videokaarten_per_merk(lijst_videokaarten):
    """Geef het aantal videokaarten per merk in de lijst van videokaarten terug.

    Het resultaat is dus een dictionary met 2 keys:
    {
        "AMD": x,
        "NVIDIA": y,
    }
    Met x het aantal AMD videokaarten in de lijst en y het aantal NVIDIA
    videokaarten in de lijst.
    """
    kaarten = {
        "AMD": 0,
        "NVIDIA": 0,

    }
    for kaart in lijst_videokaarten:
        merk = kaart["merk"]
        kaarten[merk] = kaarten.get(merk, 0) + 1
    return kaarten


def grootste_videokaart(lijst_videokaarten):
    """Gegeven een lijst met videokaarten, geef je een de naam terug
    van de grootste videokaart.

    Bijvoorbeeld:
    >>> grootste_videokaart([{'naam': 'RTX 3080', 'diesize': 628}])
    RTX 3080
    """
    grootste_diesize = 0
    for dicts in lijst_videokaarten:
        if dicts["diesize"] > grootste_diesize:
            grootste_gpu = dicts["naam"]
            grootste_diesize = dicts["diesize"]
    return grootste_gpu



def grootste_videokaartgrootte_per_merk(lijst_videokaarten):
    """Gegeven een lijst met videokaarten, geef je een dictionary terug met
    voor ieder merk de omvang van de grootste kaart.

    Bijvoorbeeld:
    >>> grootste_videokaartgrootte_per_merk([{'naam': 'RTX 3080', 'diesize': 628}])
    {'AMD': 0, 'NVIDIA': 628}
    """
    grootste = {"AMD": 0,
                "NVIDIA": 0,
                }
    for videokaarten in lijst_videokaarten:
        if videokaarten['merk'] == 'AMD':
            if videokaarten['diesize'] > grootste ['AMD']:
                grootste['AMD'] = videokaarten['diesize']

        if videokaarten['merk'] == 'NVIDIA':
            if videokaarten['diesize'] > grootste ['NVIDIA']:
                grootste['NVIDIA'] = videokaarten['diesize']

    return grootste



def diesizes_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over vidoekaarten,
    geef je een lijst van diesizes terug.

    Bijvoorbeeld:
    >>> diesizes_videokaarten([{"diesize": 500}, {"diesize": 300}])
    [421, 320]
    """
    grote_diesize = []

    for grootste_diesizes in lijst_videokaarten:
        die = grootste_diesizes['diesize']
        grote_diesize.append(die)

    return grote_diesize




def gemiddelde_diesize_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je de gemiddelde diesize terug.

    Bijvoorbeeld:
    >>> diesizes_videokaarten([{"diesize": 500}, {"diesize": 300}])
    400
    """
    optelling = 0
    for videokaarten in lijst_videokaarten:
        optelling = optelling+videokaarten["diesize"]

    return optelling/len(lijst_videokaarten)




def jaren_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van jaartalen terug waarin de videokaarten uitgebracht werden.

    Bijvoorbeeld:
    >>> videokaarten_voor_jaar([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}], 2020)
    [2020, 2020]
    """
    lijst_jaren = []
    for dicts in lijst_videokaarten:
        lijst_jaren.append(dicts["jaar"])
    return lijst_jaren



def videokaarten_voor_jaar(lijst_videokaarten, jaar):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van dictionaries terug met informatie over videokaarten
    voor het opgegeven jaar.

    Bijvoorbeeld:
    >>> videokaarten_voor_jaar([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}], 2020)
    [{"jaar": 2020, "diesize": 500}]
    """
    lijst_jaren = []
    for kaart in lijst_videokaarten:
        if kaart["jaar"] == jaar:
            lijst_jaren.append(kaart)
    return lijst_jaren
