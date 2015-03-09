from __future__ import (absolute_import, division, print_function)

import matplotlib.pyplot as plt
import numpy as np

from napkin.tests import ImageTesting


@ImageTesting(['tan'])
def test_tan():
    # Example of a test that generates one plot ...
    xmin, xmax = -np.pi/2, np.pi/2
    x = np.linspace(xmin, xmax)[1:-1]

    plt.plot(x, np.tan(x))
    plt.grid(True)
    plt.xlim(xmin, xmax)
    plt.ylim(-4, 4)
    # Run the tests in order to generate the expected visual results
    # for each of the associated tests. Then uncomment the following line
    # to cause a test failure for this test ... then from the command line
    # run idiff.py for a visual comparision of the failure ;-)
    # plt.scatter(0, 0)


@ImageTesting(['sin', 'cos'])
def test_sin_cos():
    # Example of a test that generates two plots ...
    xmin, xmax = -np.pi, np.pi
    x = np.linspace(xmin, xmax)

    f1 = plt.figure()
    plt.plot(x, np.sin(x))
    plt.grid(True)
    plt.xlim(xmin, xmax)
    plt.ylim(-1, 1)
    
    f2 = plt.figure()
    plt.plot(x, np.cos(x))
    plt.grid(True)
    plt.xlim(xmin, xmax)
    plt.ylim(-1, 1)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)
