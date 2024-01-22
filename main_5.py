from Challenge_5 import experiment, Hat

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat, expected={"red": 2, "green": 1},
                         balls_drawn=5, experiments=200)