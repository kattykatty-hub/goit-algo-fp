import turtle


def draw_pifagor_tree(t, length, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pifagor_tree(t, length * 0.6, depth - 1)
    t.right(90)
    draw_pifagor_tree(t, length * 0.6, depth - 1)
    t.left(45)
    t.backward(length)


def main():
    depth = int(input("Введіть рівень рекурсії: "))

    # Налаштування вікна для малювання
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    # Створення черепахи
    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()

    # Викликаємо функцію для малювання фрактала
    draw_pifagor_tree(t, 150, depth)

    # Закриваємо вікно при натисканні на нього
    screen.mainloop()


if __name__ == "__main__":
    main()
