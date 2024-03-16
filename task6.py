def greedy_algorithm(items, budget):
    # Створення списку кортежів (назва, вартість, калорії, вартість/калорії)
    item_list = [
        (name, data["cost"], data["calories"], data["calories"] / data["cost"])
        for name, data in items.items()]

    # Сортування списку за співвідношенням вартості/калорії у спадному порядку
    sorted_items = sorted(item_list, key=lambda x: x[3], reverse=True)

    # Ініціалізація результату та поточного бюджету
    result = []
    remaining_budget = budget

    # Вибір страви з максимальним співвідношенням калорій до вартості, доки є бюджет та страви
    for item in sorted_items:
        if remaining_budget >= item[1]:  # Перевірка, чи вистачає бюджету
            result.append(item[0])  # Додавання страви до результату
            remaining_budget -= item[1]  # Віднімання вартості страви від поточного бюджету

    return result


def dynamic_programming(items, budget):
    # Створення матриці, де рядки - страви, стовпці - бюджет
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    # Заповнення матриці
    for i, (name, data) in enumerate(items.items(), start=1):
        cost = data["cost"]
        calories = data["calories"]
        for j in range(1, budget + 1):
            if cost > j:
                dp_table[i][j] = dp_table[i - 1][j]
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - cost] + calories)

    # Відновлення найкращого набору страв
    result = []
    j = budget
    for i in range(len(items), 0, -1):
        if dp_table[i][j] != dp_table[i - 1][j]:
            result.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]

    return result[::-1]


# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

print("Greedy Algorithm Result:", greedy_algorithm(items, budget))
print("Dynamic Programming Result:", dynamic_programming(items, budget))
