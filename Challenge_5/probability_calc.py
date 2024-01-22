class Hat:

    def __init__(
            self, red=0, orange=0, black=0, blue=0,
            pink=0, striped=0, yellow=0, green=0) -> None:
        colors = {'red': red, 'orange': orange, 'black': black, 'blue': blue,
                  'pink':pink, 'striped':striped, 'yellow':yellow, 'green':green}
        self.content = []
        self.amount = 0
        for color in colors.items():
            if color[1] > 0:
                for c in range(color[1]):
                    self.content.append(color[0])
                    self.amount += 1

    def draw(self, number) -> str:
        from random import choice
        chosen_list = []
        try:
            for c in range(number):
                chosen = choice(self.content)
                self.content.remove(chosen)
                print(f'\033[32mThe removed item was {chosen}.\033[m')
                self.amount -= 1
                chosen_list.append(chosen)
        except:
            print('\033[31mThe hat is empty.\033[m')
        return chosen_list
    
def experiment(
        hat: Hat, expected: dict, balls_drawn: int, experiments: int
        ) -> str:
    n = ok = 0
    for c in range(experiments):
        balls_to_check = []
        hat2 = Hat(black=6, red=4, green=3)
        balls = hat2.draw(balls_drawn)
        for d in expected.items():
            for c in range(d[1]):
                balls_to_check.append(d[0])
        for ball in balls:
            if ball in balls_to_check:
                balls_to_check.remove(ball)
                if len(balls_to_check) == 0:
                    n += 1
        print(f'{n} times')
        balls_to_check = []

    try:
        print(f'The probability was {n/experiments*100:.2f}%')
    except:
        print('The probability was 0%')
