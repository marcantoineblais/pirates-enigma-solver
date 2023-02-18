import time

solutions = []
solution_remainder = []
completion_percent_shown = []


def number_validation(question, restriction=False):
  number_entered_str = input(question)
  try:
    number_entered_int = int(number_entered_str)
  except ValueError:
    print("Veuillez entrer un nombre.")
    return number_validation(question)
  if restriction:
    if number_entered_int >= restriction:
      print(
        f"Aucune solution possible, le nombre de noix de coco donné au singe doit être plus petit que "
        f"{nb_pirate}."
      )
    return number_validation(question, restriction)
  return number_entered_int


def coconut_calculator_1st_solution(nb_of_pirates, coconut_given_monkey, step, last_step):
  if nb_of_pirates % 2 == 1:
    result = ((nb_of_pirates ** nb_of_pirates) * coconut_given_monkey) - (coconut_given_monkey *
                                                                              (nb_of_pirates - 1))
  else:
    result = (((nb_of_pirates ** nb_of_pirates) * coconut_given_monkey) * (nb_of_pirates-1) -
      (coconut_given_monkey * (nb_of_pirates - 1))) - \
      ((nb_of_pirates ** (nb_of_pirates + 1)) * (coconut_given_monkey - 1))
  solutions.append(result)
  step = timer(step, last_step)
  return result, step


def coconut_calculator_next_solutions(previous_solution, nb_of_pirates, step, last_step):
  next_solution = previous_solution + nb_of_pirates**(nb_of_pirates+1)
  solutions.append(next_solution)
  step = timer(step, last_step)
  return next_solution, step


def coconut_split_first(nb_of_pirates, nb_given_monkey):
  if nb_of_pirates % 2 == 1:
    coconut_shared = (((((nb_of_pirates - 1) ** nb_of_pirates) * nb_given_monkey) + nb_given_monkey) // nb_of_pirates) - nb_given_monkey
  else:
    coconut_shared = (((((nb_of_pirates - 1) ** nb_of_pirates) * (nb_of_pirates - 1) - (nb_of_pirates - 1)) // nb_of_pirates) * nb_given_monkey) - (((nb_of_pirates - 1) ** nb_of_pirates) * (nb_given_monkey - 1))
  solution_remainder.append(coconut_shared)
  return coconut_shared


def coconut_split_next(nb_of_coconut, nb_of_pirates):
  coconut_shared = nb_of_coconut + ((nb_of_pirates - 1) ** nb_of_pirates)
  solution_remainder.append(coconut_shared)
  return coconut_shared


def timer(step, last_step):
  completion = int(round((step / last_step) * 100, 0))
  if completion > 100:
    completion = 100
  if completion not in completion_percent_shown:
    print(f"{completion}% done.")
    completion_percent_shown.append(completion)
  step += nb_pirate ** (nb_pirate + 1)
  return step


def show_results(nb_of_pirates, nb_monkey, max_coconut_exp):
  if len(solutions) == 0:
    print()
    print("Aucune solution.")
    log_result(nb_of_pirates)
  elif len(solutions) == 1:
    print()
    print(f"L'unique solution : {solutions[0]} noix de coco.")
    print(f"Nombre de noix de coco par pirate à la fin = {solution_remainder[0]} noix de coco.")
    log_result(nb_of_pirates)
  else:
    print()
    print(f"Plus petite solution : {solutions[0]} noix de coco.")
    print(f"Plus grande solution : {solutions[-1]} noix de coco.")
    print(f"Nombre de solutions : {len(solutions)} solutions.")
    log_final(nb_of_pirates, nb_monkey, max_coconut_exp)


def log_param(nb_of_pirates, nb_given_monkey, exponent):
  log = open(f"{nb_of_pirates}pirates_{nb_monkey}remainder_10({max_coconut_exp})range.txt", "w+")
  log.write(f"Nombre de pirates sur l'ile : {nb_of_pirates}\n")
  log.write(f"Nombre de noix de coco donnée au singe à chaque round : {nb_given_monkey}\n")
  log.write(f"Range maximum recherché : 10^{exponent}\n")
  log.write("_______________________________________________________________________\r\n")
  log.close()
  return


def log_result(nb_of_pirates):
  log = open(f"{nb_of_pirates}pirates_{nb_monkey}remainder_10({max_coconut_exp})range.txt", "a+")
  if len(solutions) == 0:
    log.write("Aucune solution.\n")
  elif len(solutions) == 1:
    log.write(f"L'unique solution : {solutions[0]} noix de coco.\n")
    log.write(f"Nombre de noix de coco par pirate à la fin = {solution_remainder[0]} noix de coco.\n")
  log.close()
  return


def log_final(nb_of_pirates, nb_monkey, max_coconut_exp):
  log = open(f"{nb_of_pirates}pirates_{nb_monkey}remainder_10({max_coconut_exp})range.txt", "a+")
  log.write(f"Plus petite solution : {solutions[0]} noix de coco.\n")
  log.write(f"Plus grande solution : {solutions[-1]} noix de coco.\n")
  log.write(f"Nombre de solutions : {len(solutions)} solutions.\n")
  log.write("______________________________________________________________________\r\n")
  index = 0
  for a in solutions:
    log.write(f"Solution #{index + 1} sur {len(solutions)}:\n")
    log.write(f"Nombre total de noix de coco : {a} noix de coco.\n")
    log.write(f"Nombre de noix de coco par pirate à la fin = {solution_remainder[index]} noix de coco.\r\n")
    index += 1
  log.close()
  return


nb_pirate = number_validation("Combien de pirates sont sur l'ile? ")
nb_monkey = number_validation("Combien de noix de coco chaque pirate donne au singe? ", nb_pirate)
max_coconut_exp = number_validation(
  "Jusqu'à quel nombre voulez-vous chercher des solutions? Choisissez une puissance de 10 : "
)
max_coconut = 10 ** max_coconut_exp
step_counter = 0


log_param(nb_pirate, nb_monkey, max_coconut_exp)

coconut, step_counter = coconut_calculator_1st_solution(nb_pirate, nb_monkey, step_counter, max_coconut)
while coconut <= max_coconut - (nb_pirate ** (nb_pirate + 1)):
  coconut, step_counter = coconut_calculator_next_solutions(coconut, nb_pirate, step_counter, max_coconut)

if 100 not in completion_percent_shown:
  print("100% done.")
coconuts_left = coconut_split_first(nb_pirate, nb_monkey)
if len(solutions) > 1:
  for solution in solutions:
    coconuts_left = coconut_split_next(coconuts_left, nb_pirate)

show_results(nb_pirate, nb_monkey, max_coconut_exp)
