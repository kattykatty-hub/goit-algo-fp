import networkx as nx
import heapq
from subtask1 import G as G_weighted


def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченні
    distances = {node: float('inf') for node in graph}
    # Відстань до початкової вершини стартує з нуля
    distances[start] = 0
    # Процесори, які очікують на обробку
    pq = [(0, start)]

    while pq:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_node = heapq.heappop(pq)

        # Якщо поточна відстань більша за відстань, яка вже була оброблена, пропускаємо
        if current_distance > distances[current_node]:
            continue

        # Проходимо по всіх сусідах поточної вершини
        for neighbor, e in graph[current_node].items():
            weight = e["weight"]
            distance = current_distance + weight

            # Якщо знайдено меншу відстань до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


if __name__ == '__main__':
    # Знаходимо найкоротші шляхи від кожної вершини до всіх інших
    all_shortest_paths = {}
    for start_node in G_weighted.nodes:
        shortest_paths = dijkstra(G_weighted, start_node)
        all_shortest_paths[start_node] = shortest_paths

    # Виводимо результат
    for start_node, shortest_paths in all_shortest_paths.items():
        print(f"Найкоротші шляхи з вершини {start_node}:")
        for end_node, distance in shortest_paths.items():
            print(f"  До вершини {end_node}: Відстань = {distance}")
