import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        """
        Constructor for the Hat class
        """
        self.contents = []

        # Get the arguments
        for key, val in kwargs.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, num):
        """
        Attempts to draws a random ball based on the number entered 

        Args:
            num (int): Represents the number of balls to draw

        Returns:
            list: Returns the list of balls (or all balls) based on the number to draw 
        """
        drawn = []

        if num >= len(self.contents):
            return self.contents

        for i in range(num):
            ball = random.choice(self.contents)
            drawn.append(ball)
            self.contents.pop(self.contents.index(ball))

        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Finds the probability of a desired outcome based on:
    https://forum.freecodecamp.org/t/python-probability-calculator-challenge-issues/409711/3

    Args:
        hat (Hat):              Represents a Hat object to use for the experiment
        expected_balls (dict):  Represents the expected number of balls to get
        num_balls_drawn (int):  Represents the number of balls to draw
        num_experiments (int):  Represents the number of times to repeat the experiment

    Returns:
        float: Returns the probability
    """
    num_accurate = 0

    for i in range(num_experiments):
        # Creates a copy the draws from the "hat"
        cpy = copy.deepcopy(hat)
        actual_balls = cpy.draw(num_balls_drawn)
        results = {ball: actual_balls.count(ball)
                   for ball in set(actual_balls)}

        # Compare results to desired results
        accurate = True
        for key, val in expected_balls.items():
            if key not in results or results[key] < expected_balls[key]:
                accurate = False
                break

        if accurate:
            num_accurate += 1

    return num_accurate / num_experiments
