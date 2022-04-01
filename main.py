import turtle
import pandas

# Setting the screen and turtle
STYLE = ('Arial', 7, 'italic')
screen = turtle.Screen()
writer = turtle.Turtle()
writer.penup()

writer.color("black")
writer.hideturtle()


# Mentioning the name on given state
def write_state(answer_row):
    xcor = int(answer_row["x"])
    ycor = int(answer_row["y"])

    writer.goto(xcor, ycor)
    ans_state = str(answer_row["state"].values[0])

    writer.write(ans_state, font=STYLE, align="center")


screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
total = 50
guess = 0
correct_state = []
# Creating the loop to take values from user continuously
while guess != 50:
    answer = screen.textinput(title=f"{guess}/{total} Guess the Sate", prompt="What's another state's name ")
    answer = str.title(answer)
    if answer in data.state.values and answer not in correct_state:
        guess_row = data[data.state == answer]
        write_state(guess_row)
        guess += 1
        correct_state.append(answer)

    # Giving back report after exiting
    elif answer == "Exit":
        state_list = data.state.to_list()
        set1 = set(state_list)
        set2 = set(correct_state)
        remaining = list(sorted(set1 - set2))
        remaining_df = pandas.DataFrame(remaining)
        remaining_df.to_csv("missed.csv")

        break

screen.exitonclick()
