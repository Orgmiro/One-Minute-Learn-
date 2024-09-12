import turtle

def draw_ellipse(turtle_obj, x, y, width, height, color):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color(color)
    turtle_obj.begin_fill()
    
    turtle_obj.left(45)
    for _ in range(2):
        turtle_obj.circle(width, 90)
        turtle_obj.circle(height, 90)
    
    turtle_obj.end_fill()
    turtle_obj.right(45)

def draw_cartoon_poop():
    screen = turtle.Screen()
    screen.bgcolor("white")
    artist = turtle.Turtle()
    artist.speed(2)
    artist.hideturtle()
    
    # Draw the bottom part of the poop
    draw_ellipse(artist, 0, -50, 60, 40, "#6f4f28")
    
    # Draw the middle part of the poop
    artist.penup()
    artist.goto(0, 0)
    artist.pendown()
    draw_ellipse(artist, 0, 0, 50, 35, "#6f4f28")
    
    # Draw the top part of the poop
    artist.penup()
    artist.goto(0, 80)
    artist.pendown()
    draw_ellipse(artist, 0, 80, 40, 30, "#6f4f28")
    
    screen.mainloop()

if __name__ == "__main__":
    draw_cartoon_poop()
