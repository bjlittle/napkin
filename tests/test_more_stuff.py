from __future__ import (absolute_import, division, print_function)

import matplotlib.pyplot as plt
import numpy as np

from napkin.tests import ImageTesting


@ImageTesting(['wibble'])
def test_wibble():
    plt.text(0, 0, 'wibble', ha='center')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)


if __name__ == '__main__':
    import nose
    nose.runmodule(argv=['-s', '--with-doctest'], exit=False)
