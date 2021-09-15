from math import pi, sqrt

import math

def oppervlakte_kegel(r, h):
    # Zoek via Google naar "area cone"
    # l = vierkantswortel(r^2 + h^2)
    # A = π * r * l + π * r^2
    l = sqrt(r**2 + h**2)
    return pi * r * l + pi * r**2


def last_element(l):
    """Return het laatste element uit een lijst"""
    return l[-1]


def sum_of_list(l):
    """Return de som van alle elementen uit een lijst"""
    return sum(l)


def average_of_list(l):
    """Return het gemiddelde van alle elementen uit een lijst"""
    n = len(l)
    s = sum(l)
    return s / n


def min_max_of_list(l):
    """Return het minimum en het maximum van de elementen uit een lijst"""
    n = max(l)
    s = min(l)
    return (s, n)


def squared_list(l):
    """Return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst

    squared_list([2,3]) == [4, 9]
    """
    n = [x**2 for x in (l)]
    return n


def differences_list(l1, l2):
    lijst1 = (l1)
    lijst2 = (l2)
    difference = lijst1 - lijst2
    return difference


def replace_takis_mr_issaris(text):
    n = text.replace("Takis", "Mr. Issaris")
    return n
