import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightcyan")

flower = turtle.Turtle()
flower.speed(0)
flower.color("coral")  # Flower color
flower.pensize(2)

# Start position at bottom to draw stem
flower.penup()
flower.goto(0, -250)
flower.pendown()

# Draw stem
flower.setheading(90)
flower.forward(100)
flower.penup()
flower.forward(40)  # Move up to flower position
flower.pendown()

# Flower parameters
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
            flower.right(angle)
        elif char == "-":
            flower.left(angle)
        elif char == "[":
            stack.append((flower.position(), flower.heading()))
        elif char == "]":
            pos, head = stack.pop()
            flower.penup()
            flower.goto(pos)
            flower.setheading(head)
            flower.pendown()

# L-system configuration for flower
axiom = "F"
rules = {
    "F": "F[+F]F[-F]+F",  # Creates branching pattern
    "+": "+",
    "-": "-",
    "[": "[",
    "]": "]"
}
iterations = 5
angle = 25.7  # Creates approximately 14 branches for full circle
final_axiom = apply_rules(axiom, rules, iterations)

# Calculate dynamic distance scaling
distance = 150 / (1.5 ** iterations)

# Draw the flower
draw_l_system(final_axiom, angle, distance)

# Add flower center
flower.penup()
flower.goto(0, -110)
flower.color("gold")
flower.dot(30)

flower.hideturtle()
turtle.done()