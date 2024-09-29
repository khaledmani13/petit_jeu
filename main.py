"""
nom: Mani
prenom: Khaled
group: G1.1
tp 3
"""
import random

class Jeu:
    """
    Classe représentante du jeu .

    Attributs:
        m (int): Le nombre m reçois en paramètre.
        k (int): Un nombre aléatoire entre 0 et m.

    Examples:
        >>> j = Jeu(10)
        >>> 0 <= j.k <= 10
        True
    """

    def __init__(self, m):
        """
        Constructeur de la classe Jeu.

        Arguments:
            m (int): Le nombre maximum pour le tirage aléatoire.

        Examples:
            >>> j = Jeu(10)
            >>> j.m
            10
        """
        self.m = m
        self.k = random.randint(0, m)

    def test(self, k):
        """
        Comparer le nombre k avec le nombre à deviner.

        Arguments:
            k (int): Le nombre donné par le joueur.

        Returns:
            bool: True si k est égal à k, False sinon.

        Examples:
            >>> j = Jeu(10)
            >>> j.test(j.k)  # On doit gagner si on propose le bon nombre
            'Bravo, tu as gagné !'
            True
        """
        if k < self.k:
            print("Trop petit !")
            return False
        elif k > self.k:
            print("Trop grand !")
            return False
        else:
            print("Bravo, tu as gagné !")
            return True

    def jouer(self):
        """
        Permet de jouer au jeu en demandant des entrées à l'utilisateur.
        """
        while True:
            k = int(input("Entrez un nombre : "))
            if self.test(k):
                break

if __name__ == '__main__':
    import doctest
    doctest.testmod()
