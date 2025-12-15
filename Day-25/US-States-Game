import turtle
import pandas

screen = turtle.Screen()
screen.setup(825, 591)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

def is_state_valid(state):
    result = states_data["state"].str.contains(state, case=False, na=False)
    if result.any():
        return True
    else:
        return False

# or simpler method...
# extract states to list and check if states in list
# all_states = states_data.state.to_list()

def print_state(state):
    x_coor = states_data.loc[states_data["state"] == state, "x"].iloc[0]
    y_coor = states_data.loc[states_data["state"] == state, "y"].iloc[0]
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(x_coor, y_coor)
    pen.pendown()
    pen.write(state, align="left", font=("Arial", 8, "bold"))

# or simply extract a row from dataframe where state == current state
# you'll need to use .item() to get the isolated value
# (this grabs first element of data series)
# data_row = states_data[states_data.state == state]
# then pen.goto(data_row.x.item(), data_row.y.item())

states_guessed = []
num_states_guessed = 0
while num_states_guessed < 50:
    answer_state = screen.textinput(title=f"{num_states_guessed}/50 Correct",
                                    prompt="What's another state name?").strip().title()
    if answer_state == "Exit":
        break
    if answer_state not in states_guessed and is_state_valid(answer_state):
        states_guessed.append(answer_state)
        num_states_guessed += 1
        print_state(answer_state)

# create file: states_to_learn.csv
# all state not guessed when game closed.

states_list = states_data.state.tolist()
states_to_learn = [item for item in states_list if item not in states_guessed]
df = pandas.DataFrame({"state": states_to_learn})
df.to_csv("states_to_learn.csv")



