"""Calculate Pi using random number generator"""
import math
import random


def calculate_pi(iterations):
    """
    area_of_a_circle = Pi * radius**2
    Pi = area_of_a_circle / radius**2

    in our case radius is 1 (random() return float:  0.0 <= x < 1.0)
    and area_of_a_circle could be calculated using Monte-Karlo method.

    Generate random dots and look if they hit inside the circle (len <= 1)
    or not (len > 1). And calculate as relative to the square
    around the circle.

    NOTE: Keep in mind that [0..1, 0..1] squaore it's 1/4 of full circle
    """
    random.seed()

    inside = 0
    for _ in range(iterations):
        a_x = random.random()
        b_y = random.random()

        # calculate len
        c_len = math.sqrt(math.pow(a_x, 2) + math.pow(b_y, 2))
        if c_len <= 1:
            inside += 1

    # calculate area for 1/4 of circle
    s_area = float(inside) / float(iterations)

    return s_area * 4  # full square


print('Pi: {}'.format(calculate_pi(1000000)))


