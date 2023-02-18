

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


def coconut_calculator(remaining_coconut, nb_given_monkey, nb_of_pirates):
    for step in range(0, nb_of_pirates):
        if remaining_coconut:
            remaining_coconut = coconut_split(remaining_coconut, nb_given_monkey, nb_of_pirates)
        else:
            return False

    if remaining_coconut:
        remaining_coconut = coconut_split_final_step(remaining_coconut, nb_of_pirates)
    else:
        return False

    if remaining_coconut:
        return remaining_coconut

    return False

nb_pirate = 513469
nb_monkey = 420

test_value =
known_result =


test = coconut_calculator(test_value, nb_monkey, nb_pirate)
print(test)
print()
if known_result == test:
    print(True)
else:
    print(False)
