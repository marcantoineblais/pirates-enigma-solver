from functools import cache

solutions = []
solution_remainder = []
completion_percent_shown = []


def number_validation(question):
    number_entered_str = input(question)
    try:
        number_entered_int = int(number_entered_str)
    except ValueError:
        print("Veuillez entrer un nombre.")
        return number_validation(question)
    return number_entered_int


def coconut_split(nb_of_coconut, nb_given_monkey, nb_of_pirates):
    if nb_of_coconut % nb_of_pirates == nb_given_monkey:
        coconut_shared = (nb_of_coconut // nb_of_pirates) * (nb_of_pirates - 1)
        return coconut_shared
    return False


def coconut_split_final_step(nb_of_coconut, nb_of_pirates):
    if nb_of_coconut % nb_of_pirates == 0:
        coconut_shared = (nb_of_coconut // nb_of_pirates)
        return coconut_shared
    return False


def timer(step, last_step, interval, interval_step):
    completion = round((step / last_step) * 100, 0)
    if completion not in completion_percent_shown and completion % interval == 0:
        print(f"{completion}% done.")
        completion_percent_shown.append(completion)
    return step + interval_step


def timer_interval(last_step_exp):
    if last_step_exp < 6:
        interval = 10
    elif last_step_exp < 10:
        interval = 5
    else:
        interval = 1
    return interval


def coconut_calculator(remaining_coconut, nb_given_monkey, nb_of_pirates, nb_of_coconut):
    for step in range(0, nb_of_pirates):
        if remaining_coconut:
            remaining_coconut = coconut_split(remaining_coconut, nb_given_monkey, nb_of_pirates)
        else:
            return

    if remaining_coconut:
        remaining_coconut = coconut_split_final_step(remaining_coconut, nb_of_pirates)
    else:
        return

    if remaining_coconut:
        solutions.append(nb_of_coconut)
        solution_remainder.append(remaining_coconut)
    return remaining_coconut


def show_results():
    if len(solutions) == 0:
        print()
        print("Aucune solution.")
    elif len(solutions) == 1:
        print()
        print(f"L'unique solution : {solutions[0]} noix de coco.")
        print(f"Nombre de noix de coco par pirate à la fin = {solution_remainder[0]} noix de coco.")
    else:
        index = 0
        print()
        for solution in solutions:
            print(f"Solution #{len(solutions[0: index]) + 1} :")
            print(f"Nombre total de noix de coco : {solution} noix de coco.")
            print(f"Nombre de noix de coco par pirate à la fin = {solution_remainder[index]} noix de coco.")
            print()
            index += 1
        print()
        print(f"Plus petite solution : {solutions[0]} noix de coco.")
        print(f"Plus grande solution : {solutions[-1]} noix de coco.")
        print(f"Nombre de solutions : {len(solutions)} solutions.")


nb_pirate = number_validation("Combien de pirates sont sur l'ile? ")
nb_monkey = number_validation("Combien de noix de coco chaque pirate donne au singe? ")
if nb_monkey >= nb_pirate:
    print(f"Aucune solution possible, le nombre de noix de coco donné au singe doit être plus petit que {nb_pirate}.")
    nb_monkey = number_validation("Combien de noix de coco chaque pirate donne au singe? ")
max_coconut_exp = number_validation(
    "Jusqu'à quel nombre voulez-vous chercher des solutions? Choisissez une puissance de 10 : "
)
max_coconut = 10 ** max_coconut_exp
step_counter = 0

percentage_interval = timer_interval(max_coconut_exp)

for nb_coconut in range(nb_monkey + nb_pirate, max_coconut + nb_monkey, nb_pirate):
    coconut_calculator(nb_coconut, nb_monkey, nb_pirate, nb_coconut)
    step_counter = timer(step_counter, max_coconut + nb_monkey, percentage_interval, nb_pirate)

show_results()

