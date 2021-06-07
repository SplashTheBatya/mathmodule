import math
from mathmodule.rectangle import *


def rectangle_method(start: float, end: float, f, steps: int, variation='trapezium',):
    """
    Scaling integral sum by chosen method

    :param start :type float: start point
    :param end :type float: end point
    :param f :type function: math function, f(x)
    :param variation :type str: one of defined method
    :return: integral sum
    """
    if variation not in rectangle_methods_dict:
        raise ValueError(f'Unknown extraction method , try one of this: {rectangle_methods_dict}')
    if variation == 'trapezium':
        return trapezium_method(start, end, f, steps)
    elif variation == 'left':
        return left_rectangle_method(start, end, f, steps)
    else:
        return right_rectangle_method(start, end, f, steps)


def simpsons_method(start: float, end: float, f):
    """
    Sipmsons_metgod:
    Calculates the integral sum by Simpson's rule

    :param start :type float: starting point
    :param end :type float: end point
    :param f :type function: f(x), integrate function
    :return: result :type float, integral sum
    """
    step = abs(end - start) / steps
    sum1 = 0
    sum2 = 0
    for i in range(1, int(steps / 2)):
        sum1 += f(step * (2 * i - 1))
    for i in range(1, int(steps / 2 - 1)):
        sum2 += f(step * (2 * i))

    sum = step / 3 * (f(start) + 4 * sum1 + 2 * sum2 + f(end))
    return sum


if __name__ == '__main__':
    steps = 1000000
    print(rectangle_method(0, math.pi * 2, math.cos, steps, 'trapezium'))
    print(rectangle_method(0, math.pi * 2, math.cos, steps, 'right_rect'))
    print(rectangle_method(0, math.pi * 2, math.cos, steps, 'left_rect'))
    print(simpsons_method(0, math.pi * 2, math.cos))
