import random
from collections import Counter

class Hat:
    def __init__(self, **kwargs):
        self.contents = [key for key in kwargs for i in range(kwargs[key])]

    def draw(self, num_balls):
        balls = []
        for _ in range(min(num_balls, len(self.contents))):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls.append(ball)
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        hat_copy = Hat(**Counter(hat.contents))
        balls_drawn = hat_copy.draw(num_balls_drawn)
        if all(balls_drawn.count(ball) >= expected_balls[ball] for ball in expected_balls):
            count += 1

    return count / num_experiments

hat = Hat(black=6, red=4,green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1},num_balls_drawn=5, num_experiments=2000)
print(probability)