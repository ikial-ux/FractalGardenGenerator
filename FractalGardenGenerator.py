import turtle

def apply_rules(axiom, rules, iterations):
    """Expand the initial axiom using production rules"""
    for _ in range(iterations):
        new_axiom = []
        for char in axiom:
            new_axiom.append(rules.get(char, char))
        axiom = ''.join(new_axiom)
    return axiom

def draw_l_system(t, axiom, angle, length):
    """Interpret and draw the L-system string"""
    stack = []
    for char in axiom:
        if char == "F":
            t.forward(length)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
        elif char == "[":
            stack.append((t.position(), t.heading()))
            t.pensize(max(1, t.pensize() * 0.8))  # Thinner branches
        elif char == "]":
            t.pensize(t.pensize() / 0.8)
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

# Set up turtle window
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("black")

# Configure turtle
plant = turtle.Turtle()
plant.speed(0)
plant.color("limegreen")
plant.pensize(3)
plant.left(75)  # Initial angle of 75 degrees

# L-system parameters from user input
rules = {
    "X": "F-[[X]+X]+F[+FX]-X",
    "F": "FF"
}
axiom = "X"
iterations = 5
segment_length = 5
angle = 22.5

# Generate L-system string
final_axiom = apply_rules(axiom, rules, iterations)

# Position turtle at bottom center
plant.penup()
plant.goto(0, -400)
plant.pendown()

# Draw the plant structure
draw_l_system(plant, final_axiom, angle, segment_length)

plant.hideturtle()
turtle.done()