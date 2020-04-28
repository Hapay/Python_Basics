# ZADANIE W 31.
def lbs_to_kgs(weight):
    return weight * 0.45


def kgs_to_lbs(weight):
    return weight / 0.45


# ZADANIE W 31.
def find_max(tab):
    highest = tab[0]
    for number in tab:
        if number > highest:
            highest = number
    return highest
