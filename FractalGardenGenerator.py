import turtle

def apply_rules(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = "".join(rules.get(char, char) for char in axiom)
    return axiom

def draw_l_system(axiom, angle, distance):
    stack = []
    for char in axiom:
        if char == "F":
            turtle.forward(distance)
        elif char == "+":
            turtle.right(angle)
        elif char == "-":
            turtle.left(angle)
        elif char == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif char == "]":
            pos, head = stack.pop()
            turtle.penup()
            turtle.goto(pos)
            turtle.setheading(head)
            turtle.pendown()

turtle.speed(0)
axiom = "F"
rules = {"F": "F+F-F-F+F"}
iterations = 4
final_axiom = apply_rules(axiom, rules, iterations)
draw_l_system(final_axiom, 90, 10)
turtle.done()
