import random

src_elements = './elements.txt'
out_tirages = './tirages.txt'


def tirage_au_sort():
    try:
        with open(src_elements, 'r') as f:
            elements = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Le fichier "+ src_elements +" n'existe pas.")
        return

    try:
        with open(out_tirages, 'r') as f:
            tirages = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tirages = []

    elements_restants = list(set(elements) - set(tirages))

    if not elements_restants:
        print("Tous les éléments ont déjà été tirés au sort.")
        recommencer_serie = input("Voulez vous recommencer une nouvelle série ? [o] [N]")
        if recommencer_serie == 'o':
            with open(out_tirages, "r+") as f:
                f.truncate(0)
            tirage_au_sort()
        return

    tirage = random.choice(elements_restants)
    print(f"L'élément tiré au sort est : {tirage}")

    with open(out_tirages, 'a') as f:
        f.write(tirage + '\n')

if __name__ == "__main__":
    tirage_au_sort()