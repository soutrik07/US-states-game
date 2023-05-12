import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
# we load in new image as a new image in the turtle screen
image = "blank_states_img.gif"
screen.addshape(image)
# now this image is available to be used by turtle
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
# print(data)
# print(data.state)
guessed_states = []
all_states = data.state.to_list()
while len(guessed_states) <= 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess The State",
                                    prompt="What Another State").title()
    # print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        # print(data[data["state"] == answer_state])
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        all_states.remove(answer_state)
        #or
        # t.write(store_data.state.item())
# states_to_learn.csv
print(all_states)
new_data = pandas.DataFrame(all_states)
new_data.to_csv("states_to_learn")
screen.exitonclick()
