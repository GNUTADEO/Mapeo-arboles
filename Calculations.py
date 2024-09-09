"""
Copyright (C) Alvarado Ludwig
ToDo:
La licencia 
"""


import math


def getDiameter(x):
    """
    Args:
     x: Circunferencia del tronco en metros.
    Returns:
     Diametro del tronco en milímetros.
    """
    return (x/math.pi)*1000

def getHeight(alpha, base, heightPerson):
    """
    Args:
     alpha: Ángulo medido en grados.
     base: Distancia en metros desde el tronco hasta
           donde se midió el ángulo.
     heightPerson: Altura de la persona que midió el ángulo en metros.
    Returns:
     Altura del árbol en metros
    """
    return math.tan(math.radians(alpha)) * base + heightPerson


def getDiameterCrown(x):
    """
    Args:
     x: Distancia del tronco hasta la rama más lejana en metros (radio).
    Returns:
     Diametro de la copa del árbol.
    """
    return x*2

def main(circ, angle, distBase, heightHuman, radius):
    return print(f"El diametro del tronco es: {getDiameter(circ)}\nLa altura del árbol es: {getHeight(angle, distBase, heightHuman)}\nEl diámetro de la copa del árbol es: {getDiameterCrown(radius)}")
