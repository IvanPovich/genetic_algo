from random import randint, random
from operator import add
from functools import reduce

def individual(length, min_val, max_val):
    """Створює одного індивіда (хромосому) для популяції."""
    return [randint(min_val, max_val) for _ in range(length)]

def population(count, length, min_val, max_val):
    """Створює популяцію (набір індивідів)."""
    return [individual(length, min_val, max_val) for _ in range(count)]

def fitness(individual, target):
    """Обчислює значення пристосованості індивіда. Чим менше значення, тим краще."""
    total = reduce(add, individual, 0)
    return abs(target - total)

def grade(pop, target):
    """Обчислює середнє значення пристосованості для всієї популяції."""
    summed = reduce(add, (fitness(x, target) for x in pop), 0)
    return summed / len(pop)

def mutate(individual, chance_to_mutate=0.01):
    """Мутує індивіда, випадково змінюючи один із його генів."""
    for i in range(len(individual)):
        if chance_to_mutate > random():
            individual[i] = randint(min(individual), max(individual))

def crossover(parent1, parent2):
    """Виконує кросовер між двома батьками для створення двох дітей."""
    if len(parent1) != len(parent2):
        raise ValueError("Батьки повинні мати однакову довжину.")
    crossover_point = randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def evolve(pop, target, retain=0.2, random_select=0.05, mutate_chance=0.01):
    """Еволюціонує популяцію до наступного покоління."""
    # Оцінка та сортування популяції за значенням пристосованості
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    
    # Відбір найкращих індивідів для наступного покоління
    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]

    # Випадкове додавання індивідів для генетичного різноманіття
    for individual in graded[retain_length:]:
        if random_select > random():
            parents.append(individual)

    # Мутація деяких індивідів
    for individual in parents:
        mutate(individual, mutate_chance)

    # Кросовер для створення дітей
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length - 1)
        female = randint(0, parents_length - 1)
        if male != female:
            child1, child2 = crossover(parents[male], parents[female])
            children.extend([child1, child2])

    # Об'єднуємо батьків і дітей, щоб створити нову популяцію
    parents.extend(children[:desired_length])
    return parents

# Початкові параметри
target = 371
p_count = 100
i_length = 5
i_min = 0
i_max = 100

# Створення початкової популяції
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target)]

# Генерація поколінь
for i in range(100):
    p = evolve(p, target)
    fitness_history.append(grade(p, target))

# Виведення історії
print("\nВиведення історії: ")
for datum in fitness_history:
    print(datum)
