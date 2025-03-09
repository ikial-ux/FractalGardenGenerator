import turtle

def apply_rules(axiom, rules, iterations):
    """Expand the L-system axiom using production rules"""
    for _ in range(iterations):
        axiom = "".join(rules.get(char, char) for char in axiom)
    return axiom

def draw_l_system(turtle, axiom, angle, distance, max_steps=10000):
    """Draw the L-system with termination safety"""
    stack = []
    step_count = 0
    
    for char in axiom:
        if step_count >= max_steps:
            print("Safety limit reached!")
            break
            
        if char == "F":
            turtle.forward(distance)
        elif char == "+":
            turtle.right(angle * 1.1)  # Introduce 10% asymmetry
        elif char == "-":
            turtle.left(angle * 0.9)   # Different asymmetry factor
        elif char == "[":
            stack.append((turtle.position(), turtle.heading()))
            turtle.pensize(max(1, turtle.pensize() * 0.8))
        elif char == "]":
            turtle.pensize(turtle.pensize() / 0.8)
            pos, head = stack.pop()
            turtle.penup()
            turtle.goto(pos)
            turtle.setheading(head)
            turtle.pendown()
            
        step_count += 1
        
        # Progress tracking
        if step_count % 500 == 0:
            print(f"Step {step_count} completed")

    return step_count

# Main program
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("midnightblue")

flora = turtle.Turtle()
flora.speed(0)
flora.color("crimson")
flora.pensize(3)

# Initial positioning
flora.penup()
flora.goto(0, -300)
flora.setheading(90)
flora.pendown()

# Draw stem
flora.forward(150)

# Flower configuration
config = {
    "axiom": "F",
    "rules": {"F": "F[+F[+F]-F]F[-F]+F"},  # Asymmetric branching
    "iterations": 4,
    "base_angle": 45,
    "base_distance": 150
}

# Generate L-system string
final_axiom = apply_rules(config["axiom"], config["rules"], config["iterations"])

# Calculate dynamic parameters
distance = config["base_distance"] / (1.6 ** config["iterations"])
angle = config["base_angle"] + 2 * config["iterations"]  # Angle increases with iterations

# Draw the flower
print(f"Starting drawing with {len(final_axiom)} commands...")
completed_steps = draw_l_system(flora, final_axiom, angle, distance)

# Final touch
flora.penup()
flora.goto(0, -120)
flora.color("gold")
flora.dot(25)

print(f"Drawing complete! Total steps: {completed_steps}")
flora.hideturtle()
turtle.done()