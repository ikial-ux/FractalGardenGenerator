import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("navy")

flower = turtle.Turtle()
flower.speed(0)
flower.color("orchid")
flower.pensize(2)

# Start position at bottom center
flower.penup()
flower.goto(0, -250)
flower.setheading(90)
flower.pendown()

# Draw simple stem
flower.forward(100)
flower.penup()
flower.forward(40)
flower.pendown()

def apply_rules(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = "".join(rules.get(char, char) for char in axiom)
    return axiom

def draw_l_system(axiom, angle, distance):
    stack = []
    for char in axiom:
        if char == "F":
            flower.forward(distance)
        elif char == "+":
            flower.right(angle + 5)  # Add variation to break symmetry
        elif char == "-":
            flower.left(angle - 5)  # Asymmetric angle modification
        elif char == "[":
            stack.append((flower.position(), flower.heading()))
            flower.pensize(max(1, flower.pensize() * 0.7))  # Reduce thickness
        elif char == "]":
            flower.pensize(flower.pensize() / 0.7)
            pos, head = stack.pop()
            flower.penup()
            flower.goto(pos)
            flower.setheading(head)
            flower.pendown()

# Modified L-system rules for twisted petals
axiom = "F"
rules = {
    "F": "F[+FF][-F+F]",  # Asymmetric branching pattern
    "+": "+",
    "-": "-",
    "[": "[",
    "]": "]"
}
iterations = 4
angle = 50  # Non-divisor of 360 to prevent perfect circles
final_axiom = apply_rules(axiom, rules, iterations)

# Dynamic scaling with twist factor
base_distance = 80
distance = base_distance / (1.3 ** iterations)

# Draw the twisted flower
draw_l_system(final_axiom, angle, distance)

# Add spiral center
flower.penup()
flower.goto(0, -110)
flower.color("gold")
for _ in range(20):
    flower.forward(5)
    flower.right(30)
    flower.stamp()

flower.hideturtle()
turtle.done()