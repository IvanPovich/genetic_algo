# Генетичний Алгоритм для Мінімізації Різниці до Цільової Суми

## Мета

Реалізувати генетичний алгоритм для знаходження набору чисел, сума яких найближча до заданого значення `TARGET_SUM`.

## Огляд

Генетичний алгоритм імітує процес природного відбору для наближення до оптимального розв'язку. Кожна "особина" (хромосома) є набором чисел, які підсумовуються і порівнюються з цільовою сумою.

## Параметри

- **POPULATION_SIZE**: Кількість особин у популяції.
- **CHROMOSOME_LENGTH**: Кількість чисел у хромосомі.
- **GENE_MIN** та **GENE_MAX**: Діапазон значень чисел.
- **TARGET_SUM**: Цільова сума.
- **GENERATIONS**: Кількість поколінь.
- **MUTATION_RATE**: Ймовірність мутації гена.

## Ключові Функції

1. **Фітнес-функція**: Обчислює відхилення суми чисел у хромосомі від `TARGET_SUM`.
2. **create_population**: Створює початкову популяцію.
3. **selection**: Відбирає найкращих особин для схрещування.
4. **crossover**: Комбінує двох батьків для створення нового потомства.
5. **mutate**: Застосовує мутацію з ймовірністю `MUTATION_RATE`.

## Використання
Відкритий приклад генетичного алгоритму (https://stackoverflow.com/questions/31011585/python-genetic-algorithm)

Результат виконання коду прикріплено на зображенні
### Запуск коду

Запустіть алгоритм для 100 поколінь:
```python
genetic_algorithm()
