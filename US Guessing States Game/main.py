import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

#create list of the states
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states=[]
missing_states=[]
while len(guessed_states) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct States",
                                 prompt="What is the next state name?").title()

    if ans_state == "Exit":
        break

    if ans_state in all_states:
        guessed_states.append(ans_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans_state)


#save the missing states to .csv
for state in all_states:
    if state not in guessed_states:
        missing_states.append(state)

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("States_to_learn.csv")
