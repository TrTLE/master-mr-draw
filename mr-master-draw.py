import random

src_elements = './elements.txt'
out_draws = './draws.txt'


def draw():
    try:
        with open(src_elements, 'r') as f:
            elements = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("The file "+ src_elements +" does not exist.")
        return

    try:
        with open(out_draws, 'r') as f:
            draws = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        draws = []

    remaining_elements = list(set(elements) - set(draws))

    if not remaining_elements:
        print("All elements have already been drawn.")
        restart_series = input("Do you want to start a new series? [y] [N]")
        if restart_series == 'y':
            with open(out_draws, "r+") as f:
                f.truncate(0)
            draw()
        return

    draw_result = random.choice(remaining_elements)
    print(f"The drawn element is: {draw_result}")

    with open(out_draws, 'a') as f:
        f.write(draw_result + '\n')

if __name__ == "__main__":
    draw()
