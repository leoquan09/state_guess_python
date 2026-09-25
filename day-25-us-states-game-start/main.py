import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
names = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50", "What's another state name?").title()

    if answer == "Exit":
        missing_states = []
        for state in names:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in names:
        row = data[data["state"] == answer]
        x = row["x"].item()
        y = row["y"].item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer)
        guessed_states.append(answer)




screen.mainloop()