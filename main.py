#### Imports et définition des variables globales
""" Ex 08 : lectures de données
"""
FILENAME = "listes.csv"

#### Fonctions secondaires
def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l=[]
    with open(filename, mode='r', encoding='utf8') as f :
        for line in f:
            l.append([int(value) for value in line.strip().split(';')])
    return l

def get_list_k(data, k):
    """ retourne la liste d'indice k"""
    l = data[k]
    return l

def get_first(l):
    """ retourne le premier élément de la liste"""
    return l[0]

def get_last(l):
    """ retourne le dernier élément de la liste"""
    return l[len(l)-1]

def get_max(l):
    """retourne le maximum de la liste"""
    return max(l)

def get_min(l):
    """retourne le minimum de la liste"""
    return min(l)

def get_sum(l):
    """retourne la somme de la liste"""
    return l.get_first + get_sum(l.pop(0))

#### Fonction principale
def main():
    """test et vérifie les fonctions secondaire
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
