
rectangle_methods_dict = ['trapezium', 'left_rect', 'right_rect']


def right_rectangle_method(start: float, end: float, f, steps: int):
    """
    Right_rectangle_method:
    Calculates the integral sum by dividing it into rectangles equal in x
    and summing it up, taking the right vertical side of the rectangle with height f(x)
    as the value of the function

    :param start :type float: starting point,
    :param end  :type float: end point
    :param f :type function: f(x), integrate function,
    :param steps :type int: value of overall steps accuracy
    :return sum :type float: result, integral sum

    step - size of x value deference per one summing period, delta(x)
    """
    step = abs(end - start) / steps
    x = start
    sum = 0
    while x < end:
        x += step
        sum += f(x) * step
    return sum


def left_rectangle_method(start: float, end: float, f, steps: int):
    """
    Left_rectangle_method:
    Calculates the integral sum by dividing it into rectangles equal in x
    and summing it up, taking the left vertical side of the rectangle with height f(x)
    as the value of the function

    :param start :type float: starting point
    :param end :type float: end point
    :param f :type function: f(x), integrate function
    :param steps :type int: value of overall steps accuracy
    :return: result :type float, integral sum
    """
    step = abs(end - start) / steps
    x = start
    sum = 0
    while x < end:
        sum += f(x) * step
        x += step
    return sum


def trapezium_method(start: float, end: float, f, steps: int):
    """
    Trapezium_method:
    Calculates the integral sum by dividing it into rectangles equal in x
    and summing it up, taking the the average value between previous x and x + delta(x) vertical side of the rectangle with height f(x)
    as the value of the function
    :param start :type float: starting point
    :param end :type float: end point
    :param f :type function: f(x), integrate function
    :param steps :type int: value of overall steps accuracy
    :return: result :type float, integral sum
    """
    step = abs(end - start) / steps
    x = start
    sum = 0
    while x < end:
        sum += (f(x - step) + f(x)) / 2 * step
        x += step
    return sum