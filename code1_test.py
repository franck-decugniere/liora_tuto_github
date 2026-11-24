from code1 import total


def test_total():
    # Les uses cases
    """La somme de la liste [1, 2, 3] est 6"""
    assert total([1, 2, 3]) == 6

    """La somme de la liste [1, -1] est 0"""
    assert total([1, -1]) == 0

    """-1 -1 = -2"""
    assert total([-1, -1]) == -2

    # Les edge cases :
    """La somme doit être égale à l'unique élément"""
    assert total([1.0]) == 1.0

    """La somme d'une liste vide doit être 0"""
    assert total([]) == 0
