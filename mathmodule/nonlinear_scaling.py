import numpy as np
import matplotlib.pyplot as plt


def bisection(a, b, f, e):
    """
    This function finds the solution of the nonlinear equation by bisection method.

    :param a: Start
    :param b: End
    :param f: Nonlinear func
    :param e: Accuracy
    :return: Solution of the nonlinear equation by bisection method
    """
    if f(a) * f(b) > 0:
        raise Exception("The scalars a and b do not bound a root")
    else:
        x = (a + b) / 2
        if np.abs(f(x)) < e:
            return x
        elif np.sign(f(a)) == np.sign(f(x)):
            return bisection(x, b, f, e)
        elif np.sign(f(b)) == np.sign(f(x)):
            return bisection(a, x, f, e)


def newton_method(a, b, f, f_1, e):
    """
    This function finds the solution of the nonlinear equation by newton method.

    :param a: Start
    :param b: End
    :param f: Nonlinear func
    :param f_1: Derivative of nonlinear func
    :param e: Accuracy
    :return: Solution of nonlinear equation
    """
    x_0 = (a + b) / 2
    xn = f(x_0)
    xn_1 = xn - (f(xn) / f_1(xn))
    while np.abs(xn_1 - xn) > e:
        xn = xn_1
        xn_1 = xn - (f(xn) / f_1(xn))
    return xn_1


def chord(a, b, f):
    """
    This function finds the solution of the nonlinear equation by chord method.

    :param a: Start
    :param b: End
    :param f: Nonlinear func
    :return: Solution of nonlinear equation
    """
    if f(a) * f(b) >= 0:
        raise Exception("The scalars a and b do not bound a root")
    an = a
    bn = b
    for n in range(1000):
        x = an - f(an) * (bn - an) / (f(bn) - f(an))
        if f(an) * f(x) < 0:
            bn = x
        elif f(bn) * f(x) < 0:
            an = x
        elif f(x) == 0:
            return x
        else:
            raise Exception("No roots in this interval.")
    return x


if __name__ == "__main__":

    f = lambda x: x ** 3 + 20 * x - 10 * np.cos(x)
    f_1 = lambda x: 3 * (x ** 2) - 20 + 10 * np.sin(x)
    e = 0.000001
    x = np.linspace(-2, 10, 1000)
    plt.plot(x, f(x))
    plt.show()
    a = float(input('Segment start: '))
    b = float(input('End of segment: '))
    print("Bisection method: ", bisection(a, b, f, e))
    print("Newton's method: ", newton_method(a, b, f, f_1, e))
    print("Chord method: ", chord(a, b, f))
